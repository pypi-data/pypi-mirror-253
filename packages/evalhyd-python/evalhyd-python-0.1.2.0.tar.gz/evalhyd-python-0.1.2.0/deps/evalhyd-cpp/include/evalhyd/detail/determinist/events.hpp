// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_DETERMINIST_EVENTS_HPP
#define EVALHYD_DETERMINIST_EVENTS_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmasked_view.hpp>
#include <xtensor/xmath.hpp>


namespace evalhyd
{
    namespace determinist
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

            /// Determine observed realisation of threshold(s) exceedance.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (1, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (series, thresholds)
            /// \param is_high_flow_event
            ///     Whether events correspond to being above the threshold(s).
            /// \return
            ///     Event observed outcome.
            ///     shape: (series, thresholds, time)
            template<class XD2>
            inline xt::xtensor<double, 3> calc_obs_event(
                    const XD2& q_obs,
                    const XD2& q_thr,
                    bool is_high_flow_event
            )
            {
                if (is_high_flow_event)
                {
                    // observations above threshold(s)
                    return xt::view(q_obs, xt::all(), xt::newaxis(), xt::all())
                           >= xt::view(q_thr, xt::all(), xt::all(), xt::newaxis());
                }
                else
                {
                    // observations below threshold(s)
                    return xt::view(q_obs, xt::all(), xt::newaxis(), xt::all())
                           <= xt::view(q_thr, xt::all(), xt::all(), xt::newaxis());
                }
            }

            /// Determine predicted realisation of threshold(s) exceedance.
            ///
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (series, thresholds)
            /// \param is_high_flow_event
            ///     Whether events correspond to being above the threshold(s).
            /// \return
            ///     Event predicted outcome.
            ///     shape: (series, thresholds, time)
            template<class XD2>
            inline xt::xtensor<double, 3> calc_prd_event(
                    const XD2& q_prd,
                    const XD2& q_thr,
                    bool is_high_flow_event
            )
            {
                if (is_high_flow_event)
                {
                    // observations above threshold(s)
                    return xt::view(q_prd, xt::all(), xt::newaxis(), xt::all())
                           >= xt::view(q_thr, xt::all(), xt::all(), xt::newaxis());
                }
                else
                {
                    // observations below threshold(s)
                    return xt::view(q_prd, xt::all(), xt::newaxis(), xt::all())
                           <= xt::view(q_thr, xt::all(), xt::all(), xt::newaxis());
                }
            }

            /// Determine hits ('a' in contingency table).
            ///
            /// \param obs_event
            ///     Observed event outcome.
            ///     shape: (series, thresholds, time)
            /// \param prd_event
            ///     Predicted event outcome.
            ///     shape: (series, thresholds, time)
            /// \return
            ///     Hits.
            ///     shape: (series, thresholds, time)
            inline xt::xtensor<double, 3> calc_ct_a(
                    const xt::xtensor<double, 3>& obs_event,
                    const xt::xtensor<double, 3>& prd_event
            )
            {
                return xt::equal(obs_event, 1.) && xt::equal(prd_event, 1.);
            }

            /// Determine false alarms ('b' in contingency table).
            ///
            /// \param obs_event
            ///     Observed event outcome.
            ///     shape: (series, thresholds, time)
            /// \param prd_event
            ///     Predicted event outcome.
            ///     shape: (series, thresholds, time)
            /// \return
            ///     False alarms.
            ///     shape: (series, thresholds, time)
            inline xt::xtensor<double, 3> calc_ct_b(
                    const xt::xtensor<double, 3>& obs_event,
                    const xt::xtensor<double, 3>& prd_event
            )
            {
                return xt::equal(obs_event, 0.) && xt::equal(prd_event, 1.);
            }

            /// Determine misses ('c' in contingency table).
            ///
            /// \param obs_event
            ///     Observed event outcome.
            ///     shape: (series, thresholds, time)
            /// \param prd_event
            ///     Predicted event outcome.
            ///     shape: (series, thresholds, time)
            /// \return
            ///     Misses.
            ///     shape: (series, thresholds, time)
            inline xt::xtensor<double, 3> calc_ct_c(
                    const xt::xtensor<double, 3>& obs_event,
                    const xt::xtensor<double, 3>& prd_event
            )
            {
                return xt::equal(obs_event, 1.) && xt::equal(prd_event, 0.);
            }

            /// Determine correct rejections ('d' in contingency table).
            ///
            /// \param obs_event
            ///     Observed event outcome.
            ///     shape: (series, thresholds, time)
            /// \param prd_event
            ///     Predicted event outcome.
            ///     shape: (series, thresholds, time)
            /// \return
            ///     Correct rejections.
            ///     shape: (series, thresholds, time)
            inline xt::xtensor<double, 3> calc_ct_d(
                    const xt::xtensor<double, 3>& obs_event,
                    const xt::xtensor<double, 3>& prd_event
            )
            {
                return xt::equal(obs_event, 0.) && xt::equal(prd_event, 0.);
            }
        }

        namespace metrics
        {
            /// Compute the cells of the contingency table (CONT_TBL),
            /// i.e. 'hits', 'false alarms', 'misses', 'correct rejections',
            /// in this order.
            ///
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (series, thresholds)
            /// \param ct_a
            ///     Hits for each time step.
            ///     shape: (series, thresholds, time)
            /// \param ct_b
            ///     False alarms for each time step.
            ///     shape: (series, thresholds, time)
            /// \param ct_c
            ///     Misses for each time step.
            ///     shape: (series, thresholds, time)
            /// \param ct_d
            ///     Correct rejections for each time step.
            ///     shape: (series, thresholds, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Contingency tables.
            ///     shape: (series, subsets, samples, thresholds, cells)
            template<class XD2>
            inline xt::xtensor<double, 5> calc_CONT_TBL(
                    const XD2& q_thr,
                    const xt::xtensor<double, 3>& ct_a,
                    const xt::xtensor<double, 3>& ct_b,
                    const xt::xtensor<double, 3>& ct_c,
                    const xt::xtensor<double, 3>& ct_d,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 5> CONT_TBL =
                        xt::zeros<double>({n_srs, n_msk, n_exp,
                                           n_thr, std::size_t {4}});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    std::size_t i = 0;
                    for (auto cell: {ct_a, ct_b, ct_c, ct_d})
                    {
                        // apply the mask
                        // (using NaN workaround until reducers work on masked_view)
                        auto cell_masked = xt::where(
                                xt::view(t_msk, xt::all(), m, xt::newaxis(), xt::all()),
                                cell,
                                NAN
                        );

                        // compute variable one sample at a time
                        for (std::size_t e = 0; e < n_exp; e++)
                        {
                            // apply the bootstrap sampling
                            auto cell_masked_sampled =
                                    xt::view(cell_masked, xt::all(), xt::all(),
                                             b_exp[e]);

                            // calculate the mean over the time steps
                            xt::view(CONT_TBL, xt::all(), m, e, xt::all(), i) =
                                    xt::nansum(cell_masked_sampled, -1);
                        }

                        i++;
                    }
                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        CONT_TBL,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::all(),
                                           xt::newaxis()))
                ) = NAN;

                return CONT_TBL;
            }
        }
    }
}

#endif //EVALHYD_DETERMINIST_EVENTS_HPP
