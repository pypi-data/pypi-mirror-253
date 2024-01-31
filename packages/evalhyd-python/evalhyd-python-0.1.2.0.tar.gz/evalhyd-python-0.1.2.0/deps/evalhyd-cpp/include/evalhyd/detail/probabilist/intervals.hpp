// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_INTERVALS_HPP
#define EVALHYD_PROBABILIST_INTERVALS_HPP

#include <limits>

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xindex_view.hpp>
#include <xtensor/xsort.hpp>


namespace evalhyd
{
    namespace probabilist
    {
        namespace elements
        {
            /// Compute the bounds of the predictive intervals by computing
            /// the quantiles of the predictive distribution corresponding
            /// to the confidence intervals.
            ///
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (sites, lead times, members, time)
            /// \param c_lvl
            ///     Confidence levels for the predictive intervals.
            ///     shape: (intervals,)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_itv
            ///     Number of predictive intervals.
            /// \param n_tim
            ///     Number of time steps.
            /// \return
            ///     Bounds of the predictive intervals.
            ///     shape: (sites, lead times, intervals, bounds, time)
            template <class XD4>
            inline xt::xtensor<double, 5> calc_itv_bnds(
                    const XD4& q_prd,
                    const xt::xtensor<double, 1>& c_lvl,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_itv,
                    std::size_t n_tim
            )
            {
                xt::xtensor<double, 5> itv_bnds =
                        xt::zeros<double>({n_sit, n_ldt, n_itv, std::size_t {2}, n_tim});

                // determine quantiles forming the predictive intervals
                // from the confidence levels
                xt::xtensor<double, 2> quantiles =
                        xt::zeros<double>({n_itv, std::size_t {2}});
                xt::col(quantiles, 0) = 0.5 - c_lvl / 200.;
                xt::col(quantiles, 1) = 0.5 + c_lvl / 200.;

                // compute predictive interval bounds from quantiles
                for (std::size_t i = 0; i < n_itv; i++)
                {
                    auto q =  xt::quantile(q_prd, xt::view(quantiles, i), 2);

                    xt::view(itv_bnds, xt::all(), xt::all(), i, 0, xt::all()) =
                            xt::view(q, 0);
                    xt::view(itv_bnds, xt::all(), xt::all(), i, 1, xt::all()) =
                            xt::view(q, 1);
                }

                return itv_bnds;
            }

            /// Determine whether the observations are inside the predictive
            /// intervals for each time step.
            ///
            /// \param q_obs
            ///     Streamflow predictions.
            ///     shape: (sites, time)
            /// \param itv_bnds
            ///     Bounds of the predictive intervals.
            ///     shape: (sites, lead times, intervals, bounds, time)
            /// \return
            ///     Boolean-like tensor evaluating to true where observations
            ///     are inside the predictive intervals.
            ///     shape: (sites, lead times, intervals, time)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_obs_in_itv(
                    const XD2& q_obs,
                    const xt::xtensor<double, 5>& itv_bnds
            )
            {
                // notations below follow Gneiting and Raftery (2007), sect 6.2
                // https://doi.org/10.1198/016214506000001437

                auto x = xt::view(q_obs, xt::all(), xt::newaxis(), xt::newaxis(), xt::all());
                auto l = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 0, xt::all());
                auto u = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 1, xt::all());

