// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_DETERMINIST_ERRORS_HPP
#define EVALHYD_DETERMINIST_ERRORS_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xoperation.hpp>

namespace evalhyd
{
    namespace determinist
    {
        namespace elements
        {
            /// Compute the mean of the observations.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (1, time)
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
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_mean_obs(
                    const XD2& q_obs,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> mean_obs =
                        xt::zeros<double>({n_msk, n_exp, n_srs, std::size_t {1}});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto obs = xt::view(obs_masked, xt::all(), b_exp[e]);
                        xt::view(mean_obs, m, e) =
                                xt::nanmean(obs, -1, xt::keep_dims);
                    }
                }

                return mean_obs;
            }

            /// Compute the mean of the predictions.
            ///
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
            ///     Mean predicted streamflow.
            ///     shape: (subsets, samples, series, 1)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_mean_prd(
                    const XD2& q_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> mean_prd =
                        xt::zeros<double>({n_msk, n_exp, n_srs, std::size_t {1}});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        // apply the bootstrap sampling
                        auto prd = xt::view(prd_masked, xt::all(), b_exp[e]);
                        xt::view(mean_prd, m, e) =
                                xt::nanmean(prd, -1, xt::keep_dims);
                    }
                }

                return mean_prd;
            }

            /// Compute the error between observations and predictions.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (1, time)
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \return
            ///     Errors between observations and predictions.
            ///     shape: (series, time)
            template <class XD2>
            inline xt::xtensor<double, 2> calc_err(
                    const XD2& q_obs,
                    const XD2& q_prd
            )
            {
                return q_obs - q_prd;
            }

            /// Compute the absolute error between observations and predictions.
            ///
            /// \param err
            ///     Errors between observations and predictions.
            ///     shape: (series, time)
            /// \return
            ///     Quadratic errors between observations and predictions.
            ///     shape: (series, time)
            inline xt::xtensor<double, 2> calc_abs_err(
                    const xt::xtensor<double, 2>& err
            )
            {
                return xt::abs(err);
            }

            /// Compute the quadratic error between observations and predictions.
            ///
            /// \param err
            ///     Errors between observations and predictions.
            ///     shape: (series, time)
            /// \return
            ///     Quadratic errors between observations and predictions.
            ///     shape: (series, time)
            inline xt::xtensor<double, 2> calc_quad_err(
                    const xt::xtensor<double, 2>& err
            )
            {
                return xt::square(err);
            }

            /// Compute the error between observations and mean observation.
            ///
            /// \param q_obs
            ///     Streamflow observations.
            ///     shape: (series, time)
            /// \param mean_obs
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_tim
            ///     Number of time steps.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_err_obs(
                    const XD2& q_obs,
                    const xt::xtensor<double, 4>& mean_obs,
                    const xt::xtensor<bool, 3>& t_msk,
                    std::size_t n_srs,
                    std::size_t n_tim,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> err_obs =
                        xt::zeros<double>({n_msk, n_exp, n_srs, n_tim});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto obs_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_obs, NAN);

                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        xt::view(err_obs, m, e) = (
                                obs_masked - xt::view(mean_obs, m, e)
                        );
                    }
                }

                return err_obs;
            }

            /// Compute the quadratic error between observations and mean observation.
            ///
            /// \param err_obs
            ///     Errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            /// \return
            ///     Quadratic errors between observations and mean observation.
            ///     shape: (subsets, samples, series, time)
            inline xt::xtensor<double, 4> calc_quad_err_obs(
                    const xt::xtensor<double, 4>& err_obs
            )
            {
                return xt::square(err_obs);
            }

            /// Compute the error between predictions and mean prediction.
            ///
            /// \param q_prd
            ///     Streamflow predictions.
            ///     shape: (series, time)
            /// \param mean_prd
            ///     Mean predicted streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param t_msk
            ///     Temporal subsets of the whole record.
            ///     shape: (series, subsets, time)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_tim
            ///     Number of time steps.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Errors between predictions and mean prediction.
            ///     shape: (subsets, samples, series, time)
            template <class XD2>
            inline xt::xtensor<double, 4> calc_err_prd(
                    const XD2& q_prd,
                    const xt::xtensor<double, 4>& mean_prd,
                    const xt::xtensor<bool, 3>& t_msk,
                    std::size_t n_srs,
                    std::size_t n_tim,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                xt::xtensor<double, 4> quad_err_prd =
                        xt::zeros<double>({n_msk, n_exp, n_srs, n_tim});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto prd_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                q_prd, NAN);

                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        xt::view(quad_err_prd, m, e) = (
                                prd_masked - xt::view(mean_prd, m, e)
                        );
                    }
                }

                return quad_err_prd;
            }

            /// Compute the quadratic error between predictions and mean prediction.
            ///
            /// \param err_prd
            ///     Errors between predictions and mean prediction.
            ///     shape: (subsets, samples, series, time)
            /// \return
            ///     Quadratic errors between predictions and mean prediction.
            ///     shape: (subsets, samples, series, time)
            inline xt::xtensor<double, 4> calc_quad_err_prd(
                    const xt::xtensor<double, 4>& err_prd
            )
            {
                return xt::square(err_prd);
            }
        }

        namespace metrics
        {
            /// Compute the mean absolute error (MAE).
            ///
            /// \param abs_err
            ///     Absolute errors between observations and predictions.
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
            ///     Mean absolute errors.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_MAE(
                    const xt::xtensor<double, 2>& abs_err,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // compute RMSE
                xt::xtensor<double, 3> MAE =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // apply the mask
                    // (using NaN workaround until reducers work on masked_view)
                    auto abs_err_masked = xt::where(xt::view(t_msk, xt::all(), m),
                                                     abs_err, NAN);

                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        auto err = xt::view(abs_err_masked, xt::all(), b_exp[e]);
                        xt::view(MAE, xt::all(), m, e) = xt::nanmean(err, -1);
                    }
                }

                return MAE;
            }

            /// Compute the mean absolute relative error (MARE).
            ///
            /// \param MAE
            ///     Mean absolute errors.
            ///     shape: (series, subsets, samples)
            /// \param mean_obs
            ///     Mean observed streamflow.
            ///     shape: (subsets, samples, series, 1)
            /// \param n_srs
            ///     Number of prediction series.
            /// \param n_msk
            ///     Number of temporal subsets.
            /// \param n_exp
            ///     Number of bootstrap samples.
            /// \return
            ///     Mean absolute relative errors.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_MARE(
                    const xt::xtensor<double, 3>& MAE,
                    const xt::xtensor<double, 4>& mean_obs,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // compute RMSE
                xt::xtensor<double, 3> MARE =
                        xt::zeros<double>({n_srs, n_msk, n_exp});

                for (std::size_t m = 0; m < n_msk; m++)
                {
                    // compute variable one sample at a time
                    for (std::size_t e = 0; e < n_exp; e++)
                    {
                        xt::view(MARE, xt::all(), m, e) =
                                xt::view(MAE, xt::all(), m, e)
                                / xt::view(mean_obs, m, e, xt::all(), 0);
                    }
                }

                return MARE;
            }

            /// Compute the mean square error (MSE).
            ///
            /// \param quad_err
            ///     Quadratic errors between observations and predictions.
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
            ///     Mean square errors.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_MSE(
                    const xt::xtensor<double, 2>& quad_err,
                    const xt::xtensor<bool, 3>& t_msk,
                    const std::vector<xt::xkeep_slice<int>>& b_exp,
                    std::size_t n_srs,
                    std::size_t n_msk,
                    std::size_t n_exp
            )
            {
                // compute RMSE
                xt::xtensor<double, 3> MSE =
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
                        auto err2 = xt::view(quad_err_masked, xt::all(), b_exp[e]);
                        xt::view(MSE, xt::all(), m, e) = xt::nanmean(err2, -1);
                    }
                }

                return MSE;
            }

            /// Compute the root mean square error (RMSE).
            ///
            /// \param MSE
            ///     Mean square errors.
            ///     shape: (series, subsets, samples)
            /// \return
            ///     Root mean square errors.
            ///     shape: (series, subsets, samples)
            inline xt::xtensor<double, 3> calc_RMSE(
                    const xt::xtensor<double, 3>& MSE
            )
            {
                // compute RMSE
                auto RMSE = xt::sqrt(MSE);

                return RMSE;
            }
        }
    }
}

#endif //EVALHYD_DETERMINIST_ERRORS_HPP
