// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#include <fstream>
#include <vector>
#include <tuple>
#include <array>
#include <string>
#include <unordered_map>

#include <gtest/gtest.h>

#include <xtensor/xtensor.hpp>
#include <xtensor/xarray.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmanipulation.hpp>
#include <xtensor/xmath.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xcsv.hpp>

#include "evalhyd/evald.hpp"

#ifndef EVALHYD_DATA_DIR
#error "need to define data directory"
#endif

using namespace xt::placeholders;  // required for `_` to work


std::vector<std::string> all_metrics_d = {
        "MAE", "MARE", "MSE", "RMSE",
        "NSE", "KGE", "KGE_D", "KGEPRIME", "KGEPRIME_D",
        "KGENP", "KGENP_D",
        "CONT_TBL"
};

std::tuple<xt::xtensor<double, 2>, xt::xtensor<double, 2>> load_data_d()
{
    // read in data
    std::ifstream ifs;
    ifs.open(EVALHYD_DATA_DIR "/data/q_obs.csv");
    xt::xtensor<double, 2> observed = xt::load_csv<double>(ifs);
    ifs.close();

    ifs.open(EVALHYD_DATA_DIR "/data/q_prd.csv");
    xt::xtensor<double, 2> predicted = xt::load_csv<double>(ifs);
    ifs.close();

    return std::make_tuple(observed, predicted);
}

std::unordered_map<std::string, xt::xarray<double>> load_expected_d()
{
    // read in expected results
    std::ifstream ifs;
    std::unordered_map<std::string, xt::xarray<double>> expected;

    for (const auto& metric : all_metrics_d)
    {
        ifs.open(EVALHYD_DATA_DIR "/expected/evald/" + metric + ".csv");
        expected[metric] = xt::view(
                xt::squeeze(xt::load_csv<double>(ifs)),
                xt::all(), xt::newaxis(), xt::newaxis()
        );
        ifs.close();
    }

    return expected;
}

