// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_CONTINGENCY_HPP
#define EVALHYD_PROBABILIST_CONTINGENCY_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmasked_view.hpp>
#include <xtensor/xmath.hpp>


// NOTE ------------------------------------------------------------------------
// All equations in metrics below are following notations from
// "Wilks, D. S. (2011). Statistical methods in the atmospheric sciences.
// Amsterdam; Boston: Elsevier Academic Press. ISBN: 9780123850225".
// In particular, pp. 302-303, 332-333.
// -----------------------------------------------------------------------------

namespace evalhyd
{
    namespace probabilist
    {
        namespace elements
        {
            // Contingency table:
            //
            //                  OBS
            //                Y     N
            //             +-----+-----+      a: hits
            //           Y |  a  |  b  |      b: false alarms
            //     PRD     +-----+-----+      c: misses
            //           N |  c  |  d  |      d: correct rejections
            //             +-----+-----+
            //

            /// Determine alerts based on forecast.
            ///
            /// \param sum_f_k
            ///     Number of forecast members exceeding threshold(s).
            ///     shape: (sites, lead times, thresholds, time)
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \return
            ///     Alerts based on forecast.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_a_k(
                    const xt::xtensor<double, 4>& sum_f_k,
                    std::size_t n_mbr
            )
            {
                // compute range of alert levels $alert_lvl$
                // (i.e. number of members that must forecast event
                //  for alert to be raised)
                auto alert_lvl = xt::arange<double>(double(n_mbr + 1));

                // determine whether forecast yield alert
                return xt::view(sum_f_k, xt::all(), xt::all(), xt::newaxis(),
                                xt::all(), xt::all())
                       >= xt::view(alert_lvl, xt::newaxis(), xt::newaxis(),
                                   xt::all(), xt::newaxis(), xt::newaxis());
            }

            /// Determine hits ('a' in contingency table).
            ///
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param a_k
            ///     Alerts based on forecast.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Hits.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_ct_a(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 5>& a_k
            )
            {
                return xt::equal(xt::view(o_k, xt::all(), xt::newaxis(),
                                          xt::newaxis(), xt::all(), xt::all()),
                                 1.)
                       && xt::equal(a_k, 1.);
            }

