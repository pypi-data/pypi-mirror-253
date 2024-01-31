// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_DIAGNOSTICS_HPP
#define EVALHYD_PROBABILIST_DIAGNOSTICS_HPP

namespace evalhyd
{
    namespace probabilist
    {
        namespace elements
        {
            /// Counts the number of time steps available in given period.
            ///
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
            ///     Time step counts.
            ///     shape: (sites, lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_t_counts(
                    const xt::xtensor<bool, 4>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_sit,
                    std::size_t n_ldt,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // initialise output variable
                xt::xtensor<double, 4> t_counts =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute variable one sample at a time
                for (std::size_t e = 0; e < n_exp; e++)
                {
                    // apply the bootstrap sampling
                    auto t_msk_sampled =
                            xt::view(t_msk, xt::all(), xt::all(), xt::all(), b_exp[e]);

                    // calculate the mean over the time steps
                    xt::view(t_counts, xt::all(), xt::all(), xt::all(), e) =
                            xt::sum(t_msk_sampled, -1);
                }

                return t_counts;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_DIAGNOSTICS_HPP
