// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_QUANTILES_HPP
#define EVALHYD_PROBABILIST_QUANTILES_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
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
            /// Compute the forecast quantiles from the ensemble members.
            ///
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (sites, lead times, members, time)
            /// \return
            ///     Streamflow forecast quantiles.
            ///     shape: (sites, lead times, quantiles, time)
            template <class XD4>
            inline xt::xtensor<double, 4> calc_q_qnt(
                    const XD4& q_prd
            )
            {
                return xt::sort(q_prd, 2);
            }
        }

        namespace intermediate
        {
            /// Compute the quantile scores for each time step.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_qnt
            ///     Streamflow quantiles.
            ///     shape: (sites, lead times, quantiles, time)
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \return
            ///     Quantile scores for each time step.
            ///     shape: (sites, lead times, quantiles, time)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_qs(
                    const XD2 &q_obs,
                    const xt::xtensor<double, 4>& q_qnt,
                    std::size_t n_mbr
            )
            {
                // compute the quantile order $alpha$
                xt::xtensor<double, 1> alpha =
                        xt::arange<double>(1., double(n_mbr + 1))
                        / double(n_mbr + 1);

                // calculate the difference
                xt::xtensor<double, 4> diff =
                        q_qnt - xt::view(q_obs, xt::all(), xt::newaxis(),
                                         xt::newaxis(), xt::all());

                // calculate the quantile scores
                xt::xtensor<double, 4> qs = xt::where(
                        diff > 0,
                        2 * (1 - xt::view(alpha, xt::newaxis(), xt::newaxis(),
                                          xt::all(), xt::newaxis())) * diff,
                        - 2 * xt::view(alpha, xt::newaxis(), xt::newaxis(),
                                       xt::all(), xt::newaxis()) * diff
                );

                return qs;
            }

            /// Compute the continuous rank probability score(s) based
            /// on quantile scores for each time step, and integrating using the
            /// trapezoidal rule.
            ///
            /// /!\ The number of quantiles must be sufficiently large so that the
            ///     cumulative distribution is smooth enough for the numerical
            ///     integration to be accurate.
            ///
            /// \param qs
            ///     Quantile scores for each time step.
            ///     shape: (sites, lead times, quantiles, time)
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \return
            ///     CRPS for each time step.
            ///     shape: (sites, lead times, time)
            inline xt::xtensor<double, 3> calc_crps_from_qs(
                    const xt::xtensor<double, 4>& qs,
                    std::size_t n_mbr
            )
            {
                // integrate with trapezoidal rule
                // xt::trapz(y, dx=1/(n+1), axis=2)
                return xt::trapz(qs, 1./(double(n_mbr) + 1.), 2);
            }
        }

        namespace metrics
        {
            /// Compute the quantile score (QS).
            ///
            /// \param qs
            ///     Quantile scores for each time step.
            ///     shape: (sites, lead times, quantiles, time)
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
            ///     Quantile scores.
            ///     shape: (sites, lead times, subsets, samples, quantiles)
            inline xt::xtensor<double, 5> calc_QS(
                    const xt::xtensor<double, 4>& qs,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_mbr,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 5> QS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_mbr});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto qs_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m,
                                     xt::newaxis(), xt::all()),
                            qs,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto qs_masked_sampled =
                                xt::view(qs_masked, xt::all(), xt::all(),
                                         xt::all(), b_exp[e]);

                        // calculate the mean over the time steps
                        // $QS = \frac{1}{n} \sum_{k=1}^{n} qs$
                        xt::view(QS, xt::all(), xt::all(), m, e, xt::all()) =
                                xt::nanmean(qs_masked_sampled, -1);
                    }
                }

                return QS;
            }

            /// Compute the continuous rank probability score based on the
            /// integration over the quantile scores (CRPS_FROM_QS).
            ///
            /// \param crps_from_qs
            ///     CRPS for each time step.
            ///     shape: (sites, lead times, time)
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
            ///     CRPS.
            ///     shape: (sites, lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_CRPS_FROM_QS(
                    const xt::xtensor<double, 3>& crps_from_qs,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 4> CRPS_FROM_QS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto crps_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            crps_from_qs,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto crps_masked_sampled =
                                xt::view(crps_masked, xt::all(), xt::all(),
                                         b_exp[e]);

                        // calculate the mean over the time steps
                        // $CRPS = \frac{1}{n} \sum_{k=1}^{n} crps$
                        xt::view(CRPS_FROM_QS, xt::all(), xt::all(), m, e) =
                                xt::squeeze(xt::nanmean(crps_masked_sampled, -1));
                    }
                }

                return CRPS_FROM_QS;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_QUANTILES_HPP
