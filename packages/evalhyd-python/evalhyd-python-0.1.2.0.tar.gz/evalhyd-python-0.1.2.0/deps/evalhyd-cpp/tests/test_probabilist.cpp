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

#include <xtl/xoptional.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xarray.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmath.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xmanipulation.hpp>
#include <xtensor/xcsv.hpp>

#include "evalhyd/evalp.hpp"

#ifndef EVALHYD_DATA_DIR
#error "need to define data directory"
#endif

using namespace xt::placeholders;  // required for `_` to work


std::vector<std::string> all_metrics_p = {
        "BS", "BSS", "BS_CRD", "BS_LBD", "REL_DIAG", "CRPS_FROM_BS",
        "CRPS_FROM_ECDF",
        "QS", "CRPS_FROM_QS",
        "CONT_TBL", "POD", "POFD", "FAR", "CSI", "ROCSS",
        "RANK_HIST", "DS", "AS",
        "CR", "AW", "AWN", "WS",
        "ES"
};

std::tuple<xt::xtensor<double, 1>, xt::xtensor<double, 2>> load_data_p()
{
    // read in data
    std::ifstream ifs;
    ifs.open(EVALHYD_DATA_DIR "/data/q_obs.csv");
    xt::xtensor<double, 1> observed = xt::squeeze(xt::load_csv<double>(ifs));
    ifs.close();

    ifs.open(EVALHYD_DATA_DIR "/data/q_prd.csv");
    xt::xtensor<double, 2> predicted = xt::load_csv<double>(ifs);
    ifs.close();

    return std::make_tuple(observed, predicted);
}

std::unordered_map<std::string, xt::xarray<double>> load_expected_p()
{
    // read in expected results
    std::ifstream ifs;
    std::unordered_map<std::string, xt::xarray<double>> expected;

    for (const auto& metric : all_metrics_p)
    {
        ifs.open(EVALHYD_DATA_DIR "/expected/evalp/" + metric + ".csv");
        expected[metric] = xt::view(
                xt::squeeze(xt::load_csv<double>(ifs)),
                xt::newaxis(), xt::newaxis(), xt::newaxis(),
                xt::newaxis(), xt::all()
        );
        ifs.close();
    }

    return expected;
}

TEST(ProbabilistTests, TestBrier)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    std::vector<std::string> metrics = {"BS", "BSS", "BS_CRD", "BS_LBD", "REL_DIAG", "CRPS_FROM_BS"};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    metrics,
                    thresholds,
                    "high"
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        if ( metrics[m] == "REL_DIAG" )
        {
            // /!\ stacked-up thresholds in CSV file because 7D metric,
            //     so need to resize array
            expected[metrics[m]].resize(
                    {std::size_t {1}, std::size_t {1}, std::size_t {1},
                     std::size_t {1}, thresholds.shape(1),
                     predicted.shape(0) + 1, std::size_t {3}}
            );
        }
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestCDF)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    std::vector<std::string> metrics = {"CRPS_FROM_ECDF"};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    metrics
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestQuantiles)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    std::vector<std::string> metrics = {"QS", "CRPS_FROM_QS"};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    metrics
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestContingency)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    xt::xtensor<double, 2> thresholds = {{690, 534, 445, NAN}};
    std::vector<std::string> metrics = {"CONT_TBL", "POD", "POFD", "FAR", "CSI", "ROCSS"};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    metrics,
                    thresholds,
                    "low"
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        if (metrics[m] == "CONT_TBL")
        {
            // /!\ stacked-up thresholds and cells in CSV file because 7D metric,
            //     so need to resize array accordingly
            expected[metrics[m]].resize(
                {std::size_t {1}, std::size_t {1}, std::size_t {1}, std::size_t {1},
                 predicted.shape(0) + 1, thresholds.shape(1), std::size_t {4}}
            );
        }

        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-04, 1e-07, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestRanks)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();
    std::vector<std::string> metrics = {"RANK_HIST", "DS", "AS"};

    // compute scores
    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    {"RANK_HIST", "DS", "AS"},
                    xt::xtensor<double, 2>({}),
                    "high",  // events
                    {},  // c_lvl
                    xt::xtensor<bool, 4>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    xtl::missing<const std::unordered_map<std::string, int>>(),  // bootstrap
                    {}, // dts
                    7  // seed
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestIntervals)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    std::vector<std::string> metrics = {"CR", "AW", "AWN", "WS"};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    {"CR", "AW", "AWN", "WS"},
                    xt::xtensor<double, 2>({}),
                    "",  // events
                    {30., 80.}  // c_lvl
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestMultiVariate)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // read in expected results
    auto expected = load_expected_p();

    // compute scores
    std::vector<std::string> metrics = {"ES"};

    xt::xtensor<double, 2> obs = xt::repeat(
            xt::view(observed, xt::newaxis(), xt::all()), 5, 0
    );
    xt::xtensor<double, 4> prd = xt::repeat(
            xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all()), 5, 0
    );

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    // shape: (sites [5], time [t])
                    obs,
                    // shape: (sites [5], lead times [1], members [m], time [t])
                    prd,
                    metrics
            );

    // check results
    for (std::size_t m = 0; m < metrics.size(); m++)
    {
        EXPECT_TRUE(xt::all(xt::isclose(
                results[m], expected[metrics[m]], 1e-05, 1e-08, true
        ))) << "Failure for (" << metrics[m] << ")";
    }
}

