// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_EVALP_HPP
#define EVALHYD_EVALP_HPP

#include <unordered_map>
#include <vector>

#include <xtl/xoptional.hpp>
#include <xtensor/xexpression.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xarray.hpp>
#include <xtensor/xadapt.hpp>

#include "detail/utils.hpp"
#include "detail/masks.hpp"
#include "detail/uncertainty.hpp"
#include "detail/probabilist/evaluator.hpp"


namespace evalhyd
{
    /// Function to evaluate probabilistic streamflow predictions.
    ///
    /// \rst
    ///
    /// :Template Parameters:
    ///
    ///    XD2: Any 2-dimensional container class storing numeric elements
    ///         (e.g. ``xt::xtensor<double, 2>``, ``xt::pytensor<double, 2>``,
    ///         ``xt::rtensor<double, 2>``, etc.).
    ///
    ///    XD4: Any 4-dimensional container class storing numeric elements
    ///         (e.g. ``xt::xtensor<double, 4>``, ``xt::pytensor<double, 4>``,
    ///         ``xt::rtensor<double, 4>``, etc.).
    ///
    ///    XB4: Any 4-dimensional container class storing boolean elements
    ///         (e.g. ``xt::xtensor<bool, 4>``, ``xt::pytensor<bool, 4>``,
    ///         ``xt::rtensor<bool, 4>``, etc.).
    ///
    ///    XS2: Any 2-dimensional container class storing string elements
    ///         (e.g. ``xt::xtensor<std::array<char, 32>, 2>``,
    ///         ``xt::pytensor<std::array<char, 32>, 2>``,
    ///         ``xt::rtensor<std::array<char, 32>, 2>``, etc.).
    ///
    /// :Parameters:
    ///
    ///    q_obs: ``XD2``
    ///       Streamflow observations. Time steps with missing observations
    ///       must be assigned `NAN` values. Those time steps will be ignored
    ///       both in the observations and the predictions before the
    ///       *metrics* are computed.
    ///       shape: (sites, time)
    ///
    ///    q_prd: ``XD4``
    ///       Streamflow predictions. Time steps with missing predictions
    ///       must be assigned `NAN` values. Those time steps will be ignored
    ///       both in the observations and the predictions before the
    ///       *metrics* are computed.
    ///       shape: (sites, lead times, members, time)
    ///
    ///    metrics: ``std::vector<std::string>``
    ///       The sequence of evaluation metrics to be computed.
    ///
    ///       .. seealso:: :doc:`../../metrics/probabilistic`
    ///
    ///    q_thr: ``XD2``, optional
    ///       Streamflow exceedance threshold(s). If provided, *events* must
    ///       also be provided.
    ///       shape: (sites, thresholds)
    ///
    ///    events: ``std::string``, optional
    ///       The type of streamflow events to consider for threshold
    ///       exceedance-based metrics. It can either be set as "high" when
    ///       flooding conditions/high flow events are evaluated (i.e. event
    ///       occurring when streamflow goes above threshold) or as "low" when
    ///       drought conditions/low flow events are evaluated (i.e. event
    ///       occurring when streamflow goes below threshold). It must be
    ///       provided if *q_thr* is provided.
    ///
    ///    c_lvl: ``std::vector<double>``, optional
    ///       Confidence interval(s).
    ///
    ///    t_msk: ``XB4``, optional
    ///       Mask(s) used to generate temporal subsets of the whole streamflow
    ///       time series (where True/False is used for the time steps to
    ///       include/discard in a given subset). If not provided and neither
    ///       is *m_cdt*, no subset is performed and only one set of metrics is
    ///       returned corresponding to the whole time series. If provided, as
    ///       many sets of metrics are returned as they are masks provided.
    ///       shape: (sites, lead times, subsets, time)
    ///
    ///       .. seealso:: :doc:`../../functionalities/temporal-masking`
    ///
    ///    m_cdt: ``XS2``, optional
    ///       Masking conditions to use to generate temporal subsets. Each
    ///       condition consists in a string and can be specified on
    ///       observed/predicted streamflow values/statistics (mean, median,
    ///       quantile), or on time indices. If provided in combination with
    ///       *t_msk*, the latter takes precedence. If not provided and neither
    ///       is *t_msk*, no subset is performed and only one set of metrics is
    ///       returned corresponding to the whole time series.
    ///       shape: (sites, subsets)
    ///
    ///       .. seealso:: :doc:`../../functionalities/conditional-masking`
    ///
    ///    bootstrap: ``std::unordered_map<std::string, int>``, optional
    ///       Parameters for the bootstrapping method used to estimate the
    ///       sampling uncertainty in the evaluation of the predictions.
    ///       The parameters are: 'n_samples' the number of random samples,
    ///       'len_sample' the length of one sample in number of years,
    ///       and 'summary' the statistics to return to characterise the
    ///       sampling distribution). If not provided, no bootstrapping is
    ///       performed. If provided, *dts* must also be provided.
    ///
    ///       .. seealso:: :doc:`../../functionalities/bootstrapping`
    ///
    ///    dts: ``std::vector<std::string>``, optional
    ///       Datetimes. The corresponding date and time for the temporal
    ///       dimension of the streamflow observations and predictions.
    ///       The date and time must be specified in a string following the
    ///       ISO 8601-1:2019 standard, i.e. "YYYY-MM-DD hh:mm:ss" (e.g. the
    ///       21st of May 2007 at 4 in the afternoon is "2007-05-21 16:00:00").
    ///       The time series must feature complete years. Only minute, hourly,
    ///       and daily time steps are supported. If provided, it is only used
    ///       if *bootstrap* is also provided.
    ///
    ///    seed: ``int``, optional
    ///       A value for the seed used by random generators. This parameter
    ///       guarantees the reproducibility of the metric values between calls.
    ///
    ///    diagnostics: ``std::vector<std::string>``, optional
    ///       The sequence of evaluation diagnostics to be computed.
    ///
    ///       .. seealso:: :doc:`../../functionalities/diagnostics`
    ///
    /// :Returns:
    ///
    ///    ``std::vector<xt::xarray<double>>``
    ///       The sequence of evaluation metrics computed in the same order
    ///       as given in *metrics*, followed by the sequence of evaluation
    ///       diagnostics computed in the same order as given in *diagnostics*.
    ///       shape: (metrics+diagnostics,)<(sites, lead times, subsets, samples,
    ///       {quantiles,} {thresholds,} {components,} {ranks,} {intervals})>
    ///
    /// :Examples:
    ///
    ///    .. code-block:: c++
    ///    
    ///       #include <xtensor/xtensor.hpp>
    ///       #include <evalhyd/evalp.hpp>
    ///    
    ///       xt::xtensor<double, 2> obs = {{ 4.7, 4.3, 5.5, 2.7, 4.1 }};
    ///       xt::xtensor<double, 4> prd = {{{{ 5.3, 4.2, 5.7, 2.3, 3.1 },
    ///                                       { 4.3, 4.2, 4.7, 4.3, 3.3 },
    ///                                       { 5.3, 5.2, 5.7, 2.3, 3.9 }}}};
    ///       xt::xtensor<double, 2> thr = {{ 4.7, 4.3, 5.5, 2.7, 4.1 }};
    ///    
    ///       evalhyd::evalp(obs, prd, {"BS"}, thr);
    ///
    ///    .. code-block:: c++
    ///
    ///       xt::xtensor<bool, 3> msk = {{{ false, true, true, false, true }}};
    ///
    ///       evalhyd::evalp(obs, prd, {"BS"}, thr, msk);
    ///
    ///    .. code-block:: c++
    ///
    ///       evalhyd::evalp(obs, prd, {"CRPS_FROM_QS"});
    ///
    /// \endrst
    template <class XD2, class XD4, class XB4 = xt::xtensor<bool, 4>,
              class XS2 = xt::xtensor<std::array<char, 32>, 2>>
    std::vector<xt::xarray<double>> evalp(
            const xt::xexpression<XD2>& q_obs,
            const xt::xexpression<XD4>& q_prd,
            const std::vector<std::string>& metrics,
            const xt::xexpression<XD2>& q_thr = XD2({}),
            xtl::xoptional<const std::string, bool> events =
                    xtl::missing<const std::string>(),
            const std::vector<double>& c_lvl = {},
            const xt::xexpression<XB4>& t_msk = XB4({}),
            const xt::xexpression<XS2>& m_cdt = XS2({}),
            xtl::xoptional<const std::unordered_map<std::string, int>, bool> bootstrap =
                    xtl::missing<const std::unordered_map<std::string, int>>(),
            const std::vector<std::string>& dts = {},
            xtl::xoptional<const int, bool> seed =
                    xtl::missing<const int>(),
            xtl::xoptional<const std::vector<std::string>, bool> diagnostics =
                    xtl::missing<const std::vector<std::string>>()
    )
    {
        // check ranks of expressions if they are tensors
        if (xt::get_rank<XD2>::value != SIZE_MAX)
        {
            if (xt::get_rank<XD2>::value != 2)
            {
                throw std::runtime_error(
                        "observations and/or thresholds are not two-dimensional"
                );
            }
        }

        if (xt::get_rank<XD4>::value != SIZE_MAX)
        {
            if (xt::get_rank<XD4>::value != 4)
            {
                throw std::runtime_error(
                        "predictions are not four-dimensional"
                );
            }
        }

        if (xt::get_rank<XB4>::value != SIZE_MAX)
        {
            if (xt::get_rank<XB4>::value != 4)
            {
                throw std::runtime_error(
                        "temporal masks are not four-dimensional"
                );
            }
        }

        // retrieve real types of the expressions
        const XD2& q_obs_ = q_obs.derived_cast();
        const XD4& q_prd_ = q_prd.derived_cast();
        const XD2& q_thr_ = q_thr.derived_cast();

        const XB4& t_msk_ = t_msk.derived_cast();
        const XS2& m_cdt_ = m_cdt.derived_cast();

        // adapt vector to tensor
        const xt::xtensor<double, 1> c_lvl_ = xt::adapt(c_lvl);

        // check that the metrics/diagnostics to be computed are valid
        utils::check_metrics(
                metrics,
                {"BS", "BSS", "BS_CRD", "BS_LBD", "REL_DIAG", "CRPS_FROM_BS",
                 "CRPS_FROM_ECDF",
                 "QS", "CRPS_FROM_QS",
                 "CONT_TBL", "POD", "POFD", "FAR", "CSI", "ROCSS",
                 "RANK_HIST", "DS", "AS",
                 "CR", "AW", "AWN", "WS",
                 "ES"}
        );

        if ( diagnostics.has_value() )
        {
            utils::check_diags(
                    diagnostics.value(),
                    {"completeness"}
            );
        }

        // check optional parameters
        if (bootstrap.has_value())
        {
            utils::check_bootstrap(bootstrap.value());
        }

        // get a seed for random generators
        auto random_seed = utils::get_seed(seed);

        // check that data dimensions are compatible
        // > time
        if (q_obs_.shape(1) != q_prd_.shape(3))
        {
            throw std::runtime_error(
                    "observations and predictions feature different "
                    "temporal lengths"
            );
        }
        if (t_msk_.size() > 0)
        {
            if (q_obs_.shape(1) != t_msk_.shape(3))
            {
                throw std::runtime_error(
                        "observations and masks feature different "
                        "temporal lengths"
                );
            }
        }
        if (!dts.empty())
        {
            if (q_obs_.shape(1) != dts.size())
            {
                throw std::runtime_error(
                        "observations and datetimes feature different "
                        "temporal lengths"
                );
            }
        }

        // > leadtimes
        if (t_msk_.size() > 0)
        {
            if (q_prd_.shape(1) != t_msk_.shape(1))
            {
                throw std::runtime_error(
                        "predictions and temporal masks feature different "
                        "numbers of lead times"
                );
            }
        }

        // > sites
        if (q_obs_.shape(0) != q_prd_.shape(0))
        {
            throw std::runtime_error(
                    "observations and predictions feature different "
                    "numbers of sites"
            );
        }

        if (q_thr_.size() > 0)
        {
            if (q_obs_.shape(0) != q_thr_.shape(0))
            {
                throw std::runtime_error(
                        "observations and thresholds feature different "
                        "numbers of sites"
                );
            }
        }

        if (t_msk_.size() > 0)
        {
            if (q_obs_.shape(0) != t_msk_.shape(0))
            {
                throw std::runtime_error(
                        "observations and temporal masks feature different "
                        "numbers of sites"
                );
            }
        }

        if (m_cdt_.size() > 0)
        {
            if (q_obs_.shape(0) != m_cdt_.shape(0))
            {
                throw std::runtime_error(
                        "observations and masking conditions feature different "
                        "numbers of sites"
                );
            }
        }

        // retrieve dimensions
        std::size_t n_tim = q_prd_.shape(3);

        // generate masks from conditions if provided
        auto gen_msk = [&]()
        {
            if ((t_msk_.size() < 1) && (m_cdt_.size() > 0))
            {
                std::size_t n_sit = q_prd_.shape(0);
                std::size_t n_ltm = q_prd_.shape(1);
                std::size_t n_msk = m_cdt_.shape(1);

                XB4 c_msk = xt::zeros<bool>({n_sit, n_ltm, n_msk, n_tim});

                for (std::size_t s = 0; s < n_sit; s++)
                {
                    for (std::size_t l = 0; l < n_ltm; l++)
                    {
                        for (std::size_t m = 0; m < n_msk; m++)
                        {
                            xt::view(c_msk, s, l, m) =
                                    masks::generate_mask_from_conditions(
                                            xt::view(m_cdt_, s, m),
                                            xt::view(q_obs_, s),
                                            xt::view(q_prd_, s, l)
                                    );
                        }
                    }
                }

                return c_msk;
            }
            else
            {
                return XB4(xt::zeros<bool>({0, 0, 0, 0}));
            }
        };
        const XB4 c_msk = gen_msk();

        // generate bootstrap experiment if requested
        std::vector<xt::xkeep_slice<int>> b_exp;
        int summary;

        if (bootstrap.has_value())
        {
            auto n_samples = bootstrap.value().find("n_samples")->second;
            auto len_sample = bootstrap.value().find("len_sample")->second;
            summary = bootstrap.value().find("summary")->second;

            if (dts.empty())
            {
                throw std::runtime_error(
                        "bootstrap requested but datetimes not provided"
                );
            }

            b_exp = uncertainty::bootstrap(
                    dts, n_samples, len_sample, random_seed
            );
        }
        else
        {
            // if no bootstrap requested, generate one sample
            // containing all the time indices once
            summary = 0;
            xt::xtensor<int, 1> all = xt::arange(n_tim);
            b_exp.push_back(xt::keep(all));
        }

        // instantiate determinist evaluator
        probabilist::Evaluator<XD2, XD4, XB4> evaluator(
                q_obs_, q_prd_, q_thr_, c_lvl_, events,
                t_msk_.size() > 0 ? t_msk_: (m_cdt_.size() > 0 ? c_msk : t_msk_),
                b_exp,
                random_seed
        );

        // initialise data structure for outputs
        std::vector<xt::xarray<double>> r;

        for ( const auto& metric : metrics )
        {
            if ( metric == "BS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_BS(), summary)
                );
            }
            else if ( metric == "BSS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_BSS(), summary)
                );
            }
            else if ( metric == "BS_CRD" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_BS_CRD(), summary)
                );
            }
            else if ( metric == "BS_LBD" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_BS_LBD(), summary)
                );
            }
            else if ( metric == "REL_DIAG" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_REL_DIAG(), summary)
                );
            }
            else if ( metric == "CRPS_FROM_BS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CRPS_FROM_BS(), summary)
                );
            }
            else if ( metric == "CRPS_FROM_ECDF" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CRPS_FROM_ECDF(), summary)
                );
            }
            else if ( metric == "QS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_QS(), summary)
                );
            }
            else if ( metric == "CRPS_FROM_QS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CRPS_FROM_QS(), summary)
                );
            }
            else if ( metric == "CONT_TBL" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CONT_TBL(), summary)
                );
            }
            else if ( metric == "POD" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_POD(), summary)
                );
            }
            else if ( metric == "POFD" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_POFD(), summary)
                );
            }
            else if ( metric == "FAR" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_FAR(), summary)
                );
            }
            else if ( metric == "CSI" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CSI(), summary)
                );
            }
            else if ( metric == "ROCSS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_ROCSS(), summary)
                );
            }
            else if ( metric == "RANK_HIST" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_RANK_HIST(), summary)
                );
            }
            else if ( metric == "DS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_DS(), summary)
                );
            }
            else if ( metric == "AS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_AS(), summary)
                );
            }
            else if ( metric == "CR" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_CR(), summary)
                );
            }
            else if ( metric == "AW" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_AW(), summary)
                );
            }
            else if ( metric == "AWN" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_AWN(), summary)
                );
            }
            else if ( metric == "WS" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_WS(), summary)
                );
            }
            else if ( metric == "ES" )
            {
                r.emplace_back(
                        uncertainty::summarise_p(evaluator.get_ES(), summary)
                );
            }
        }

        if ( diagnostics.has_value() )
        {
            for ( const auto& diagnostic : diagnostics.value() )
            {
                if ( diagnostic == "completeness" )
                {
                    r.emplace_back(
                            evaluator.get_completeness()
                    );
                }
            }
        }

        return r;
    }
}

#endif //EVALHYD_EVALP_HPP
