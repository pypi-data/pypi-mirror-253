// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_DETERMINIST_EFFICIENCIES_HPP
#define EVALHYD_DETERMINIST_EFFICIENCIES_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xoperation.hpp>

#include "../maths.hpp"


namespace evalhyd
{
    namespace determinist
    {
        namespace elements
        {
            /// Compute the Pearson correlation coefficient.
            ///
            /// \param err_obs
            ///     Errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            /// \param err_prd
            ///     Errors between predictions and mean prediction.
            ///     shape: (subsets, samples, series, time)
            /// \param quad_err_obs
            ///     Quadratic errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            /// \param quad_err_prd
            ///     Quadratic errors between predictions and mean prediction.
            ///     shape: (subsets, samples, series, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Pearson correlation coefficients.
            ///     shape: (subsets, samples, series)
            inline xt::xtensor<double, 3> calc_r_pearson(
                    const xt::xtensor<double, 4>& err_obs,
                    const xt::xtensor<double, 4>& err_prd,
                    const xt::xtensor<double, 4>& quad_err_obs,
                    const xt::xtensor<double, 4>& quad_err_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // calculate error in timing and dynamics $r_{pearson}$
                // (Pearson's correlation coefficient)
                xt::xtensor<double, 3> r_pearson =
                        xt::zeros<double>({n_msk, n_exp, n_srs});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        auto prd = xt::view(err_prd, m, e, xt::all(), b_exp[e]);
                        auto obs = xt::view(err_obs, m, e, xt::all(), b_exp[e]);
                        auto r_num = xt::nansum(prd * obs, -1);

                        auto prd2 = xt::view(quad_err_prd, m, e, xt::all(), b_exp[e]);
                        auto obs2 = xt::view(quad_err_obs, m, e, xt::all(), b_exp[e]);
                        auto r_den = xt::sqrt(
                                xt::nansum(prd2, -1) * xt::nansum(obs2, -1)
                        );

                        xt::view(r_pearson, m, e) = r_num / r_den;
                    }
                }

                return r_pearson;
            }

