// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_MULTIVARIATE_HPP
#define EVALHYD_PROBABILIST_MULTIVARIATE_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmath.hpp>


namespace evalhyd
{
    namespace probabilist
    {
        namespace intermediate
        {
            /// Compute the energy score for each time step computed using its
            /// formulation based on expectancies where the ensemble is used as
            /// the random variable.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (sites, lead times, members, time)
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_tim
            ///     Number of time steps.
            /// \return
            ///     CRPS for each time step.
            ///     shape: (lead times, time)
            template <class XD2, class XD4>
            inline xt::xtensor<double, 2> calc_es(
                    const XD2& q_obs,
                    const XD4& q_prd,
                    std::size_t n_ldt,
                    std::size_t n_mbr,
                    std::size_t n_tim
            )
            {
                // notations below follow Gneiting et al. (2008)
                // https://doi.org/10.1007/s11749-008-0114-x

                // initialise internal variable
                xt::xtensor<double, 2> es_xj_x =
                        xt::zeros<double>({n_ldt, n_tim});
                xt::xtensor<double, 2> es_xi_xj =
                        xt::zeros<double>({n_ldt, n_tim});

                for (std::size_t j = 0; j < n_mbr; j++)
                {
                    // $\sum_{j=1}^{m} || x_j - x ||$
                    es_xj_x += xt::sqrt(
                            xt::sum(
                                    xt::square(
                                            // x_j is the jth member of q_prd
                                            xt::view(q_prd, xt::all(), xt::all(),
                                                     j, xt::all())
                                            // x is q_obs
                                            - xt::view(q_obs, xt::all(),
                                                       xt::newaxis(), xt::all())
                                    ),
                                    0
                            )
                    );

                    for (std::size_t i = 0; i < n_mbr; i++)
                    {
                        // $\sum_{i=1}^{m} \sum_{j=1}^{m} || x_i - x_j ||$
                        es_xi_xj += xt::sqrt(
                                xt::sum(
                                        xt::square(
                                                // x_i is the ith member of q_prd
                                                xt::view(q_prd, xt::all(),
                                                         xt::all(), i, xt::all())
                                                // x_j is the jth member of q_prd
                                                - xt::view(q_prd, xt::all(),
                                                           xt::all(), j, xt::all())
                                        ),
                                        0
                                )
                        );
                    }
                }

                auto es = (
                        (1. / n_mbr * es_xj_x)
                        - (1. / (2 * n_mbr * n_mbr) * es_xi_xj)
                );

                return es;
            }
        }

        namespace metrics
        {
            /// Compute the energy score (ES), a multi-site generalisation
            /// of the continuous rank probability score.
            ///
            /// \param es
            ///     ES for each time step.
            ///     shape: (lead times, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (sites, lead times, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_ldt
            ///     Number of lead times.
            /// \param n_tim
            ///     Number of time steps.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     ES.
            ///     shape: (lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_ES(
                    const xt::xtensor<double, 2>& es,
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_ldt,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 4> ES =
                        xt::zeros<double>({std::size_t {1}, n_ldt, n_msk, n_exp});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // determine the multi-site mask (i.e. only retain time
                    // steps where no site is masked)
                    auto msk = xt::prod(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            0
                    );

                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto es_masked = xt::where(msk, es, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto es_masked_sampled = xt::view(
                                es_masked, xt::all(), b_exp[e]
                        );

                        // calculate the mean over the time steps
                        xt::view(ES, 0, xt::all(), m, e) =
                                xt::nanmean(es_masked_sampled, -1);
                    }
                }

                return ES;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_MULTIVARIATE_HPP