TEST(ProbabilistTests, TestMasks)
{
    // read in data
    xt::xtensor<double, 1> observed;
    xt::xtensor<double, 2> predicted;
    std::tie(observed, predicted) = load_data_p();

    // generate temporal subset by dropping 20 first time steps
    xt::xtensor<bool, 4> masks =
            xt::ones<bool>({std::size_t {1}, std::size_t {1}, std::size_t {1},
                            std::size_t {observed.size()}});
    xt::view(masks, 0, xt::all(), 0, xt::range(0, 20)) = 0;

    // compute scores using masks to subset whole record
    xt::xtensor<double, 2> thresholds = {{690, 534, 445}};
    std::vector<double> confidence_levels = {30., 80.};

    std::vector<xt::xarray<double>> metrics_masked =
            evalhyd::evalp(
                    // shape: (sites [1], time [t])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    // shape: (sites [1], lead times [1], members [m], time [t])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels,
                    // shape: (sites [1], lead times [1], subsets [1], time [t])
                    masks
            );

    // compute scores on pre-computed subset of whole record
    std::vector<xt::xarray<double>> metrics_subset =
            evalhyd::evalp(
                    // shape: (sites [1], time [t-20])
                    xt::eval(xt::view(observed, xt::newaxis(), xt::range(20, _))),
                    // shape: (sites [1], lead times [1], members [m], time [t-20])
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::range(20, _))),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "masked" and "subset", which
        //     results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        EXPECT_TRUE(xt::all(xt::isclose(metrics_masked[m], metrics_subset[m], 1e-04, 1e-07, true)))
        << "Failure for (" << all_metrics_p[m] << ")";
    }
}