            /// Determine false alarms ('b' in contingency table).
            ///
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param a_k
            ///     Alerts based on forecast.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     False alarms.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_ct_b(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 5>& a_k
            )
            {
                return xt::equal(xt::view(o_k, xt::all(), xt::newaxis(),
                                          xt::newaxis(), xt::all(), xt::all()),
                                 0.)
                       && xt::equal(a_k, 1.);
            }

            /// Determine misses ('c' in contingency table).
            ///
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param a_k
            ///     Alerts based on forecast.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Misses.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_ct_c(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 5>& a_k
            )
            {
                return xt::equal(xt::view(o_k, xt::all(), xt::newaxis(),
                                          xt::newaxis(), xt::all(), xt::all()),
                                 1.)
                       && xt::equal(a_k, 0.);
            }

            /// Determine correct rejections ('d' in contingency table).
            ///
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param a_k
            ///     Alerts based on forecast.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Correct rejections.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_ct_d(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 5>& a_k
            )
            {
                return xt::equal(xt::view(o_k, xt::all(), xt::newaxis(),
                                          xt::newaxis(), xt::all(), xt::all()),
                                 0.)
                       && xt::equal(a_k, 0.);
            }
        }

        namespace intermediate
        {
            /// Compute the probability of detection for each time step.
            ///
            /// \param ct_a
            ///     Hits.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_c
            ///     Misses.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Probability of detection for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_pod(
                    const xt::xtensor<double, 5>& ct_a,
                    const xt::xtensor<double, 5>& ct_c
            )
            {
                return ct_a / (ct_a + ct_c);
            }

            /// Compute the probability of false detection for each time step.
            ///
            /// \param ct_b
            ///     False alarms.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_d
            ///     Correct rejections.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Probability of false detection for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_pofd(
                    const xt::xtensor<double, 5>& ct_b,
                    const xt::xtensor<double, 5>& ct_d
            )
            {
                return ct_b / (ct_b + ct_d);
            }

            /// Compute the false alarm ratio for each time step.
            ///
            /// \param ct_a
            ///     Hits.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_b
            ///     False alarms.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     False alarm ratio for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_far(
                    const xt::xtensor<double, 5>& ct_a,
                    const xt::xtensor<double, 5>& ct_b
            )
            {
                return ct_b / (ct_a + ct_b);
            }

            /// Compute the critical success index for each time step.
            ///
            /// \param ct_a
            ///     Hits.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_b
            ///     False alarms.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_c
            ///     Misses.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \return
            ///     Critical success index for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            inline xt::xtensor<double, 5> calc_csi(
                    const xt::xtensor<double, 5>& ct_a,
                    const xt::xtensor<double, 5>& ct_b,
                    const xt::xtensor<double, 5>& ct_c
            )
            {
                return ct_a / (ct_a + ct_b + ct_c);
            }
        }

        namespace metrics
        {
            namespace detail
            {
                template <class XD2>
                inline xt::xtensor<double, 6> calc_METRIC_from_metric(
                        const xt::xtensor<double, 5>& metric,
                        const XD2& q_thr,
                        const xt::xtensor<bool, 4>& t_msk,
                        const std::vector<xt::xkeep_slice<int>>& b_exp,
                        std::size_t n_sit,
                        std::size_t n_ldt,
                        std::size_t n_thr,
                        std::size_t n_mbr,
                        std::size_t n_msk,
                        std::size_t n_exp
                )
                {
                    // initialise output variable
                    xt::xtensor<double, 6> METRIC =
                            xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp,
                                               n_mbr + 1, n_thr});

                    // compute variable one mask at a time to minimise memory imprint
                    for (std::size_t m = 0; m < n_msk; m++)
                    {
                        // apply the mask
                        // (using NaN workaround until reducers work on masked_view)
                        auto metric_masked = xt::where(
                                xt::view(t_msk, xt::all(), xt::all(), m,
                                         xt::newaxis(), xt::newaxis(),
                                         xt::all()),
                                metric,
                                NAN
                        );

                        // compute variable one sample at a time
                        for (std::size_t e = 0; e < n_exp; e++)
                        {
                            // apply the bootstrap sampling
                            auto metric_masked_sampled =
                                    xt::view(metric_masked, xt::all(), xt::all(),
                                             xt::all(), xt::all(), b_exp[e]);

                            // calculate the mean over the time steps
                            xt::view(METRIC, xt::all(), xt::all(), m, e,
                                     xt::all(), xt::all()) =
                                    xt::nanmean(metric_masked_sampled, -1);
                        }
                    }

                    // assign NaN where thresholds were not provided (i.e. set as NaN)
                    xt::masked_view(
                            METRIC,
                            xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                               xt::newaxis(), xt::newaxis(),
                                               xt::newaxis(), xt::all()))
                    ) = NAN;

                    return METRIC;
                }
            }

            /// Compute the contingency table (CONT_TBL), i.e. 'hits',
            /// 'false alarms', 'misses', 'correct rejections', in this order.
            ///
            /// \param ct_a
            ///     Hits.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_b
            ///     False alarms.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_c
            ///     Misses.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param ct_d
            ///     Correct rejections.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
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
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Contingency table.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds, cells)
            template <class XD2>
            inline xt::xtensor<double, 7> calc_CONT_TBL(
                    const xt::xtensor<double, 5>& ct_a,
                    const xt::xtensor<double, 5>& ct_b,
                    const xt::xtensor<double, 5>& ct_c,
                    const xt::xtensor<double, 5>& ct_d,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 7> CONT_TBL =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp,
                                           n_mbr + 1, n_thr, std::size_t {4}});

                // compute table one cell at a time
                std::size_t i = 0;
                for (auto cell: {ct_a, ct_b, ct_c, ct_d})
                {
                    xt::view(CONT_TBL, xt::all(), xt::all(), xt::all(),
                             xt::all(), xt::all(), xt::all(), i) =
                        detail::calc_METRIC_from_metric(
                                cell, q_thr, t_msk, b_exp,
                                n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                        );

                    i++;
                }

                return CONT_TBL;
            }

            /// Compute the probability of detection (POD),
            /// also known as 'hit rate'.
            ///
            /// \param pod
            ///     Probability of detection for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
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
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Probabilities of detection.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_POD(
                    const xt::xtensor<double, 5>& pod,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        pod, q_thr, t_msk, b_exp,
                        n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                );
            }

            /// Compute the probability of detection (POFD),
            /// also known as 'false alarm rate'.
            ///
            /// \param pofd
            ///     Probability of false detection for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
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
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Probabilities of false detection.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_POFD(
                    const xt::xtensor<double, 5>& pofd,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        pofd, q_thr, t_msk, b_exp,
                        n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                );
            }

            /// Compute the false alarm ratio (FAR).
            ///
            /// \param far
            ///     False alarm ratio for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
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
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     False alarm ratios.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_FAR(
                    const xt::xtensor<double, 5>& far,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        far, q_thr, t_msk, b_exp,
                        n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                );
            }

            /// Compute the critical success index (CSI).
            ///
            /// \param csi
            ///     Critical success index for each time step.
            ///     shape: (sites, lead times, levels, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
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
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Critical success indices.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_CSI(
                    const xt::xtensor<double, 5>& csi,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                return detail::calc_METRIC_from_metric(
                        csi, q_thr, t_msk, b_exp,
                        n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                );
            }

            /// Compute the relative operating characteristic skill score (ROCSS).
            ///
            /// \param POD
            ///     Probabilities of detection.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            /// \param POFD
            ///     Probabilities of false detection.
            ///     shape: (sites, lead times, subsets, samples, levels, thresholds)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \return
            ///     ROC skill scores.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 5> calc_ROCSS(
                    const xt::xtensor<double, 6>& POD,
                    const xt::xtensor<double, 6>& POFD,
                    const XD2& q_thr
            )
            {
                // compute the area under the ROC curve
                // xt::trapz(y, x, axis=4)
                // (note: taking the opposite of the integration results
                //        because POD/POFD values are in decreasing order)
                auto A = - xt::trapz(POD, POFD, 4);

                // compute the ROC skill score
                // $SS_{ROC} = \frac{A - A_{random}}{A_{perfect} - A_{random}}$
                // $SS_{ROC} = \frac{A - 0.5}{1. - 0.5} = 2A - 1$
                auto ROCSS = xt::eval((2. * A) - 1.);

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        ROCSS,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all()))
                ) = NAN;

                return ROCSS;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_CONTINGENCY_HPP