            /// Compute the Spearman rank correlation coefficient.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (series, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Spearman rank correlation coefficients.
            ///     shape: (subsets, samples, series)
            template <class XD2>
            inline xt::xtensor<double, 3> calc_r_spearman(
                    const XD2& q_obs,
                    const XD2& q_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // calculate error in timing and dynamics $r_{spearman}$
                // (Spearman's rank correlation coefficient)
                xt::xtensor<double, 3> r_spearman =
                        xt::zeros<double>({n_msk, n_exp, n_srs});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute one series at a time because xt::sort does not
                        // consistently put NaN values at the end/beginning, so
                        // need to eliminate them before the sorting
                        for (std::size_t s = 0; s < n_srs; s++)
                        {
                            auto prd = xt::view(prd_masked, s, b_exp[e]);
                            auto obs = xt::view(obs_masked, s, b_exp[e]);

                            auto prd_filtered =
                                    xt::filter(prd, !xt::isnan(prd));
                            auto obs_filtered =
                                    xt::filter(obs, !xt::isnan(obs));

                            auto prd_sort = xt::argsort(
                                    xt::eval(prd_filtered), {0},
                                    xt::sorting_method::stable
                            );
                            auto obs_sort = xt::argsort(
                                    xt::eval(obs_filtered), {0},
                                    xt::sorting_method::stable
                            );

                            auto prd_rank = xt::eval(xt::argsort(prd_sort));
                            auto obs_rank = xt::eval(xt::argsort(obs_sort));

                            auto mean_rank = (prd_rank.size() - 1) / 2.;

                            auto prd_rank_err = xt::eval(prd_rank - mean_rank);
                            auto obs_rank_err = xt::eval(obs_rank - mean_rank);

                            auto r_num = xt::nansum(prd_rank_err * obs_rank_err);

                            auto r_den = xt::sqrt(
                                    xt::nansum(xt::square(prd_rank_err))
                                    * xt::nansum(xt::square(obs_rank_err))
                            );

                            xt::view(r_spearman, m, e, s) = r_num / r_den;
                        }
                    }
                }

                return r_spearman;
            }

            /// Compute alpha.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (series, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param mean_obs
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param mean_prd
            ///     Mean predicted streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Alphas, ratios of standard deviations.
            ///     shape: (subsets, samples, series)
            template <class XD2>
            inline xt::xtensor<double, 3> calc_alpha(
                    const XD2& q_obs,
                    const XD2& q_prd,
                    const xt::xtensor<double, 4>& mean_obs,
                    const xt::xtensor<double, 4>& mean_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // calculate error in spread of flow $alpha$
                xt::xtensor<double, 3> alpha =
                        xt::zeros<double>({n_msk, n_exp, n_srs});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        auto prd = xt::view(prd_masked, xt::all(), b_exp[e]);
                        auto obs = xt::view(obs_masked, xt::all(), b_exp[e]);
                        xt::view(alpha, m, e) =
                                maths::nanstd(prd, xt::view(mean_prd, m, e))
                                / maths::nanstd(obs, xt::view(mean_obs, m, e));
                    }
                }

                return alpha;
            }

            /// Compute gamma.
            ///
            /// \param mean_obs
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param mean_prd
            ///     Mean predicted streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param alpha
            ///     Alphas, ratios of standard deviations.
            ///     shape: (subsets, samples, series)
            /// \return
            ///     Gammas, ratios of standard deviations normalised by
            ///     their means.
            ///     shape: (subsets, samples, series)
            inline xt::xtensor<double, 3> calc_gamma(
                    const xt::xtensor<double, 4>& mean_obs,
                    const xt::xtensor<double, 4>& mean_prd,
                    const xt::xtensor<double, 3>& alpha
            )
            {
                // calculate normalised error in spread of flow $gamma$
                xt::xtensor<double, 3> gamma =
                        alpha * (xt::view(mean_obs, xt::all(), xt::all(), xt::all(), 0)
                                 / xt::view(mean_prd, xt::all(), xt::all(), xt::all(), 0));

                return gamma;
            }

            /// Compute non-parametric alpha.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (series, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param mean_obs
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param mean_prd
            ///     Mean predicted streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Non-parametric alphas.
            ///     shape: (subsets, samples, series)
            template <class XD2>
            inline xt::xtensor<double, 3> calc_alpha_np(
                    const XD2& q_obs,
                    const XD2& q_prd,
                    const xt::xtensor<double, 4>& mean_obs,
                    const xt::xtensor<double, 4>& mean_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // calculate error in spread of flow $alpha$
                xt::xtensor<double, 3> alpha_np =
                        xt::zeros<double>({n_msk, n_exp, n_srs});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute one series at a time because xt::sort does not
                        // consistently put NaN values at the end/beginning, so
                        // need to eliminate them before the sorting
                        for (std::size_t s = 0; s < n_srs; s++)
                        {
                            auto prd = xt::view(prd_masked, s, b_exp[e]);
                            auto obs = xt::view(obs_masked, s, b_exp[e]);

                            auto prd_filtered =
                                    xt::filter(prd, !xt::isnan(prd));
                            auto obs_filtered =
                                    xt::filter(obs, !xt::isnan(obs));

                            auto prd_fdc = xt::sort(
                                    xt::eval(prd_filtered
                                             / (prd_filtered.size()
                                                * xt::view(mean_prd, m, e, s)))
                            );
                            auto obs_fdc = xt::sort(
                                    xt::eval(obs_filtered
                                             / (obs_filtered.size()
                                                * xt::view(mean_obs, m, e, s)))
                            );

                            xt::view(alpha_np, m, e, s) =
                                    1 - 0.5 * xt::nansum(xt::abs(prd_fdc - obs_fdc));
                        }
                    }
                }

                return alpha_np;
            }

            /// Compute the bias.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (series, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Biases.
            ///     shape: (subsets, samples, series)
            template <class XD2>
            inline xt::xtensor<double, 3> calc_bias(
                    const XD2& q_obs,
                    const XD2& q_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // calculate $bias$
                xt::xtensor<double, 3> bias =
                        xt::zeros<double>({n_msk, n_exp, n_srs});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        auto prd = xt::view(prd_masked, xt::all(), b_exp[e]);
                        auto obs = xt::view(obs_masked, xt::all(), b_exp[e]);
                        xt::view(bias, m, e) =
                                xt::nansum(prd, -1) / xt::nansum(obs, -1);
                    }
                }

                return bias;
            }
        }

        namespace metrics
        {
            /// Compute the Nash-Sutcliffe Efficiency (NSE).
            ///
            /// \param quad_err
            ///     Quadratic errors between observations and predictions.
            ///     shape: (series, time)
            /// \param quad_err_obs
            ///     Quadratic errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param b_exp
            ///     Boostrap samples.
            ///     shape: (samples, time slice)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Nash-Sutcliffe efficiencies.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_NSE(
                    const xt::xtensor<double, 2>& quad_err,
                    const xt::xtensor<double, 4>& quad_err_obs,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 3> NSE =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto quad_err_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                     quad_err, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute squared errors operands
                        auto err2 = xt::view(quad_err_masked, xt::all(), b_exp[e]);
                        xt::xtensor<double, 1> f_num =
                                xt::nansum(err2, -1);
                        auto obs2 = xt::view(quad_err_obs, m, e, xt::all(), b_exp[e]);
                        xt::xtensor<double, 1> f_den =
                                xt::nansum(obs2, -1);

                        // compute NSE
                        xt::view(NSE, xt::all(), m, e) = 1 - (f_num / f_den);
                    }
                }

                return NSE;
            }

            /// Compute the Kling-Gupta Efficiency (KGE).
            ///
            /// \param r_pearson
            ///     Pearson correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param alpha
            ///     Alphas, ratios of standard deviations.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Kling-Gupta efficiencies.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_KGE(
                    const xt::xtensor<double, 3>& r_pearson,
                    const xt::xtensor<double, 3>& alpha,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 3> KGE =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute KGE
                        xt::view(KGE, xt::all(), m, e) = 1 - xt::sqrt(
                                xt::square(xt::view(r_pearson, m, e) - 1)
                                + xt::square(xt::view(alpha, m, e) - 1)
                                + xt::square(xt::view(bias, m, e) - 1)
                        );
                    }
                }

                return KGE;
            }

            /// Compute the Kling-Gupta Efficiency Decomposed (KGE_D) into
            /// its three components that are the linear correlation (r),
            /// the variability (alpha), and the bias (beta), in this order.
            ///
            /// \param r_pearson
            ///     Pearson correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param alpha
            ///     Alphas, ratios of standard deviations.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     KGE components (r, alpha, beta) for each subset
            ///     and for each threshold.
            ///     shape: (series, subsets, samples, 3)
            inline xt::xtensor<double, 4> calc_KGE_D(
                    const xt::xtensor<double, 3>& r_pearson,
                    const xt::xtensor<double, 3>& alpha,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> KGE_D =
                        xt::zeros<double>({n_srs, n_msk, n_exp, std::size_t {3}});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // put KGE components together
                        xt::view(KGE_D, xt::all(), m, e, 0) =
                                xt::view(r_pearson, m, e);
                        xt::view(KGE_D, xt::all(), m, e, 1) =
                                xt::view(alpha, m, e);
                        xt::view(KGE_D, xt::all(), m, e, 2) =
                                xt::view(bias, m, e);
                    }
                }

                return KGE_D;
            }

            /// Compute the modified Kling-Gupta Efficiency (KGEPRIME).
            ///
            /// \param r_pearson
            ///     Pearson correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param gamma
            ///     Gammas, ratios of standard deviations normalised by
            ///     their means.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Modified Kling-Gupta efficiencies.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_KGEPRIME(
                    const xt::xtensor<double, 3>& r_pearson,
                    const xt::xtensor<double, 3>& gamma,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 3> KGEPRIME =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute KGEPRIME
                        xt::view(KGEPRIME, xt::all(), m, e) =  1 - xt::sqrt(
                                xt::square(xt::view(r_pearson, m, e) - 1)
                                + xt::square(xt::view(gamma, m, e) - 1)
                                + xt::square(xt::view(bias, m, e) - 1)
                        );
                    }
                }

                return KGEPRIME;
            }

            /// Compute the modified Kling-Gupta Efficiency Decomposed
            /// (KGEPRIME_D) into its three components that are the linear
            /// correlation (r), the variability (gamma), and the bias (beta),
            /// in this order.
            ///
            /// \param r_pearson
            ///     Pearson correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param gamma
            ///     Gammas, ratios of standard deviations normalised by
            ///     their means.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Modified KGE components (r, gamma, beta) for each subset
            ///     and for each threshold.
            ///     shape: (series, subsets, samples, 3)
            inline xt::xtensor<double, 4> calc_KGEPRIME_D(
                    const xt::xtensor<double, 3>& r_pearson,
                    const xt::xtensor<double, 3>& gamma,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> KGEPRIME_D =
                        xt::zeros<double>({n_srs, n_msk, n_exp, std::size_t {3}});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // put KGE components together
                        xt::view(KGEPRIME_D, xt::all(), m, e, 0) =
                                xt::view(r_pearson, m, e);
                        xt::view(KGEPRIME_D, xt::all(), m, e, 1) =
                                xt::view(gamma, m, e);
                        xt::view(KGEPRIME_D, xt::all(), m, e, 2) =
                                xt::view(bias, m, e);
                    }
                }

                return KGEPRIME_D;
            }

            /// Compute the non-parametric Kling-Gupta Efficiency (KGENP).
            ///
            /// \param r_spearman
            ///     Spearman rank correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param alpha_np
            ///     Non-parametric alphas.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Modified Kling-Gupta efficiencies.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_KGENP(
                    const xt::xtensor<double, 3>& r_spearman,
                    const xt::xtensor<double, 3>& alpha_np,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 3> KGENP =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // compute KGEPRIME
                        xt::view(KGENP, xt::all(), m, e) =  1 - xt::sqrt(
                                xt::square(xt::view(r_spearman, m, e) - 1)
                                + xt::square(xt::view(alpha_np, m, e) - 1)
                                + xt::square(xt::view(bias, m, e) - 1)
                        );
                    }
                }

                return KGENP;
            }

            /// Compute the non-parametric Kling-Gupta Efficiency
            /// Decomposed (KGENP) into its three components that are the rank
            /// correlation (r), the variability (non-parametric alpha), and
            /// the bias (beta), in this order.
            ///
            /// \param r_spearman
            ///     Spearman correlation coefficients.
            ///     shape: (subsets, samples, series)
            /// \param alpha_np
            ///     Non-parametric alphas.
            ///     shape: (subsets, samples, series)
            /// \param bias
            ///     Biases.
            ///     shape: (subsets, samples, series)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Modified Kling-Gupta efficiencies.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 4> calc_KGENP_D(
                    const xt::xtensor<double, 3>& r_spearman,
                    const xt::xtensor<double, 3>& alpha_np,
                    const xt::xtensor<double, 3>& bias,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> KGENP_D =
                        xt::zeros<double>({n_srs, n_msk, n_exp, std::size_t {3}});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // put KGE components together
                        xt::view(KGENP_D, xt::all(), m, e, 0) =
                                xt::view(r_spearman, m, e);
                        xt::view(KGENP_D, xt::all(), m, e, 1) =
                                xt::view(alpha_np, m, e);
                        xt::view(KGENP_D, xt::all(), m, e, 2) =
                                xt::view(bias, m, e);
                    }
                }

                return KGENP_D;
            }
        }
    }
}

#endif //EVALHYD_DETERMINIST_EFFICIENCIES_HPP
