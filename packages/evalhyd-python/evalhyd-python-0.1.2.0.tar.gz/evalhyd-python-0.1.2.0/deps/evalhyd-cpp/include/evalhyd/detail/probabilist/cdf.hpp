// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_CDF_HPP
#define EVALHYD_PROBABILIST_CDF_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmath.hpp>


namespace evalhyd
{
    namespace probabilist
    {
        namespace intermediate
        {
            /// Compute the CRPS for each time step as the distance between the
            /// observed and empirical (i.e. constructed from the ensemble
            /// predictions) quadratic cumulative density functions (CDFs).
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_qnt
            ///     Streamflow prediction quantiles.
            ///     shape: (sites, lead times, quantiles, time)
            /// \param n_sit
            ///     Number of sites.
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_tim
            ///     Number of time steps.
            /// \return
            ///     CRPS for each time step.
            ///     shape: (sites, lead times, time)
            template <class XD2>
            inline xt::xtensor<double, 3> calc_crps_from_ecdf(
                    const XD2& q_obs,
                    const xt::xtensor<double, 4>& q_qnt,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_mbr,
                    std::size_t n_tim
            )
            {
                // notations below follow Hersbach (2000)
                // https://doi.org/10.1175/1520-0434(2000)015<0559:DOTCRP>2.0.CO;2

                // declare and initialise internal variables
                xt::xtensor<double, 4> alpha_i =
                        xt::zeros<double>({n_mbr + 1, n_sit, n_ldt, n_tim});

                xt::xtensor<double, 4> beta_i =
                        xt::zeros<double>({n_mbr + 1, n_sit, n_ldt, n_tim});

                // case x_a < x_1
                // i.e. observation is an outlier before predictive range
                auto x_a = xt::view(q_obs, xt::all(), xt::newaxis(), xt::all());
                auto x_1 = xt::view(q_qnt, xt::all(), xt::all(), 0, xt::all());

                auto is_before = x_a < x_1;
                xt::view(beta_i, 0, xt::all()) = xt::where(
                        is_before, x_1 - x_a, xt::view(beta_i, 0)
                );

                for (std::size_t m = 0; m < n_mbr - 1; m++)
                {
                    auto x_i = xt::view(q_qnt, xt::all(), xt::all(), m, xt::all());
                    auto x_ip1 = xt::view(q_qnt, xt::all(), xt::all(), m + 1, xt::all());

                    // case x_a < x_i
                    // i.e. observation below given member
                    auto is_below = x_a < x_i;
                    xt::view(beta_i, m + 1, xt::all()) = xt::where(
                            is_below, x_ip1 - x_i, xt::view(beta_i, m + 1)
                    );

                    // case x_i <= x_a <= x_{i+1}
                    // i.e. observation between given member and next member
                    auto is_between = (x_i <= x_a) && (x_a <= x_ip1);
                    xt::view(alpha_i, m + 1, xt::all()) = xt::where(
                            is_between, x_a - x_i,  xt::view(alpha_i, m + 1)
                    );
                    xt::view(beta_i, m + 1, xt::all()) = xt::where(
                            is_between, x_ip1 - x_a, xt::view(beta_i, m + 1)
                    );

                    // case x_a > x_{i+1}
                    // i.e. observation above next member
                    auto is_above = x_a > x_ip1;
                    xt::view(alpha_i, m + 1, xt::all()) = xt::where(
                            is_above, x_ip1 - x_i, xt::view(alpha_i, m + 1)
                    );
                }

                // case x_a > x_N
                // i.e. observation is an outlier beyond predictive range
                auto x_N = xt::view(q_qnt, xt::all(), xt::all(), n_mbr - 1, xt::all());

                auto is_beyond = x_a > x_N;
                xt::view(alpha_i, n_mbr, xt::all()) = xt::where(
                        is_beyond, x_a - x_N, xt::view(alpha_i, n_mbr)
                );

                // compute crps as difference between the quadratic CDFs
                auto p_i = xt::eval(
                        xt::view(
                                xt::arange<double>(n_mbr + 1) / n_mbr,
                                xt::all(), xt::newaxis(), xt::newaxis(),
                                xt::newaxis()
                        )
                );

                auto crps_from_ecdf = xt::sum(
                        (alpha_i * xt::square(p_i))
                        + (beta_i * xt::square(1 - p_i)),
                        0
                );

                return crps_from_ecdf;
            }
        }

        namespace metrics
        {
            /// Compute the continuous rank probability score based on the
            /// integration over the quadratic difference between the observed
            /// and empirical cumulative density functions (CRPS_FROM_ECDF).
            ///
            /// \param crps_from_ecdf
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
            /// \param n_tim
            ///     Number of time steps.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     CRPS.
            ///     shape: (sites, lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_CRPS_FROM_ECDF(
                    const xt::xtensor<double, 3>& crps_from_ecdf,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 4> CRPS_FROM_ECDF =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto crps_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            crps_from_ecdf,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto crps_masked_sampled = xt::view(
                                crps_masked, xt::all(), xt::all(), b_exp[e]
                        );

                        // calculate the mean over the time steps
                        xt::view(CRPS_FROM_ECDF, xt::all(), xt::all(), m, e) =
                                xt::nanmean(crps_masked_sampled, -1);
                    }
                }

                return CRPS_FROM_ECDF;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_CDF_HPP
