// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_RANKS_HPP
#define EVALHYD_PROBABILIST_RANKS_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xindex_view.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xrandom.hpp>


namespace evalhyd
{
    namespace probabilist
    {
        namespace elements
        {
            /// Compute the position of the observations amongst the ensemble
            /// member predictions (i.e. their ranks).
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (sites, time)
            /// \param q_qnt
            ///     Streamflow quantiles.
            ///     shape: (sites, lead times, quantiles, time)
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param seed
            ///     Seed to be used by random generator.
            /// \return
            ///     Ranks of streamflow observations.
            ///     shape: (sites, lead times, time)
            template <class XD2, class XD4>
            inline xt::xtensor<double, 3> calc_r_k(
                    const XD2& q_obs,
                    const XD4& q_qnt,
                    std::size_t n_mbr,
                    long int seed
            )
            {
                xt::xtensor<double, 3> ranks = xt::zeros<double>(
                        {q_qnt.shape(0), q_qnt.shape(1), q_qnt.shape(3)}
                );
                xt::view(ranks, xt::all()) = NAN;

                xt::xtensor<double, 3> min_ranks = xt::zeros<double>(
                        {q_qnt.shape(0), q_qnt.shape(1), q_qnt.shape(3)}
                );
                xt::view(min_ranks, xt::all()) = NAN;

                xt::xtensor<double, 3> max_ranks = xt::zeros<double>(
                        {q_qnt.shape(0), q_qnt.shape(1), q_qnt.shape(3)}
                );
                xt::view(max_ranks, xt::all()) = NAN;
                
                for (std::size_t m = 0; m < n_mbr; m++)
                {
                    // strictly below a member and no rank yet
                    xt::view(ranks, xt::all()) = xt::where(
                            (xt::view(q_obs, xt::all(), xt::newaxis(), xt::all())
                             < xt::view(q_qnt, xt::all(), xt::all(), m, xt::all()))
                            &&
                            xt::isnan(ranks),
                            m,
                            ranks
                    );

                    // first time tied with a member
                    xt::view(min_ranks, xt::all()) = xt::where(
                            xt::equal(xt::view(q_obs, xt::all(), xt::newaxis(), xt::all()),
                                      xt::view(q_qnt, xt::all(), xt::all(), m, xt::all()))
                            &&
                            xt::isnan(min_ranks),
                            m,
                            min_ranks
                    );

                    // again tied with a member
                    xt::view(max_ranks, xt::all()) = xt::where(
                            xt::equal(xt::view(q_obs, xt::all(), xt::newaxis(), xt::all()),
                                      xt::view(q_qnt, xt::all(), xt::all(), m, xt::all()))
                            &&
                            !xt::isnan(min_ranks),
                            m + 1,
                            max_ranks
                    );
                }

                // above last member
                xt::view(ranks, xt::all()) = xt::where(
                        xt::view(q_obs, xt::all(), xt::newaxis(), xt::all())
                        > xt::view(q_qnt, xt::all(), xt::all(), n_mbr - 1, xt::all()),
                        n_mbr,
                        ranks
                );

                // for ties, take random rank between min and max
                xt::random::seed(seed);
                xt::view(ranks, xt::all()) = xt::where(
                        !xt::isnan(min_ranks),
                        min_ranks
                        + xt::round((max_ranks - max_ranks + 1)
                                    * xt::random::rand<double>(ranks.shape())),
                        ranks
                );

                return ranks;
            }

            /// Compute the number of observations in each interval of the
            /// rank diagram.
            ///
            /// \param r_k
            ///     Ranks of streamflow observations.
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
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Tallies of streamflow observations in each rank interval.
            ///     shape: (sites, lead times, subsets, samples, ranks)
            inline xt::xtensor<double, 5> calc_o_j(
                    const xt::xtensor<double, 3>& r_k,
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
                xt::xtensor<double, 5> o_j =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_mbr + 1});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto r_k_masked = xt::where(
                            xt::view(t_msk, xt::all(), xt::all(), m, xt::all()),
                            r_k,
                            NAN
                    );

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto r_k_masked_sampled =
                                xt::view(r_k_masked, xt::all(), xt::all(),
                                         b_exp[e]);