TEST(ProbabilistTests, TestMaskingConditions)
{
    xt::xtensor<double, 2> thresholds = {{690, 534, 445}};
    std::vector<double> confidence_levels = {30., 80.};

    // read in data
    xt::xtensor<double, 1> observed_;
    xt::xtensor<double, 2> predicted;
    std::tie(observed_, predicted) = load_data_p();

    // turn observed into 2D view (to simplify syntax later on)
    auto observed = xt::view(observed_, xt::newaxis(), xt::all());

    // generate dummy empty masks required to access next optional argument
    xt::xtensor<bool, 4> masks;

    // conditions on streamflow values _________________________________________

    // compute scores using masking conditions on streamflow to subset whole record
    xt::xtensor<std::array<char, 32>, 2> q_conditions = {
            {std::array<char, 32> {"q_obs{<2000,>3000}"}}
    };

    std::vector<xt::xarray<double>> metrics_q_conditioned =
            evalhyd::evalp(
                    xt::eval(observed),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels,
                    masks,
                    q_conditions
            );

    // compute scores using "NaN-ed" time indices where conditions on streamflow met
    std::vector<xt::xarray<double>> metrics_q_preconditioned =
            evalhyd::evalp(
                    xt::eval(xt::where((observed < 2000) | (observed > 3000), observed, NAN)),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "conditioned" and "preconditioned",
        //     which results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        EXPECT_TRUE(
                xt::all(xt::isclose(metrics_q_conditioned[m],
                                    metrics_q_preconditioned[m],
                                    1e-05, 1e-08, true))
        ) << "Failure for (" << all_metrics_p[m] << ")";
    }

    // conditions on streamflow statistics _____________________________________

    // compute scores using masking conditions on streamflow to subset whole record
    xt::xtensor<std::array<char, 32>, 2> q_conditions_ = {
            {std::array<char, 32> {"q_prd_mean{>=median}"}}
    };

    auto q_prd_mean = xt::mean(predicted, {0}, xt::keep_dims);
    double median = xt::median(q_prd_mean);

    std::vector<xt::xarray<double>> metrics_q_conditioned_ =
            evalhyd::evalp(
                    xt::eval(observed),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels,
                    masks,
                    q_conditions_
            );

    // compute scores using "NaN-ed" time indices where conditions on streamflow met
    std::vector<xt::xarray<double>> metrics_q_preconditioned_ =
            evalhyd::evalp(
                    xt::eval(xt::where(q_prd_mean >= median, observed, NAN)),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "conditioned" and "preconditioned",
        //     which results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        EXPECT_TRUE(
                xt::all(xt::isclose(metrics_q_conditioned_[m],
                                    metrics_q_preconditioned_[m],
                                    1e-05, 1e-08, true))
        ) << "Failure for (" << all_metrics_p[m] << ")";
    }

    // conditions on temporal indices __________________________________________

    // compute scores using masking conditions on time indices to subset whole record
    xt::xtensor<std::array<char, 32>, 2> t_conditions = {
            {std::array<char, 32> {"t{0,1,2,3,4,5:97,97,98,99}"}}
    };

    std::vector<xt::xarray<double>> metrics_t_conditioned =
            evalhyd::evalp(
                    xt::eval(observed),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels,
                    masks,
                    t_conditions
            );

    // compute scores on already subset time series
    std::vector<xt::xarray<double>> metrics_t_subset =
            evalhyd::evalp(
                    xt::eval(xt::view(observed_, xt::newaxis(), xt::range(0, 100))),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::range(0, 100))),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "conditioned" and "subset",
        //     which results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        EXPECT_TRUE(
                xt::all(xt::isclose(metrics_t_conditioned[m],
                                    metrics_t_subset[m],
                                    1e-05, 1e-08, true))
        ) << "Failure for (" << all_metrics_p[m] << ")";
    }
}