TEST(DeterministTests, TestMetrics)
{
    // read in data
    xt::xtensor<double, 2> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_d();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // read in expected results
    auto expected = load_expected_d();

    // compute scores (with 2D tensors)
    std::vector<xt::xarray<double>> results =
            evalhyd::evald(
                    observed, predicted, all_metrics_d, thresholds, "high"
            );

    // check results
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        if (all_metrics_d[m] == "CONT_TBL")
        {
            // /!\ stacked-up thresholds in CSV file because 5D metric,
            //     so need to resize array
            expected[all_metrics_d[m]].resize(
                    {predicted.shape(0), std::size_t {1}, std::size_t {1},
                     thresholds.shape(1), std::size_t {4}}
            );
        }

        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[all_metrics_d[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }
}

TEST(DeterministTests, TestTransform)
{
    // read in data
    xt::xtensor<double, 2> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_d();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // compute and check results on square-rooted streamflow series
    std::vector<xt::xarray<double>> results_sqrt =
            evalhyd::evald(observed, predicted, all_metrics_d,
                           thresholds, "high", "sqrt");

    xt::xtensor<double, 2> obs_sqrt = xt::sqrt(observed);
    xt::xtensor<double, 2> prd_sqrt = xt::sqrt(predicted);
    xt::xtensor<double, 2> thr_sqrt = xt::sqrt(thresholds);

    std::vector<xt::xarray<double>> results_sqrt_ =
            evalhyd::evald(obs_sqrt, prd_sqrt, all_metrics_d,
                           thr_sqrt, "high");

    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results_sqrt[m], results_sqrt_[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

    // compute and check results on inverted streamflow series
    std::vector<xt::xarray<double>> results_inv =
            evalhyd::evald(observed, predicted, all_metrics_d,
                           thresholds, "high", "inv");

    xt::xtensor<double, 2> epsilon = xt::nanmean(observed, {1}, xt::keep_dims) * 0.01;
    xt::xtensor<double, 2> obs_inv = 1. / (observed + epsilon);
    xt::xtensor<double, 2> prd_inv = 1. / (predicted + epsilon);
    xt::xtensor<double, 2> thr_inv = 1. / (thresholds + epsilon);

    std::vector<xt::xarray<double>> results_inv_ =
            evalhyd::evald(obs_inv, prd_inv, all_metrics_d,
                           thr_inv, "high");

    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results_inv[m], results_inv_[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

    // compute and check results on square-rooted streamflow series
    std::vector<xt::xarray<double>> results_log =
            evalhyd::evald(observed, predicted, all_metrics_d,
                           thresholds, "high", "log");

    xt::xtensor<double, 2> obs_log = xt::log(observed + epsilon);
    xt::xtensor<double, 2> prd_log = xt::log(predicted + epsilon);
    xt::xtensor<double, 2> thr_log = xt::log(thresholds + epsilon);

    std::vector<xt::xarray<double>> results_log_ =
            evalhyd::evald(obs_log, prd_log, all_metrics_d,
                           thr_log, "high");

    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results_log[m], results_log_[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

    // compute and check results on power-transformed streamflow series
    std::vector<xt::xarray<double>> results_pow =
            evalhyd::evald(observed, predicted, all_metrics_d,
                           thresholds, "high", "pow", 0.2);

    xt::xtensor<double, 2> obs_pow = xt::pow(observed, 0.2);
    xt::xtensor<double, 2> prd_pow = xt::pow(predicted, 0.2);
    xt::xtensor<double, 2> thr_pow = xt::pow(thresholds, 0.2);

    std::vector<xt::xarray<double>> results_pow_ =
            evalhyd::evald(obs_pow, prd_pow, all_metrics_d,
                           thr_pow, "high");

    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results_pow[m], results_pow_[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

}

TEST(DeterministTests, TestMasks)
{
    // read in data
    xt::xtensor<double, 2> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_d();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // generate temporal subset by dropping 20 first time steps
    xt::xtensor<bool, 3> masks =
            xt::ones<bool>({std::size_t {predicted.shape(0)},
                            std::size_t {1},
                            std::size_t {observed.size()}});
    xt::view(masks, xt::all(), 0, xt::range(0, 20)) = 0;

    // compute scores using masks to subset whole record
    std::vector<xt::xarray<double>> metrics_masked =
            evalhyd::evald(observed, predicted, all_metrics_d,
                           thresholds,  // thresholds
                           "high",  // events
                           xtl::missing<const std::string>(),  // transform
                           xtl::missing<double>(),  // exponent
                           xtl::missing<double>(),  // epsilon
                           masks);

    // compute scores on pre-computed subset of whole record
    xt::xtensor<double, 2> obs = xt::view(observed, xt::all(), xt::range(20, _));
    xt::xtensor<double, 2> prd = xt::view(predicted, xt::all(), xt::range(20, _));

    std::vector<xt::xarray<double>> metrics_subset =
            evalhyd::evald(obs, prd, all_metrics_d, thresholds, "high");

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                metrics_masked[m], metrics_subset[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }
}

TEST(DeterministTests, TestMaskingConditions)
{
    // read in data
    xt::xtensor<double, 2> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_d();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // generate dummy empty masks required to access next optional argument
    xt::xtensor<bool, 3> masks;

    // conditions on streamflow values _________________________________________

    // compute scores using masking conditions on streamflow to subset whole record
    xt::xtensor<std::array<char, 32>, 2> q_conditions = {
            {std::array<char, 32>{"q_obs{<2000,>3000}"}}
    };
    q_conditions = xt::repeat(q_conditions, predicted.shape(0), 0);

    std::vector<xt::xarray<double>> metrics_q_conditioned =
            evalhyd::evald(
                    observed, predicted, all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    masks, q_conditions
            );

    // compute scores using "NaN-ed" time indices where conditions on streamflow met
    std::vector<xt::xarray<double>> metrics_q_preconditioned =
            evalhyd::evald(
                    xt::eval(xt::where((observed < 2000) | (observed > 3000), observed, NAN)),
                    predicted,
                    all_metrics_d,
                    thresholds,
                    "high"
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                metrics_q_conditioned[m], metrics_q_preconditioned[m],
                1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

    // conditions on streamflow statistics _____________________________________

    // compute scores using masking conditions on streamflow to subset whole record
    xt::xtensor<std::array<char, 32>, 2> q_conditions_ = {
            {std::array<char, 32>{"q_obs{>=mean}"}}
    };
    q_conditions_ = xt::repeat(q_conditions_, predicted.shape(0), 0);

    double mean = xt::nanmean(observed, {1})();

    std::vector<xt::xarray<double>> metrics_q_conditioned_ =
            evalhyd::evald(
                    observed, predicted, all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    masks, q_conditions_
            );

    // compute scores using "NaN-ed" time indices where conditions on streamflow met
    std::vector<xt::xarray<double>> metrics_q_preconditioned_ =
            evalhyd::evald(
                    xt::eval(xt::where(observed >= mean, observed, NAN)),
                    predicted,
                    all_metrics_d,
                    thresholds,
                    "high"
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                metrics_q_conditioned_[m], metrics_q_preconditioned_[m],
                1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }

    // conditions on temporal indices __________________________________________

    // compute scores using masking conditions on time indices to subset whole record
    xt::xtensor<std::array<char, 32>, 2> t_conditions = {
            {std::array<char, 32>{"t{0,1,2,3,4,5:97,97,98,99}"}}
    };
    t_conditions = xt::repeat(t_conditions, predicted.shape(0), 0);

    std::vector<xt::xarray<double>> metrics_t_conditioned =
            evalhyd::evald(
                    observed, predicted, all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    masks, t_conditions
            );

    // compute scores on already subset time series
    std::vector<xt::xarray<double>> metrics_t_subset =
            evalhyd::evald(
                    xt::eval(xt::view(observed, xt::all(), xt::range(0, 100))),
                    xt::eval(xt::view(predicted, xt::all(), xt::range(0, 100))),
                    all_metrics_d,
                    thresholds,
                    "high"
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                metrics_t_conditioned[m], metrics_t_subset[m],
                1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }
}

TEST(DeterministTests, TestMissingData)
{
    // read in data
    xt::xtensor<double, 2> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_d();
    predicted = xt::view(predicted, xt::range(0, 5), xt::all());

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // add some missing observations artificially by assigning NaN values
    xt::view(observed, xt::all(), xt::range(0, 20)) = NAN;
    // add some missing predictions artificially by assigning NaN values
    xt::view(observed, 0, xt::range(20, 23)) = NAN;
    xt::view(observed, 1, xt::range(20, 26)) = NAN;
    xt::view(observed, 2, xt::range(20, 29)) = NAN;
    xt::view(observed, 3, xt::range(20, 32)) = NAN;
    xt::view(observed, 4, xt::range(20, 35)) = NAN;

    // compute metrics with observations containing NaN values
    std::vector<xt::xarray<double>> metrics_nan =
            evalhyd::evald(observed, predicted, all_metrics_d, thresholds, "high");

    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        for (std::size_t p = 0; p < predicted.shape(0); p++)
        {
            // compute metrics on subset of observations and predictions (i.e.
            // eliminating region with NaN in observations or predictions manually)
            xt::xtensor<double, 1> obs =
                    xt::view(observed, 0, xt::range(20+(3*(p+1)), _));
            xt::xtensor<double, 1> prd =
                    xt::view(predicted, p, xt::range(20+(3*(p+1)), _));
            xt::xtensor<double, 1> thr =
                    xt::view(thresholds, p);

            std::vector<xt::xarray<double>> metrics_sbs =
                    evalhyd::evald(
                            xt::eval(xt::view(obs, xt::newaxis(), xt::all())),
                            xt::eval(xt::view(prd, xt::newaxis(), xt::all())),
                            {all_metrics_d[m]},
                            xt::eval(xt::view(thr, xt::newaxis(), xt::all())),
                            "high"
                    );

            // compare to check results are the same
            EXPECT_TRUE(xt::all(xt::isclose(
                    xt::view(metrics_nan[m], p), metrics_sbs[0],
                    1e-05, 1e-08, true
            ))) << "Failure for (" << all_metrics_d[m] << ")";
        }
    }
}

TEST(DeterministTests, TestBootstrap)
{
    // read in data
    std::ifstream ifs;

    ifs.open(EVALHYD_DATA_DIR "/data/q_obs_1yr.csv");
    xt::xtensor<std::string, 1> x_dts = xt::squeeze(xt::load_csv<std::string>(ifs, ',', 0, 1));
    ifs.close();
    std::vector<std::string> datetimes (x_dts.begin(), x_dts.end());

    ifs.open(EVALHYD_DATA_DIR "/data/q_obs_1yr.csv");
    xt::xtensor<double, 1> observed = xt::squeeze(xt::load_csv<double>(ifs, ',', 1));
    ifs.close();

    ifs.open(EVALHYD_DATA_DIR "/data/q_prd_1yr.csv");
    xt::xtensor<double, 2> predicted = xt::load_csv<double>(ifs, ',', 1);
    ifs.close();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // compute metrics via bootstrap
    std::unordered_map<std::string, int> bootstrap =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 0}};

    std::vector<xt::xarray<double>> metrics_bts =
            evalhyd::evald(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    predicted,
                    all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    xt::xtensor<bool, 3>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap,
                    datetimes
            );

    // compute metrics by repeating year of data 3 times
    // (since there is only one year of data, and that the bootstrap works on
    //  one-year blocks, it can only select that given year to form samples,
    //  and the length of the sample corresponds to how many times this year
    //  is repeated in the sample, so that repeating the input data this many
    //  times should result in the same numerical results)
    xt::xtensor<double, 1> observed_x3 =
            xt::concatenate(xt::xtuple(observed, observed, observed), 0);
    xt::xtensor<double, 2> predicted_x3 =
            xt::concatenate(xt::xtuple(predicted, predicted, predicted), 1);

    std::vector<xt::xarray<double>> metrics_rep =
            evalhyd::evald(
                    xt::eval(xt::view(observed_x3, xt::newaxis(), xt::all())),
                    predicted_x3,
                    all_metrics_d,
                    thresholds,
                    "high"
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                metrics_bts[m], metrics_rep[m], 1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ")";
    }
}

TEST(DeterministTests, TestBootstrapSummary)
{
    // read in data
    std::ifstream ifs;

    ifs.open(EVALHYD_DATA_DIR "/data/q_obs_1yr.csv");
    xt::xtensor<std::string, 1> x_dts = xt::squeeze(xt::load_csv<std::string>(ifs, ',', 0, 1));
    ifs.close();
    std::vector<std::string> datetimes (x_dts.begin(), x_dts.end());

    ifs.open(EVALHYD_DATA_DIR "/data/q_obs_1yr.csv");
    xt::xtensor<double, 1> observed = xt::squeeze(xt::load_csv<double>(ifs, ',', 1));
    ifs.close();

    ifs.open(EVALHYD_DATA_DIR "/data/q_prd_1yr.csv");
    xt::xtensor<double, 2> predicted = xt::load_csv<double>(ifs, ',', 1);
    ifs.close();

    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    thresholds = xt::repeat(thresholds, predicted.shape(0), 0);

    // compute metrics via bootstrap with raw summary
    std::unordered_map<std::string, int> bootstrap_0 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 0}};

    std::vector<xt::xarray<double>> metrics_raw =
            evalhyd::evald(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    predicted,
                    all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    xt::xtensor<bool, 3>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_0,
                    datetimes
            );

    // compute metrics via bootstrap with mean and standard deviation summary
    std::unordered_map<std::string, int> bootstrap_1 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 1}};

    std::vector<xt::xarray<double>> metrics_mas =
            evalhyd::evald(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    predicted,
                    all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    xt::xtensor<bool, 3>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_1,
                    datetimes
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        // mean
        EXPECT_TRUE(xt::all(xt::isclose(
                xt::mean(metrics_raw[m], {2}),
                xt::view(metrics_mas[m], xt::all(), xt::all(), 0),
                1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ") on mean";
        // standard deviation
        EXPECT_TRUE(xt::all(xt::isclose(
                xt::stddev(metrics_raw[m], {2}),
                xt::view(metrics_mas[m], xt::all(), xt::all(), 1),
                1e-05, 1e-08, true
        ))) << "Failure for (" << all_metrics_d[m] << ") on standard deviation";
    }

    // compute metrics via bootstrap with quantiles summary
    std::unordered_map<std::string, int> bootstrap_2 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 2}};

    std::vector<xt::xarray<double>> metrics_qtl =
            evalhyd::evald(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    predicted,
                    all_metrics_d,
                    thresholds,  // thresholds
                    "high",  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    xt::xtensor<bool, 3>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_2,
                    datetimes
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_d.size(); m++)
    {
        // quantiles
        std::vector<double> quantiles = {0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95};
        std::size_t i = 0;

        for (auto q : quantiles)
        {
            EXPECT_TRUE(xt::all(xt::isclose(
                    xt::quantile(metrics_raw[m], {q}, 2),
                    xt::view(metrics_qtl[m], xt::all(), xt::all(), i),
                    1e-05, 1e-08, true
            ))) << "Failure for (" << all_metrics_d[m] << ") on quantile " << q;
            i++;
        }
    }
}

