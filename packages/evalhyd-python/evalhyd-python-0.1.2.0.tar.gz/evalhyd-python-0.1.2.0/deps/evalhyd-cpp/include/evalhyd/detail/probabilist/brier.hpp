// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_BRIER_HPP
#define EVALHYD_PROBABILIST_BRIER_HPP

#include <limits>

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xindex_view.hpp>
#include <xtensor/xmasked_view.hpp>
#include <xtensor/xsort.hpp>
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
            /// Determine observed realisation of threshold(s) exceedance.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param is_high_flow_event
            ///     Whether events correspond to being above the threshold(s).
            /// \return
            ///     Event observed outcome.
            ///     shape: (sites, thresholds, time)
            template<class XD2a, class XD2b>
            inline xt::xtensor<double, 3> calc_o_k(
                    const XD2a& q_obs,
                    const XD2b& q_thr,
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

            /// Determine mean observed realisation of threshold(s) exceedance.
            ///
            /// \param o_k
            ///     Event observed outcome.
            ///     shape: (sites, thresholds, time)
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
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Mean event observed outcome.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
            inline xt::xtensor<double, 5> calc_bar_o(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 5> bar_o =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr});

                // apply the mask
                // (using NaN workaround until reducers work on masked_view)
                auto o_k_masked = xt::where(
                        xt::view(t_msk, xt::all(), xt::all(),
                                 xt::all(), xt::newaxis(), xt::all()),
                        xt::view(o_k, xt::all(), xt::newaxis(),
                                 xt::newaxis(), xt::all(), xt::all()),
                        NAN
                );

                // compute variable one sample at a time
                for (std::size_t e = 0; e < n_exp; e++)
                {
                    // apply the bootstrap sampling
                    auto o_k_masked_sampled =
                            xt::view(o_k_masked, xt::all(), xt::all(),
                                     xt::all(), xt::all(), b_exp[e]);

                    // compute mean "climatology" relative frequency of the event
                    // $\bar{o} = \frac{1}{n} \sum_{k=1}^{n} o_k$
                    xt::view(bar_o, xt::all(), xt::all(), xt::all(), e, xt::all()) =
                            xt::nanmean(o_k_masked_sampled, -1);
                }

                return bar_o;
            }

            /// Determine number of forecast members exceeding threshold(s)
            ///
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (sites, lead times, members, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param is_high_flow_event
            ///     Whether events correspond to being above the threshold(s).
            /// \return
            ///     Number of forecast members exceeding threshold(s).
            ///     shape: (sites, lead times, thresholds, time)
            template<class XD4, class XD2>
            inline xt::xtensor<double, 4> calc_sum_f_k(
                    const XD4& q_prd,
                    const XD2& q_thr,
                    bool is_high_flow_event
            )
            {
                if (is_high_flow_event)
                {
                    // determine if members are above threshold(s)
                    auto f_k = xt::view(q_prd, xt::all(), xt::all(),
                                        xt::newaxis(), xt::all(), xt::all())
                               >= xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::all(), xt::newaxis(), xt::newaxis());

                    // calculate how many members are above threshold(s)
                    return xt::sum(f_k, 3);
                }
                else
                {
                    // determine if members are below threshold(s)
                    auto f_k = xt::view(q_prd, xt::all(), xt::all(),
                                        xt::newaxis(), xt::all(), xt::all())
                               <= xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::all(), xt::newaxis(), xt::newaxis());

                    // calculate how many members are below threshold(s)
                    return xt::sum(f_k, 3);
                }
            }

            /// Determine forecast probability of threshold(s) exceedance to occur.
            ///
            /// \param sum_f_k
            ///     Number of forecast members exceeding threshold(s).
            ///     shape: (sites, lead times, thresholds, time)
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \return
            ///     Event probability forecast.
            ///     shape: (sites, lead times, thresholds, time)
            inline xt::xtensor<double, 4> calc_y_k(
                    const xt::xtensor<double, 4>& sum_f_k,
                    std::size_t n_mbr
            )
            {
                // determine probability of threshold(s) exceedance
                // /!\ probability calculation dividing by n (the number of
                //     members), not n+1 (the number of ranks) like in other metrics
                return sum_f_k / n_mbr;
            }
        }

        namespace intermediate
        {
            /// Compute the Brier score for each time step.
            ///
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param y_k
            ///     Event probability forecast.
            ///     shape: (sites, lead times, thresholds, time)
            /// \return
            ///     Brier score for each threshold for each time step.
            ///     shape: (sites, lead times, thresholds, time)
            inline xt::xtensor<double, 4> calc_bs(
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 4>& y_k
            )
            {
                // return computed Brier score(s)
                // $bs = (o_k - y_k)^2$
                return xt::square(
                        xt::view(o_k, xt::all(), xt::newaxis(),
                                 xt::all(), xt::all())
                        - y_k
                );
            }
        }

        namespace metrics
        {
            /// Compute the Brier score (BS).
            ///
            /// \param bs
            ///     Brier score for each threshold for each time step.
            ///     shape: (sites, lead times, thresholds, time)
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
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Brier score for each subset and for each threshold.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 5> calc_BS(
                    const xt::xtensor<double, 4>& bs,
                    const XD2& q_thr,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 5> BS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto bs_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m,
                                     xt::newaxis(), xt::all()),
                            bs,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto bs_masked_sampled =
                                xt::view(bs_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);

                        // calculate the mean over the time steps
                        // $BS = \frac{1}{n} \sum_{k=1}^{n} (o_k - y_k)^2$
                        xt::view(BS, xt::all(), xt::all(), m, e, xt::all()) =
                                xt::nanmean(bs_masked_sampled, -1);
                    }
                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        BS,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all()))
                ) = NAN;

                return BS;
            }

            /// Compute the X and Y axes of the reliability diagram
            /// (`y_i`, the forecast probability; `bar_o_i`, the observed frequency;)
            /// as well as the frequencies of the sampling histogram
            /// (`N_i`, the number of forecasts of given probability `y_i`)'.
            ///
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param y_k
            ///     Event probability forecast.
            ///     shape: (sites, lead times, thresholds, time)
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
            ///     X and Y axes of the reliability diagram, and ordinates
            ///     (i.e. frequencies) of the sampling histogram, in this order.
            ///     shape: (sites, lead times, subsets, samples, thresholds, bins, axes)
            template <class XD2>
            inline xt::xtensor<double, 7> calc_REL_DIAG(
                    const XD2& q_thr,
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 4>& y_k,
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
                xt::xtensor<double, 7> REL_DIAG =
                    xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr,
                                       n_mbr + 1, std::size_t {3}});

                // compute range of forecast values $y_i$
                auto y_i = xt::arange<double>(double(n_mbr + 1)) / n_mbr;

                xt::view(REL_DIAG, xt::all(), xt::all(), xt::all(), xt::all(),
                         xt::all(), xt::all(), 0) = y_i;

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto o_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(),
                                     m, xt::newaxis(), xt::all()),
                            xt::view(o_k, xt::all(), xt::newaxis(),
                                     xt::all(), xt::all()),
                            NAN
                    );
                    auto y_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(),
                                     m, xt::newaxis(), xt::all()),
                            y_k,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto o_k_masked_sampled =
                                xt::view(o_k_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);
                        auto y_k_masked_sampled =
                                xt::view(y_k_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);
                        auto t_msk_sampled =
                                xt::view(t_msk, xt::all(), xt::all(), m,
                                         xt::newaxis(), b_exp[e]);

                        // compute mask to subsample time steps belonging to same forecast bin
                        // (where bins are defined as the range of forecast values)
                        auto msk_bins = xt::equal(
                                // force evaluation to avoid segfault
                                xt::view(xt::eval(y_k_masked_sampled),
                                         xt::all(), xt::all(), xt::all(),
                                         xt::newaxis(), xt::all()),
                                xt::view(y_i,
                                         xt::newaxis(), xt::newaxis(), xt::newaxis(),
                                         xt::all(), xt::newaxis())
                        );

                        // compute number of forecasts in each forecast bin $N_i$
                        auto N_i = xt::eval(xt::sum(msk_bins, -1));

                        xt::view(REL_DIAG, xt::all(), xt::all(), m, e, xt::all(),
                                 xt::all(), 2) = N_i;

                        // compute subsample relative frequency
                        // $\bar{o_i} = \frac{1}{N_i} \sum_{k \in N_i} o_k$
                        auto bar_o_i = xt::where(
                                N_i > 0,
                                xt::nansum(
                                        xt::where(
                                                msk_bins,
                                                xt::view(o_k_masked_sampled,
                                                         xt::all(), xt::all(),
                                                         xt::all(), xt::newaxis(),
                                                         xt::all()),
                                                0.
                                        ),
                                        -1
                                ) / N_i,
                                0.
                        );

                        xt::view(REL_DIAG, xt::all(), xt::all(), m, e, xt::all(),
                                 xt::all(), 1) = bar_o_i;
                    }
                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        REL_DIAG,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all(), xt::newaxis(),
                                           xt::newaxis()))
                ) = NAN;

                return REL_DIAG;
            }

            /// Compute the calibration-refinement decomposition of the Brier score
            /// into reliability, resolution, and uncertainty.
            ///
            /// BS = reliability - resolution + uncertainty
            ///
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param bar_o
            ///     Mean event observed outcome.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
            /// \param REL_DIAG
            ///     Axes of the reliability diagram and the sampling histogram.
            ///     shape: (sites, lead times, thresholds, time)
            /// \param t_counts
            ///     Time step counts for the period.
            ///     shape: (sites, lead times, subsets, samples)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Brier score components (reliability, resolution, uncertainty)
            ///     for each subset and for each threshold.
            ///     shape: (sites, lead times, subsets, samples, thresholds, bins, axes)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_BS_CRD(
                    const XD2& q_thr,
                    const xt::xtensor<double, 5>& bar_o,
                    const xt::xtensor<double, 7>& REL_DIAG,
                    const xt::xtensor<double, 4>& t_counts,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 6> BS_CRD =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr,
                                           std::size_t {3}});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // retrieve length of period
                        auto l = xt::view(t_counts, xt::all(), xt::all(),
                                          m, xt::newaxis(), e);

                        // retrieve range of forecast values $y_i$
                        auto y_i = xt::eval(
                                xt::view(REL_DIAG, xt::all(), xt::all(), m, e,
                                         xt::all(), xt::all(), 0)
                        );

                        // retrieve number of forecasts in each forecast bin $N_i$
                        auto N_i = xt::eval(
                                xt::view(REL_DIAG, xt::all(), xt::all(), m, e,
                                         xt::all(), xt::all(), 2)
                        );

                        // retrieve subsample relative frequency
                        // $\bar{o_i} = \frac{1}{N_i} \sum_{k \in N_i} o_k$
                        auto bar_o_i = xt::eval(
                                xt::view(REL_DIAG, xt::all(), xt::all(), m, e,
                                         xt::all(), xt::all(), 1)
                        );

                        // retrieve mean event observed outcome $bar_o$
                        auto _bar_o = xt::view(bar_o, xt::all(), xt::all(),
                                               m, e, xt::all());
                        // (reshape to insert size-one axis for "bins")
                        auto _bar_o_ = xt::view(_bar_o, xt::all(), xt::all(),
                                                xt::all(), xt::newaxis());

                        // calculate reliability =
                        // $\frac{1}{n} \sum_{i=1}^{I} N_i (y_i - \bar{o_i})^2$
                        xt::view(BS_CRD, xt::all(), xt::all(), m, e, xt::all(), 0) =
                                xt::nansum(
                                        xt::square(y_i - bar_o_i) * N_i,
                                        -1
                                ) / l;

                        // calculate resolution =
                        // $\frac{1}{n} \sum_{i=1}^{I} N_i (\bar{o_i} - \bar{o})^2$
                        xt::view(BS_CRD, xt::all(), xt::all(), m, e, xt::all(), 1) =
                                xt::nansum(
                                        xt::square(bar_o_i - _bar_o_) * N_i,
                                        -1
                                ) / l;

                        // calculate uncertainty = $\bar{o} (1 - \bar{o})$
                        xt::view(BS_CRD, xt::all(), xt::all(), m, e, xt::all(), 2) =
                                _bar_o * (1 - _bar_o);
                    }
                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        BS_CRD,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all(), xt::newaxis()))
                ) = NAN;

                return BS_CRD;
            }

            /// Compute the likelihood-base rate decomposition of the Brier score
            /// into type 2 bias, discrimination, and sharpness (a.k.a. refinement).
            ///
            /// BS = type 2 bias - discrimination + sharpness
            ///
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param y_k
            ///     Event probability forecast.
            ///     shape: (sites, lead times, thresholds, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param t_counts
            ///     Time step counts for the period.
            ///     shape: (sites, lead times, subsets, samples)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_thr
            ///     Number of thresholds.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Brier score components (type 2 bias, discrimination, sharpness)
            ///     for each subset and for each threshold.
            ///     shape: (sites, lead times, subsets, samples, thresholds, components)
            template <class XD2>
            inline xt::xtensor<double, 6> calc_BS_LBD(
                    const XD2& q_thr,
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 4>& y_k,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    const xt::xtensor<double, 4>& t_counts,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // declare internal variables
                // shape: (sites, lead times, bins, thresholds, time)
                xt::xtensor<double, 5> msk_bins;
                // shape: (sites, lead times, thresholds)
                xt::xtensor<double, 3> bar_y;
                // shape: (sites, lead times, bins, thresholds)
                xt::xtensor<double, 4> M_j, bar_y_j;
                // shape: (bins,)
                xt::xtensor<double, 1> o_j;

                // set the range of observed values $o_j$
                o_j = {0., 1.};

                // declare and initialise output variable
                xt::xtensor<double, 6> BS_LBD =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr,
                                           std::size_t {3}});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto o_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(),
                                     m, xt::newaxis(), xt::all()),
                            xt::view(o_k, xt::all(), xt::newaxis(),
                                     xt::all(), xt::all()),
                            NAN
                    );
                    auto y_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(),
                                     m, xt::newaxis(), xt::all()),
                            y_k,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto o_k_masked_sampled =
                                xt::view(o_k_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);
                        auto y_k_masked_sampled =
                                xt::view(y_k_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);

                        // retrieve length of period
                        auto l = xt::view(t_counts, xt::all(), xt::all(),
                                          m, xt::newaxis(), e);

                        // compute mask to subsample time steps belonging to same observation bin
                        // (where bins are defined as the range of forecast values)
                        msk_bins = xt::equal(
                                // force evaluation to avoid segfault
                                xt::view(xt::eval(o_k_masked_sampled),
                                         xt::all(), xt::all(), xt::newaxis(),
                                         xt::all(), xt::all()),
                                xt::view(o_j,
                                         xt::newaxis(), xt::newaxis(), xt::all(),
                                         xt::newaxis(), xt::newaxis())
                        );

                        // compute number of observations in each observation bin $M_j$
                        M_j = xt::nansum(msk_bins, -1);

                        // compute subsample relative frequency
                        // $\bar{y_j} = \frac{1}{M_j} \sum_{k \in M_j} y_k$
                        bar_y_j = xt::where(
                                M_j > 0,
                                xt::nansum(
                                        xt::where(
                                                msk_bins,
                                                xt::view(y_k_masked_sampled,
                                                         xt::all(), xt::all(),
                                                         xt::newaxis(),
                                                         xt::all(), xt::all()),
                                                0.
                                        ),
                                        -1
                                ) / M_j,
                                0.
                        );

                        // compute mean "climatology" forecast probability
                        // $\bar{y} = \frac{1}{n} \sum_{k=1}^{n} y_k$
                        bar_y = xt::nanmean(y_k_masked_sampled, -1);

                        // calculate type 2 bias =
                        // $\frac{1}{n} \sum_{j=1}^{J} M_j (o_j - \bar{y_j})^2$
                        xt::view(BS_LBD, xt::all(), xt::all(), m, e, xt::all(), 0) =
                                xt::nansum(
                                        xt::square(
                                                xt::view(o_j, xt::newaxis(),
                                                         xt::newaxis(), xt::all(),
                                                         xt::newaxis())
                                                - bar_y_j
                                        ) * M_j,
                                        2
                                ) / l;

                        // calculate discrimination =
                        // $\frac{1}{n} \sum_{j=1}^{J} M_j (\bar{y_j} - \bar{y})^2$
                        xt::view(BS_LBD, xt::all(), xt::all(), m, e, xt::all(), 1) =
                                xt::nansum(
                                        xt::square(
                                                bar_y_j
                                                - xt::view(bar_y,
                                                           xt::all(), xt::all(),
                                                           xt::newaxis(),
                                                           xt::all())
                                        ) * M_j,
                                        2
                                ) / l;

                        // calculate sharpness =
                        // $\frac{1}{n} \sum_{k=1}^{n} (\bar{y_k} - \bar{y})^2$
                        xt::view(BS_LBD, xt::all(), xt::all(), m, e, xt::all(), 2) =
                                xt::nansum(
                                        xt::square(
                                                y_k_masked_sampled
                                                - xt::view(bar_y, xt::all(),
                                                           xt::all(), xt::all(),
                                                           xt::newaxis())
                                        ),
                                        -1
                                ) / l;
                    }

                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        BS_LBD,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all(), xt::newaxis()))
                ) = NAN;

                return BS_LBD;
            }

            /// Compute the Brier skill score (BSS).
            ///
            /// \param bs
            ///     Brier score for each threshold for each time step.
            ///     shape: (sites, lead times, thresholds, time)
            /// \param q_thr
            ///     Streamflow exceedance threshold(s).
            ///     shape: (sites, thresholds)
            /// \param o_k
            ///     Observed event outcome.
            ///     shape: (sites, thresholds, time)
            /// \param bar_o
            ///     Mean event observed outcome.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
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
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Brier skill score for each subset and for each threshold.
            ///     shape: (sites, lead times, subsets, samples, thresholds)
            template <class XD2>
            inline xt::xtensor<double, 5> calc_BSS(
                    const xt::xtensor<double, 4>& bs,
                    const XD2& q_thr,
                    const xt::xtensor<double, 3>& o_k,
                    const xt::xtensor<double, 5>& bar_o,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_thr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // declare and initialise output variable
                xt::xtensor<double, 5> BSS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_thr});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto o_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(),
                                     m, xt::newaxis(), xt::all()),
                            xt::view(o_k, xt::all(), xt::newaxis(),
                                     xt::all(), xt::all()),
                            NAN
                    );
                    auto bs_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m,
                                     xt::newaxis(), xt::all()),
                            bs,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto o_k_masked_sampled =
                                xt::view(o_k_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);
                        auto bs_masked_sampled =
                                xt::view(bs_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);
                        auto bar_o_sampled =
                                xt::view(bar_o, xt::all(), xt::all(),
                                         xt::all(), e, xt::all());

                        // calculate reference Brier score(s)
                        // $bs_{ref} = \frac{1}{n} \sum_{k=1}^{n} (o_k - \bar{o})^2$
                        xt::xtensor<double, 4> bs_ref =
                                xt::nanmean(
                                        xt::square(
                                                o_k_masked_sampled -
                                                xt::view(
                                                        bar_o_sampled, xt::all(),
                                                        xt::all(), m, xt::all(),
                                                        xt::newaxis()
                                                )
                                        ),
                                        -1,
                                        xt::keep_dims
                                );

                        // compute Brier skill score(s)
                        // $BSS = \frac{1}{n} \sum_{k=1}^{n} 1 - \frac{bs}{bs_{ref}}
                        xt::view(BSS, xt::all(), xt::all(), m, e, xt::all()) =
                                xt::nanmean(
                                        xt::where(
                                                xt::equal(bs_ref, 0),
                                                - std::numeric_limits<double>::infinity(),
                                                1 - (bs_masked_sampled / bs_ref)
                                        ),
                                        -1
                                );
                    }
                }

                // assign NaN where thresholds were not provided (i.e. set as NaN)
                xt::masked_view(
                        BSS,
                        xt::isnan(xt::view(q_thr, xt::all(), xt::newaxis(),
                                           xt::newaxis(), xt::newaxis(),
                                           xt::all()))
                ) = NAN;

                return BSS;
            }

            /// Compute the continuous rank probability score based on the
            /// integration over 101 Brier scores (CRPS_FROM_BS), i.e. using the
            /// observed minimum, the 99 observed percentiles, and the observed
            /// maximum as the exceedance thresholds.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (sites, lead times, members, time)
            /// \param is_high_flow_event
            ///     Whether events correspond to being above the threshold(s).
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
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     CRPS for each subset and for each threshold.
            ///     shape: (sites, lead times, subsets, samples)
            template <class XD2, class XD4>
            inline xt::xtensor<double, 4> calc_CRPS_FROM_BS(
                    const XD2& q_obs,
                    const XD4& q_prd,
                    bool is_high_flow_event,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // declare and initialise output variable
                xt::xtensor<double, 4> CRPS_FROM_BS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto q_obs_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            xt::view(q_obs, xt::all(), xt::newaxis(), xt::all()),
                            NAN
                    );
                    auto q_prd_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m,
                                     xt::newaxis(), xt::all()),
                            q_prd,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        for (std::size_t l = 0; l < n_ldt; l++)
                        {
                            // compute empirical thresholds from 99 observed quantiles
                            xt::xtensor<double, 2> thr =
                                    xt::zeros<double>({n_sit, std::size_t {101}});

                            // /!\ need to compute quantiles one site at a time
                            //     because there is no `xt::nanquantile`, so
                            //     need to filter NaN before computing quantiles
                            for (std::size_t s = 0; s < n_sit; s++)
                            {
                                auto obs = xt::view(q_obs_masked, s, l, b_exp[e]);

                                auto obs_filtered = xt::filter(
                                        obs, !xt::isnan(obs)
                                );

                                if (obs_filtered.size() > 0)
                                {
                                    xt::view(thr, s, xt::all()) = xt::quantile(
                                            obs_filtered,
                                            xt::arange<double>(0.00, 1.01, 0.01)
                                    );
                                }
                                else
                                {
                                    xt::view(thr, s, xt::all()) = NAN;
                                }
                            }

                            // compute observed and predicted event outcomes
                            auto o_k = elements::calc_o_k(
                                    xt::view(q_obs_masked, xt::all(), l,
                                             xt::all()),
                                    thr, is_high_flow_event
                            );

                            auto y_k = elements::calc_y_k(
                                    elements::calc_sum_f_k(
                                            xt::view(q_prd_masked, xt::all(), l,
                                                     xt::newaxis(), xt::all(),
                                                     xt::all()),
                                            thr, is_high_flow_event
                                    ),
                                    n_mbr
                            );

                            // compute 99 Brier scores
                            auto bs = intermediate::calc_bs(o_k, y_k);

                            auto bs_masked = xt::where(
                                    xt::view(t_msk, xt::all(), l, xt::newaxis(),
                                             m, xt::newaxis(), xt::all()),
                                    bs,
                                    NAN
                            );

                            auto bs_masked_sampled = xt::view(
                                    bs_masked, xt::all(), xt::all(), xt::all(),
                                    b_exp[e]
                            );

                            auto BS = xt::nanmean(bs_masked_sampled, -1);

                            // compute CRPS from integration over 99 Brier scores
                            xt::view(CRPS_FROM_BS, xt::all(), l, m, e) =
                                    // xt::trapz(y, x, axis=1)
                                    xt::trapz(
                                            xt::view(BS, xt::all(), 0, xt::all()),
                                            thr,
                                            1
                                    );
                        }
                    }
                }

                return CRPS_FROM_BS;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_BRIER_HPP