                        for (std::size_t j = 0; j < n_mbr + 1; j++)
                        {
                            // compute the observed relative frequency
                            // $o_j = \sum_{k \in M_j} r_k$
                            xt::view(o_j, xt::all(), xt::all(), m, e, j) =
                                    xt::sum(
                                            xt::equal(r_k_masked_sampled, j),
                                            -1
                                    );
                        }
                    }
                }

                return o_j;
            }
        }

        namespace metrics
        {
            /// Compute the frequencies of the rank histogram, also known as
            /// Talagrand diagram.
            ///
            /// \param o_j
            ///     Tallies of streamflow observations for all possible ranks.
            ///     shape: (sites, lead times, subsets, samples, ranks)
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
            ///     Frequencies of the rank histogram.
            ///     shape: (sites, lead times, subsets, samples, ranks)
            inline xt::xtensor<double, 5> calc_RANK_HIST(
                    const xt::xtensor<double, 5>& o_j,
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
                xt::xtensor<double, 5> RANK_HIST =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp, n_mbr + 1});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto t_msk_sampled =
                                xt::view(t_msk, xt::all(), xt::all(),
                                         m, b_exp[e]);

                        // calculate length of subset
                        auto l = xt::eval(
                                xt::sum(t_msk_sampled, -1, xt::keep_dims)
                        );

                        // compute the rank diagram
                        xt::view(RANK_HIST, xt::all(), xt::all(), m, e, xt::all()) =
                                xt::view(o_j, xt::all(), xt::all(),
                                         m, e, xt::all())
                                / l
                        ;
                    }
                }

                return RANK_HIST;
            }

            /// Compute the Delta score.
            ///
            /// \param o_j
            ///     Tallies of streamflow observations for all possible ranks.
            ///     shape: (sites, lead times, subsets, samples, ranks)
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
            ///     Delta scores.
            ///     shape: (sites, lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_DS(
                    const xt::xtensor<double, 5>& o_j,
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
                xt::xtensor<double, 4> DS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute variable one mask at a time to minimise memory imprint
                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto t_msk_sampled =
                                xt::view(t_msk, xt::all(), xt::all(),
                                         m, b_exp[e]);

                        // calculate length of subset
                        auto l = xt::eval(
                                xt::sum(t_msk_sampled, -1, xt::keep_dims)
                        );

                        // compute the Delta score
                        // \Delta = \sum_{k=1}^{N+1} (r_k - \frac{M}{N+1})^2
                        auto delta =  xt::nansum(
                                xt::square(
                                        xt::view(o_j, xt::all(), xt::all(), m, e, xt::all())
                                        - (l / (n_mbr + 1))
                                ),
                                -1
                        );

                        // \Delta_o = \frac{MN}{N+1}
                        auto delta_o = (
                                xt::view(l, xt::all(), xt::all(), 0)
                                * n_mbr / (n_mbr + 1)
                        );

                        // \delta = $\frac{\Delta}{\Delta_o}
                        xt::view(DS, xt::all(), xt::all(), m, e) =
                               delta / delta_o;
                    }
                }

                return DS;
            }

            /// Compute the Alpha score.
            ///
            /// \param r_k
            ///     Ranks of streamflow observations.
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
            /// \param n_mbr
            ///     Number of ensemble members.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Alpha scores.
            ///     shape: (sites, lead times, subsets, samples)
            inline xt::xtensor<double, 4> calc_AS(
                    const xt::xtensor<double, 3>& r_k,
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
                xt::xtensor<double, 4> AS =
                        xt::zeros<double>({n_sit, n_ldt, n_msk, n_exp});

                // compute one site and one leadtime at a time because of
                // potential NaN (of varying numbers across sites/lead times)
                // in the ranks that are not put at the end with `xt::sort`
                // (unlike `numpy.sort`) which prevent from an easy conversion
                // from rank to probability
                for (std::size_t s = 0; s < n_sit; s++)
                {
                    for (std::size_t l = 0; l < n_ldt; l++)
                    {
                        // compute variable one mask at a time to minimise memory imprint
                        for (std::size_t m = 0; m < n_msk; m++)
                        {
                            // apply the mask
                            // (using NaN workaround until reducers work on masked_view)
                            auto r_k_masked = xt::where(
                                    xt::view(t_msk, s, l, m, xt::all()),
                                    xt::view(r_k, s, l, xt::all()),
                                    NAN
                            );

                            // compute variable one sample at a time
                            for (std::size_t e = 0; e < n_exp; e++)
                            {
                                // apply the bootstrap sampling
                                auto r_k_masked_sampled =
                                        xt::view(r_k_masked, b_exp[e]);

                                // notations below follow Renard et al. (2010)
                                // https://doi.org/10.1029/2009WR008328

                                // compute observed p values
                                // $p_{x(i)}$
                                auto p_x_i = xt::sort(
                                        xt::eval(
                                                // filter out NaNs
                                                xt::filter(
                                                        r_k_masked_sampled,
                                                        !xt::isnan(r_k_masked_sampled)
                                                )
                                                / n_mbr
                                        )
                                );

                                // calculate length of realisations
                                // $N_x$
                                auto N_x = p_x_i.size();

                                // compute theoretical p values
                                // $p_{x(i)}^{(th)}$
                                auto p_x_i_th =
                                        xt::arange<double>(double(N_x)) / (N_x - 1);

                                // compute area between the predictive curve and
                                // the 1:1 line in the Q-Q plot
                                // $\alpha'_x$
                                auto alpha_prime_x = xt::nanmean(
                                        xt::abs(p_x_i - p_x_i_th)
                                );

                                // compute the alpha score
                                // $\alpha_x = 1 - 2 \alpha'_x$
                                xt::view(AS, s, l, m, e) = 1 - 2 * alpha_prime_x;
                            }
                        }
                    }
                }

                return AS;
            }
        }
    }
}

#endif //EVALHYD_PROBABILIST_RANKS_HPP