TEST(ProbabilistTests, TestMissingData)
{
    xt::xtensor<double, 2> thresholds = {{ 4., 5. }};
    std::vector<double> confidence_levels = {30., 80.};

    // compute metrics on series with NaN
    xt::xtensor<double, 4> forecast_nan {{
        // leadtime 1
        {{ 5.3, 4.2, 5.7, 2.3, NAN },
         { 4.3, 4.2, 4.7, 4.3, NAN },
         { 5.3, 5.2, 5.7, 2.3, NAN }},
        // leadtime 2
        {{ NAN, 4.2, 5.7, 2.3, 3.1 },
         { NAN, 4.2, 4.7, 4.3, 3.3 },
         { NAN, 5.2, 5.7, 2.3, 3.9 }}
    }};

    xt::xtensor<double, 2> observed_nan
        {{ 4.7, 4.3, NAN, 2.7, 4.1 }};

    std::vector<xt::xarray<double>> metrics_nan =
        evalhyd::evalp(
                observed_nan,
                forecast_nan,
                all_metrics_p,
                thresholds,
                "high",
                confidence_levels
        );

    // compute metrics on manually subset series (one leadtime at a time)
    xt::xtensor<double, 4> forecast_pp1 {{
        // leadtime 1
        {{ 5.3, 4.2, 2.3 },
         { 4.3, 4.2, 4.3 },
         { 5.3, 5.2, 2.3 }},
    }};

    xt::xtensor<double, 2> observed_pp1
        {{ 4.7, 4.3, 2.7 }};

    std::vector<xt::xarray<double>> metrics_pp1 =
        evalhyd::evalp(
                observed_pp1,
                forecast_pp1,
                all_metrics_p,
                thresholds,
                "high",
                confidence_levels
        );

    xt::xtensor<double, 4> forecast_pp2 {{
        // leadtime 2
        {{ 4.2, 2.3, 3.1 },
         { 4.2, 4.3, 3.3 },
         { 5.2, 2.3, 3.9 }}
    }};

    xt::xtensor<double, 2> observed_pp2
        {{ 4.3, 2.7, 4.1 }};

    std::vector<xt::xarray<double>> metrics_pp2 =
        evalhyd::evalp(
                observed_pp2,
                forecast_pp2,
                all_metrics_p,
                thresholds,
                "high",
                confidence_levels
        );

    // check that numerical results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // for leadtime 1
        EXPECT_TRUE(
                xt::all(xt::isclose(xt::view(metrics_nan[m], xt::all(), 0),
                                    xt::view(metrics_pp1[m], xt::all(), 0),
                                    1e-05, 1e-08, true))
        ) << "Failure for (" << all_metrics_p[m] << ", " << "leadtime 1)";
        
        // for leadtime 2
        EXPECT_TRUE(
                xt::all(xt::isclose(xt::view(metrics_nan[m], xt::all(), 1),
                                    xt::view(metrics_pp2[m], xt::all(), 0),
                                    1e-05, 1e-08, true))
        ) << "Failure for (" << all_metrics_p[m] << ", " << "leadtime 2)";
    }
}

TEST(ProbabilistTests, TestBootstrap)
{
    xt::xtensor<double, 2> thresholds = {{ 33.87, 55.67 }};
    std::vector<double> confidence_levels = {30., 80.};

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

    // compute metrics via bootstrap
    std::unordered_map<std::string, int> bootstrap =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 0}};

    std::vector<xt::xarray<double>> metrics_bts =
            evalhyd::evalp(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",  // events
                    confidence_levels,
                    xt::xtensor<bool, 4>({}),  // t_msk
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
            evalhyd::evalp(
                    xt::eval(xt::view(observed_x3, xt::newaxis(), xt::all())),
                    xt::eval(xt::view(predicted_x3, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",
                    confidence_levels
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "bts" and "rep", which
        //     results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        EXPECT_TRUE(
                xt::all(xt::isclose(
                        metrics_bts[m], metrics_rep[m]
                ))
        ) << "Failure for (" << all_metrics_p[m] << ")";
    }
}

TEST(ProbabilistTests, TestBootstrapSummary)
{
    xt::xtensor<double, 2> thresholds = {{ 33.87, 55.67 }};
    std::vector<double> confidence_levels = {30., 80.};

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

    // compute metrics via bootstrap
    std::unordered_map<std::string, int> bootstrap_0 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 0}};

    std::vector<xt::xarray<double>> metrics_raw =
            evalhyd::evalp(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",  // events
                    confidence_levels,
                    xt::xtensor<bool, 4>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_0,
                    datetimes
            );

    // compute metrics via bootstrap with mean and standard deviation summary
    std::unordered_map<std::string, int> bootstrap_1 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 1}};

    std::vector<xt::xarray<double>> metrics_mas =
            evalhyd::evalp(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",  // events
                    confidence_levels,
                    xt::xtensor<bool, 4>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_1,
                    datetimes
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "bts" and "rep", which
        //     results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        // mean
        EXPECT_TRUE(
                xt::all(xt::isclose(
                        xt::mean(metrics_raw[m], {3}),
                        xt::view(metrics_mas[m], xt::all(), xt::all(), xt::all(), 0)
                ))
        ) << "Failure for (" << all_metrics_p[m] << ") on mean";
        // standard deviation
        EXPECT_TRUE(
                xt::all(xt::isclose(
                        xt::stddev(metrics_raw[m], {3}),
                        xt::view(metrics_mas[m], xt::all(), xt::all(), xt::all(), 1)
                ))
        ) << "Failure for (" << all_metrics_p[m] << ") on standard deviation";
    }

    // compute metrics via bootstrap with quantiles summary
    std::unordered_map<std::string, int> bootstrap_2 =
            {{"n_samples", 10}, {"len_sample", 3}, {"summary", 2}};

    std::vector<xt::xarray<double>> metrics_qtl =
            evalhyd::evalp(
                    xt::eval(xt::view(observed, xt::newaxis(), xt::all())),
                    xt::eval(xt::view(predicted, xt::newaxis(), xt::newaxis(), xt::all(), xt::all())),
                    all_metrics_p,
                    thresholds,
                    "high",  // events
                    confidence_levels,
                    xt::xtensor<bool, 4>({}),  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    bootstrap_2,
                    datetimes
            );

    // check results are identical
    for (std::size_t m = 0; m < all_metrics_p.size(); m++)
    {
        // ---------------------------------------------------------------------
        // /!\ skip ranks-based metrics because it contains a random process
        //     for which setting the seed will not work because the time series
        //     lengths are different between "bts" and "rep", which
        //     results in different tensor shapes, and hence in different
        //     random ranks for ties
        if ((all_metrics_p[m] == "RANK_HIST")
            || (all_metrics_p[m] == "DS")
            || (all_metrics_p[m] == "AS"))
        {
            continue;
        }
        // ---------------------------------------------------------------------

        // quantiles
        std::vector<double> quantiles = {0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95};
        std::size_t i = 0;

        for (auto q : quantiles)
        {
            EXPECT_TRUE(
                    xt::all(xt::isclose(
                            xt::quantile(metrics_raw[m], {q}, 3),
                            xt::view(metrics_qtl[m], xt::all(), xt::all(), xt::all(), i)
                    ))
            ) << "Failure for (" << all_metrics_p[m] << ") on quantile " << q;
            i++;
        }
    }
}