TEST(DeterministTests, TestCompleteness)
{
    std::vector<std::string> diags = {"completeness"};

    // compute metrics on series with NaN
    xt::xtensor<double, 2> prd = {
            { 5.3, NAN, 5.7, 2.3, 3.3, 4.1 },
            { 4.3, 4.2, 4.7, 4.3, 3.3, 2.8 },
            { 5.3, NAN, 5.7, 2.3, 3.8, NAN }
    };

    xt::xtensor<double, 2> obs =
            {{ 4.7, 4.3, NAN, 2.7, 4.1, 5.0 }};

    xt::xtensor<bool, 3> msk = {
            {{ true, true, true, false, true, true },
             { true, true, true, true, true, true  }},
            {{ true, true, true, true, true, false },
             { true, true, true, true, true, true  }},
            {{ true, true, true, false, false, true },
             { true, true, true, true, true, true  }}
    };

    std::vector<xt::xarray<double>> results =
            evalhyd::evald(
                    obs,
                    prd,
                    std::vector<std::string> {},  // metrics
                    xt::xtensor<double, 2>({}),  // thresholds
                    xtl::missing<const std::string>(),  // events
                    xtl::missing<const std::string>(),  // transform
                    xtl::missing<double>(),  // exponent
                    xtl::missing<double>(),  // epsilon
                    msk,  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    xtl::missing<const std::unordered_map<std::string, int>>(),  // bootstrap
                    {},  // dts
                    xtl::missing<const int>(),  // seed
                    diags
            );

    // check that numerical results are identical
    xt::xtensor<double, 3> expected = {
            {{ 3. },
             { 4. }},
            {{ 4. },
             { 5. }},
            {{ 1. },
             { 3. }}
    };

    EXPECT_TRUE(
            xt::all(xt::isclose(results[0], expected, 1e-05, 1e-08, true))
    );
}