                return ((x >= l) && (x <= u));
            }

            /// Compute the width of the predictive intervals for each time step.
            ///
            /// \param itv_bnds
            ///     Bounds of the predictive intervals.
            ///     shape: (sites, lead times, intervals, bounds, time)
            /// \return
            ///     Interval scores for each time step.
            ///     shape: (sites, lead times, intervals, time)
            inline xt::xtensor<double, 4> calc_itv_width(
                    const xt::xtensor<double, 5>& itv_bnds
            )
            {
                // notations below follow Gneiting and Raftery (2007), sect 6.2
                // https://doi.org/10.1198/016214506000001437

                auto l = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 0, xt::all());
                auto u = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 1, xt::all());

                return (u - l);
            }
        }

        namespace intermediate
        {
            /// Compute the Winkler score for each time step.
            ///
            /// \param q_obs
            ///     Streamflow predictions.
            ///     shape: (sites, time)
            /// \param c_lvl
            ///     Confidence levels for the predictive intervals.
            ///     shape: (intervals,)
            /// \param itv_bnds
            ///     Bounds of the predictive intervals.
            ///     shape: (sites, lead times, intervals, bounds, time)
            /// \return
            ///     Interval scores for each time step.
            ///     shape: (sites, lead times, intervals, time)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_ws(
                    const XD2& q_obs,
                    const xt::xtensor<double, 1>& c_lvl,
                    const xt::xtensor<double, 5>& itv_bnds
            )
            {
                // notations below follow Gneiting and Raftery (2007), sect 6.2
                // https://doi.org/10.1198/016214506000001437

                auto x = xt::view(q_obs, xt::all(), xt::newaxis(), xt::newaxis(), xt::all());
                auto alpha = 1 - xt::view(c_lvl, xt::all(), xt::newaxis()) / 100.;

                // compute component corresponding to observations below interval
                auto l = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 0, xt::all());
                // (l - x)𝟙{x < l}
                auto ws_l = xt::where(x < l, l - x, 0.);

                // compute component corresponding to observations above interval
                auto u = xt::view(itv_bnds, xt::all(), xt::all(), xt::all(), 1, xt::all());
                // (x - u)𝟙{x > u}
                auto ws_u = xt::where(x > u, x - u, 0.);

                // compute interval score
                auto ws = (u - l) + 2. * (ws_l + ws_u) / alpha;

                return ws;
            }
        }

        namespace metrics
        {
            namespace detail {
                inline xt::xtensor<double, 5> calc_METRIC_from_metric(
                        const xt::xtensor<double, 4>& metric,
                        const xt::xtensor<bool, 4>& t_msk,
                        const std::vector<xt::xkeep_slice<int>>& b_exp,
                        std::size_t n_sit,
                        std::size_t n_ldt,
                        std::size_t n_itv,
                        std::size_t n_msk,
                        std::size_t n_exp
                )
                {
                    // initialise output variable
                    xt::xtensor<double, 5> METRIC =
                            xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_itv});

                    // compute variable one mask at a time to minimise memory imprint
                    for (std::size_t m = 0; m < n_msk; m++)
                    {
                        // apply the mask
                        // (using NaN workaround until reducers work on masked_view)
                        auto metric_masked = xt::where(
                                xt::view(t_msk, xt::all(), xt::all(), m,
                                         xt::newaxis(), xt::all()),
                                metric,
                                NAN
                        );

                        // compute variable one sample at a time
                        for (std::size_t e = 0; e < n_exp; e++)
                        {
                            // apply the bootstrap sampling
                            auto metric_masked_sampled =
                                    xt::view(metric_masked, xt::all(),
                                             xt::all(), xt::all(), b_exp[e]);

                            // calculate the mean over the time steps
                            xt::view(METRIC, xt::all(), xt::all(), m, e, xt::all()) =
                                    xt::nanmean(metric_masked_sampled, -1);
                        }
                    }

                    return METRIC;
                }
            }

            /// Compute the Coverage Ratio (CR), i.e. the portion of
            /// observations falling within the predictive intervals.
            /// It is a measure of the reliability of the predictions.
            ///
            /// \param obs_in_itv
            ///     Boolean-like tensor evaluating to true where observations
            ///     are inside the predictive intervals.
            ///     shape: (sites, lead times, intervals, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_itv
            ///     Number of predictive intervals.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Coverage ratios.
            ///     shape: (sites, lead times, subsets, samples, intervals)
            inline xt::xtensor<double, 5> calc_CR(
                    const xt::xtensor<double, 4>& obs_in_itv,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_itv,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        obs_in_itv, t_msk, b_exp,
                        n_sit, n_ldt, n_itv, n_msk, n_exp
                );
            }

            /// Compute the Average Width (AW) of the predictive intervals.
            /// It is a measure of the sharpness of the predictions.
            ///
            /// \param itv_width
            ///     Widths of predictive intervals for each time step.
            ///     shape: (sites, lead times, intervals, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_itv
            ///     Number of predictive intervals.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Average widths.
            ///     shape: (sites, lead times, subsets, samples, intervals)
            inline xt::xtensor<double, 5> calc_AW(
                    const xt::xtensor<double, 4>& itv_width,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_itv,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        itv_width, t_msk, b_exp, n_sit, n_ldt, n_itv, n_msk, n_exp
                );
            }

            /// Compute the Average Width Normalised (AWN).
            ///
            /// \param q_obs
            ///     Streamflow predictions.
            ///     shape: (sites, time)
            /// \param AW
            ///     Average widths.
            ///     shape: (sites, lead times, subsets, samples, intervals)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Average widths normalised with mean observations.
            ///     shape: (sites, lead times, subsets, samples, intervals)
            template <class XD2>
            inline xt::xtensor<double, 5> calc_AWN(
                    const XD2& q_obs,
                    const xt::xtensor<double, 5>& AW,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // compute "climatology" average width
                xt::xtensor<double, 5> mean_obs =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp,
                                           std::size_t {1}});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++) {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto q_obs_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            xt::view(q_obs, xt::all(), xt::newaxis(), xt::all()),
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto q_obs_masked_sampled =
                                xt::view(q_obs_masked, xt::all(), xt::all(), b_exp[e]);

                        // compute mean observation
                        xt::view(mean_obs, xt::all(), xt::all(), m, e, 0) =
                                xt::nanmean(q_obs_masked_sampled, -1);
                    }
                }

                return xt::where(mean_obs > 0,
                                 AW / mean_obs,
                                 - std::numeric_limits<double>::infinity());
            }

            /// Compute the Winkler scores (WS), also known as interval score.
            ///
            /// \param ws
            ///     Winkler scores for each time step.
            ///     shape: (sites, lead times, intervals, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_itv
            ///     Number of predictive intervals.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Winkler scores.
            ///     shape: (sites, lead times, subsets, samples, intervals)
            inline xt::xtensor<double, 5> calc_WS(
                    const xt::xtensor<double, 4>& ws,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_itv,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        ws, t_msk, b_exp, n_sit, n_ldt, n_itv, n_msk, n_exp
                );
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_INTERVALS_HPP
