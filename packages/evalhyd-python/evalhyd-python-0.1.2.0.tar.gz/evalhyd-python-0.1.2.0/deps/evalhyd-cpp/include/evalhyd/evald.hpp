// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_EVALD_HPP
#define EVALHYD_EVALD_HPP

#include <unordered_map>
#include <vector>

#include <xtl/xoptional.hpp>
#include <xtensor/xexpression.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xarray.hpp>

#include "detail/utils.hpp"
#include "detail/masks.hpp"
#include "detail/uncertainty.hpp"
#include "detail/determinist/evaluator.hpp"


namespace evalhyd
{
    /// Function to evaluate deterministic streamflow predictions.
    ///
    /// \rst
    ///
    /// :Template Parameters:
    ///
    ///    XD2: Any 2-dimensional container class storing numeric elements
    ///         (e.g. ``xt::xtensor<double, 2>``, ``xt::pytensor<double, 2>``,
    ///         ``xt::rtensor<double, 2>``, etc.).
    ///
    ///    XB3: Any 3-dimensional container class storing boolean elements
    ///         (e.g. ``xt::xtensor<bool, 3>``, ``xt::pytensor<bool, 3>``,
    ///         ``xt::rtensor<bool, 3>``, etc.).
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
    ///       shape: (1, time)
    ///
    ///    q_prd: ``XD2``
    ///       Streamflow predictions. Time steps with missing predictions
    ///       must be assigned `NAN` values. Those time steps will be ignored
    ///       both in the observations and the predictions before the
    ///       *metrics* are computed.
    ///       shape: (series, time)
    ///
    ///    metrics: ``std::vector<std::string>``
    ///       The sequence of evaluation metrics to be computed.
    ///
    ///       .. seealso:: :doc:`../../metrics/deterministic`
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
    ///    transform: ``std::string``, optional
    ///       The transformation to apply to both streamflow observations and
    ///       predictions prior to the calculation of the *metrics*.
    ///
    ///       .. seealso:: :doc:`../../functionalities/transformation`
    ///
    ///    exponent: ``double``, optional
    ///       The value of the exponent n to use when the *transform* is the
    ///       power function. If not provided, the streamflow observations
    ///       and predictions remain untransformed.
    ///
    ///    epsilon: ``double``, optional
    ///       The value of the small constant ε to add to both the streamflow
    ///       observations and predictions prior to the calculation of the
    ///       *metrics* when the *transform* is the reciprocal function, the
    ///       natural logarithm, or the power function with a negative exponent
    ///       (since none are defined for 0). If not provided, one hundredth of
    ///       the mean of the streamflow observations is used as value for
    ///       epsilon, as recommended by `Pushpalatha et al. (2012)
    ///       <https://doi.org/10.1016/j.jhydrol.2011.11.055>`_.
    ///
    ///    t_msk: ``XB3``, optional
    ///       Mask used to temporally subset of the whole streamflow time series
    ///       (where True/False is used for the time steps to include/discard in
    ///       the subset).
    ///       shape: (series, subsets, time)
    ///
    ///       .. seealso:: :doc:`../../functionalities/temporal-masking`
    ///
    ///    m_cdt: ``XS2``, optional
    ///       Masking conditions to use to generate temporal subsets. Each
    ///       condition consists in a string and can be specified on observed
    ///       streamflow values/statistics (mean, median, quantile), or on time
    ///       indices. If provided in combination with *t_msk*, the latter takes
    ///       precedence. If not provided and neither is *t_msk*, no subset is
    ///       performed.
    ///       shape: (series, subsets)
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
    ///       shape: (metrics+diagnostics,)<(series, subsets, samples, {components})>
    ///
    /// :Examples:
    ///    
    ///    .. code-block:: c++
    ///       
    ///       #include <xtensor/xtensor.hpp>
    ///       #include <evalhyd/evald.hpp>
    ///    
    ///       xt::xtensor<double, 2> obs = {{ 4.7, 4.3, 5.5, 2.7, 4.1 }};
    ///       xt::xtensor<double, 2> prd = {{ 5.3, 4.2, 5.7, 2.3, 3.1 },
    ///                                     { 4.3, 4.2, 4.7, 4.3, 3.3 },
    ///                                     { 5.3, 5.2, 5.7, 2.3, 3.9 }};
    ///
    ///       evalhyd::evald(obs, prd, {"NSE"});
    ///
    ///    .. code-block:: c++
    ///
    ///       evalhyd::evald(obs, prd, {"NSE"}, "sqrt");
    ///
    ///    .. code-block:: c++
    ///
    ///       evalhyd::evald(obs, prd, {"NSE"}, "pow", 0.2);
    ///
    ///    .. code-block:: c++
    ///
    ///       evalhyd::evald(obs, prd, {"NSE"}, "log", 1, 0.05);
    ///
    ///    .. code-block:: c++
    ///
    ///       xt::xtensor<double, 3> msk = {{{ 1, 1, 0, 1, 0 }}};
    ///
    ///       evalhyd::evald(obs, prd, {"NSE"}, "none", 1, -9, msk);
    ///
    /// \endrst
    template <class XD2, class XB3 = xt::xtensor<bool, 3>,
              class XS2 = xt::xtensor<std::array<char, 32>, 2>>
    std::vector<xt::xarray<double>> evald(
            const xt::xexpression<XD2>& q_obs,
            const xt::xexpression<XD2>& q_prd,
            const std::vector<std::string>& metrics,
            const xt::xexpression<XD2>& q_thr = XD2({}),
            xtl::xoptional<const std::string, bool> events =
                    xtl::missing<const std::string>(),
            xtl::xoptional<const std::string, bool> transform =
                    xtl::missing<const std::string>(),
            xtl::xoptional<double, bool> exponent =
                    xtl::missing<double>(),
            xtl::xoptional<double, bool> epsilon =
                    xtl::missing<double>(),
            const xt::xexpression<XB3>& t_msk = XB3({}),
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
                        "observations and/or predictions and/or thresholds "
                        "are not two-dimensional"
                );
            }
        }
        if (xt::get_rank<XB3>::value != SIZE_MAX)
        {
            if (xt::get_rank<XB3>::value != 3)
            {
                throw std::runtime_error(
                        "temporal masks are not three-dimensional"
                );
            }
        }

        // retrieve real types of the expressions
        const XD2& q_obs_ = q_obs.derived_cast();
        const XD2& q_prd_ = q_prd.derived_cast();
        const XD2& q_thr_ = q_thr.derived_cast();

        const XB3& t_msk_ = t_msk.derived_cast();
        const XS2& m_cdt_ = m_cdt.derived_cast();

        // check that the metrics/diagnostics to be computed are valid
        utils::check_metrics(
                metrics,
                {"MAE", "MARE", "MSE", "RMSE",
                 "NSE", "KGE", "KGE_D", "KGEPRIME", "KGEPRIME_D",
                 "KGENP", "KGENP_D",
                 "CONT_TBL"}
        );

        if ( diagnostics.has_value() )
        {
            utils::check_diags(
                    diagnostics.value(),
                    {"completeness"}
            );
        }

        // check that optional parameters are valid
        if (bootstrap.has_value())
        {
            utils::check_bootstrap(bootstrap.value());
        }

        // get a seed for random generators
        auto random_seed = utils::get_seed(seed);

        // check that data dimensions are compatible
        // > time
        if (q_obs_.shape(1) != q_prd_.shape(1))
        {
            throw std::runtime_error(
                    "observations and predictions feature different "
                    "temporal lengths"
            );
        }
        if (t_msk_.size() > 0)
        {
            if (q_obs_.shape(1) != t_msk_.shape(2))
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

        // > series
        if (q_obs_.shape(0) != 1)
        {
            throw std::runtime_error(
                    "observations contain more than one time series"
            );
        }

        if (q_thr_.size() > 0)
        {
            if (q_prd_.shape(0) != q_thr_.shape(0))
            {
                throw std::runtime_error(
                        "predictions and thresholds feature different "
                        "numbers of series"
                );
            }
        }

        if (t_msk_.size() > 0)
        {
            if (q_prd_.shape(0) != t_msk_.shape(0))
            {
                throw std::runtime_error(
                        "predictions and masks feature different "
                        "number of series"
                );
            }
        }

        if (m_cdt_.size() > 0)
        {
            if (q_prd_.shape(0) != m_cdt_.shape(0))
            {
                throw std::runtime_error(
                        "predictions and masking conditions feature different "
                        "numbers of series"
                );
            }
        }

        // retrieve dimensions
        std::size_t n_tim = q_prd_.shape(1);

        // generate masks from conditions if provided
        auto gen_msk = [&]()
        {
            if ((t_msk_.size() < 1) && (m_cdt_.size() > 0))
            {
                std::size_t n_srs = q_prd_.shape(0);
                std::size_t n_msk = m_cdt_.shape(1);

                XB3 c_msk = xt::zeros<bool>({n_srs, n_msk, n_tim});

                for (std::size_t s = 0; s < n_srs; s++)
                {
                    for (std::size_t m = 0; m < n_msk; m++)
                    {
                        xt::view(c_msk, s, m) =
                                masks::generate_mask_from_conditions(
                                        xt::view(m_cdt_, s, m),
                                        xt::view(q_obs_, 0),
                                        xt::view(q_prd_, s, xt::newaxis())
                                );
                    }
                }

                return c_msk;
            }
            else
            {
                return XB3(xt::zeros<bool>({0, 0, 0}));
            }
        };
        const XB3 c_msk = gen_msk();

        // apply streamflow transformation if requested
        auto q_transform = [&](const XD2& q)
        {
            if (transform.has_value())
            {
                if ( transform.value() == "sqrt" )
                {
                    return XD2(xt::sqrt(q));
                }
                else if ( transform.value() == "inv" )
                {
                    if ( !epsilon.has_value() )
                    {
                        // determine an epsilon value to avoid zero divide
                        epsilon = xt::nanmean(q_obs_)() * 0.01;
                    }

                    return XD2(1. / (q + epsilon.value()));
                }
                else if ( transform.value() == "log" )
                {
                    if ( !epsilon.has_value() )
                    {
                        // determine an epsilon value to avoid log zero
                        epsilon = xt::nanmean(q_obs_)() * 0.01;
                    }

                    return XD2(xt::log(q + epsilon.value()));
                }
                else if ( transform.value() == "pow" )
                {
                    if ( exponent.has_value() )
                    {
                        if ( exponent.value() == 1)
                        {
                            return q;
                        }
                        else if ( exponent.value() < 0 )
                        {
                            if ( !epsilon.has_value() )
                            {
                                // determine an epsilon value to avoid zero divide
                                epsilon = xt::nanmean(q_obs_)() * 0.01;
                            }

                            return XD2(xt::pow(q + epsilon.value(),
                                               exponent.value()));
                        }
                        else
                        {
                            return XD2(xt::pow(q, exponent.value()));
                        }
                    }
                    else
                    {
                        throw std::runtime_error(
                                "missing exponent for power transformation"
                        );
                    }
                }
                else
                {
                    throw std::runtime_error(
                            "invalid streamflow transformation: "
                            + transform.value()
                    );
                }
            }
            else
            {
                return q;
            }
        };

        const XD2& obs = q_transform(q_obs_);
        const XD2& prd = q_transform(q_prd_);
        const XD2& thr = q_transform(q_thr_);

        // generate bootstrap experiment if requested
        std::vector<xt::xkeep_slice<int>> exp;
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

            exp = uncertainty::bootstrap(
                    dts, n_samples, len_sample, random_seed
            );
        }
        else
        {
            // if no bootstrap requested, generate one sample
            // containing all the time indices once
            summary = 0;
            xt::xtensor<int, 1> all = xt::arange(n_tim);
            exp.push_back(xt::keep(all));
        }

        // instantiate determinist evaluator
        determinist::Evaluator<XD2, XB3> evaluator(
                obs, prd, thr, events,
                t_msk_.size() > 0 ? t_msk_: (m_cdt_.size() > 0 ? c_msk : t_msk_),
                exp
        );

        // retrieve or compute requested metrics
        std::vector<xt::xarray<double>> r;

        for ( const auto& metric : metrics )
        {
            if ( metric == "MAE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_MAE(), summary)
                );
            }
            if ( metric == "MARE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_MARE(), summary)
                );
            }
            if ( metric == "MSE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_MSE(), summary)
                );
            }
            if ( metric == "RMSE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_RMSE(), summary)
                );
            }
            else if ( metric == "NSE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_NSE(), summary)
                );
            }
            else if ( metric == "KGE" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGE(), summary)
                );
            }
            else if ( metric == "KGE_D" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGE_D(), summary)
                );
            }
            else if ( metric == "KGEPRIME" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGEPRIME(), summary)
                );
            }
            else if ( metric == "KGEPRIME_D" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGEPRIME_D(), summary)
                );
            }
            else if ( metric == "KGENP" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGENP(), summary)
                );
            }
            else if ( metric == "KGENP_D" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_KGENP_D(), summary)
                );
            }
            else if ( metric == "CONT_TBL" )
            {
                r.emplace_back(
                        uncertainty::summarise_d(evaluator.get_CONT_TBL(), summary)
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
    };
}

#endif //EVALHYD_EVALD_HPP