TEST(ProbabilistTests, TestCompleteness)
{
    std::vector<std::string> diags = {"completeness"};

    // compute metrics on series with NaN
    xt::xtensor<double, 4> prd = {{
            // leadtime 1
            {{ 5.3, NAN, 5.7, 2.3, 3.3, NAN },
             { 4.3, NAN, 4.7, 4.3, 3.4, NAN },
             { 5.3, NAN, 5.7, 2.3, 3.8, NAN }},
            // leadtime 2
            {{ NAN, 4.2, 5.7, 2.3, 3.1, 4.1 },
             { NAN, 4.2, 4.7, 4.3, 3.3, 2.8 },
             { NAN, 5.2, 5.7, 2.3, 3.9, 3.5 }}
    }};

    xt::xtensor<double, 2> obs =
            {{ 4.7, 4.3, NAN, 2.7, 4.1, 5.0 }};

    xt::xtensor<bool, 4> msk = {{
            // leadtime 1
            {{ true, true, true, false, true, true },
             { true, true, true, true, true, true  }},
            // leadtime 2
            {{ true, true, true, true, true, false },
             { true, true, true, true, true, true  }},
    }};

    std::vector<xt::xarray<double>> results =
            evalhyd::evalp(
                    obs,
                    prd,
                    std::vector<std::string> {},  // metrics
                    xt::xtensor<double, 2>({}),  // thresholds
                    xtl::missing<const std::string>(),  // events
                    {},
                    msk,  // t_msk
                    xt::xtensor<std::array<char, 32>, 2>({}),  // m_cdt
                    xtl::missing<const std::unordered_map<std::string, int>>(),  // bootstrap
                    {},  // dts
                    xtl::missing<const int>(),  // seed
                    diags
            );

    // check that numerical results are identical
    xt::xtensor<double, 4> expected = {{
            // leadtime 1
            {{ 2. },
             { 3. }},
            // leadtime 2
            {{ 3. },
             { 4. }},
    }};

    EXPECT_TRUE(
            xt::all(xt::isclose(results[0], expected, 1e-05, 1e-08, true))
    );
}

