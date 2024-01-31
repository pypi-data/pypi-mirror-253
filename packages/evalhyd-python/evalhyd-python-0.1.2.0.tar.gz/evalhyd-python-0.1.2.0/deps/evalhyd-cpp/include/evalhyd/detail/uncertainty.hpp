// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_UNCERTAINTY_HPP
#define EVALHYD_UNCERTAINTY_HPP

#include <string>
#include <vector>
#include <array>
#include <ctime>
#include <chrono>
#include <iomanip>
#include <stdexcept>

#include <xtensor/xtensor.hpp>
#include <xtensor/xadapt.hpp>
#include <xtensor/xrandom.hpp>
#include <xtensor/xsort.hpp>


typedef std::chrono::time_point<
        std::chrono::system_clock, std::chrono::minutes
> tp_minutes;

namespace evalhyd
{
    namespace uncertainty
    {
        inline auto bootstrap(
                const std::vector<std::string>& datetimes,
                int n_samples, int len_sample, long int seed
        )
        {
            // convert string to time_point (via tm)
            std::vector<std::tm> v_tm;
            std::vector<tp_minutes> v_timepoints;

            for (auto const& str: datetimes)
            {
                // convert string to tm
                std::tm tm = {};
                std::istringstream ss(str);
                ss >> std::get_time(&tm, "%Y-%m-%d %H:%M:%S");
                if (ss.fail())
                {
                    throw std::runtime_error("datetime string parsing failed");
                }
                tm.tm_year += 400; // add 400y to avoid dates prior 1970
                                   // while preserving leap year pattern
                v_tm.push_back(tm);

                // convert tm to time_point
                auto tp = std::chrono::system_clock::from_time_t(std::mktime(&tm));
                v_timepoints.push_back(
                        std::chrono::time_point_cast<std::chrono::minutes>(tp)
                );
            }

            // adapt vector into xtensor
            xt::xtensor<tp_minutes, 1> x_timepoints = xt::adapt(v_timepoints);

            // check constant time interval
            auto ti = x_timepoints[1] - x_timepoints[0];
            for (std::size_t t = 1; t < x_timepoints.size() - 1; t++)
            {
                if (x_timepoints[t + 1] - x_timepoints[t] != ti)
                {
                    throw std::runtime_error(
                            "time interval not constant across datetimes"
                    );
                }
            }

            // identify start and end years for period
            int start_yr = v_tm.front().tm_year + 1900;
            int end_yr = v_tm.back().tm_year + 1900;

            // deal with special case with a start on 1st of January
            // (note: use string rather than *tm_yday* member of time_point
            //  because *tm_yday* is not set when using `std::get_time`)
            if (datetimes[0].substr(5, 5) == "01-01")
            {
                // add one year to make sure last year is included in loop
                end_yr += 1;
            }

            // take start of year block as start of time series
            std::tm start_hy = v_tm.front();

            xt::xtensor<int, 1> year_blocks = xt::zeros<int>({v_tm.size()});
            for (int y = start_yr; y < end_yr; y++)
            {
                // define window for year blocks
                start_hy.tm_year = y - 1900;
                auto start = std::chrono::system_clock::from_time_t(
                        std::mktime(&start_hy)
                );
                start_hy.tm_year += 1;
                auto end = std::chrono::system_clock::from_time_t(
                        std::mktime(&start_hy)
                );

                xt::xtensor<bool, 1> wdw =
                        (x_timepoints >= start) && (x_timepoints < end);

                // check that year is complete (without a rigorous leap year check)
                bool complete_yr = true;
                if (std::chrono::minutes(ti).count() == 1)
                {
                    // minute timestep
                    int n_minutes = xt::sum(wdw)();
                    if ((n_minutes != 60 * 24 * 365) && (n_minutes != 60 * 24 * 366))
                    {
                        complete_yr = false;
                    }
                }
                else if (std::chrono::minutes(ti).count() == 60)
                {
                    // hourly timestep
                    int n_hours = xt::sum(wdw)();
                    if ((n_hours != 24 * 365) && (n_hours != 24 * 366))
                    {
                        complete_yr = false;
                    }
                }
                else if (std::chrono::minutes(ti).count() == 60 * 24)
                {
                    // daily timestep
                    int n_days = xt::sum(wdw)();
                    if ((n_days != 365) && (n_days != 366))
                    {
                        complete_yr = false;
                    }
                }
                else
                {
                    throw std::runtime_error(
                            "time step must be minute, hourly, or daily"
                    );
                }
                if (!complete_yr)
                {
                    throw std::runtime_error(
                            "year starting in " + std::to_string(y - 400)
                            + " is incomplete"
                    );
                }

                // determine corresponding year block for each time step
                year_blocks = xt::where(wdw, y, year_blocks);
            }

            // check that time series ends on the last day of a year block
            if (year_blocks(year_blocks.size() - 1) == 0)
            {
                throw std::runtime_error(
                        "final day of final year not equal to first day of "
                        "first year minus one time step"
                );
            }

            // generate bootstrapping experiment
            xt::random::seed(seed);
            xt::xtensor<int, 2> experiment = xt::random::randint(
                    {n_samples, len_sample}, start_yr, end_yr
            );

            std::vector<xt::xkeep_slice<int>> samples;

            // compute metrics for each sample
            for (int s = 0; s < n_samples; s++)
            {
                // select bootstrapped years
                auto exp = xt::view(experiment, s);

                auto i0 = xt::flatten_indices(
                        xt::argwhere(xt::equal(year_blocks, exp(0)))
                );
                auto i1 = xt::flatten_indices(
                        xt::argwhere(xt::equal(year_blocks, exp(1)))
                );
                xt::xtensor<int, 1> idx = xt::concatenate(xt::xtuple(i0, i1), 0);

                for (std::size_t p = 2; p < exp.size(); p++)
                {
                    auto i = xt::flatten_indices(
                            xt::argwhere(xt::equal(year_blocks, exp(p)))
                    );
                    idx = xt::concatenate(xt::xtuple(idx, i), 0);
                }

                samples.push_back(xt::keep(idx));
            }

            return samples;
        }
        
        inline auto summarise_d(const xt::xarray<double>& values, int summary)
        {
            // define axis along which samples are
            std::size_t axis = 2;

            // determine shape for output values
            std::vector<std::size_t> shp;
            std::size_t i = 0;
            for (auto a : values.shape())
            {
                if (i != axis)
                {
                    shp.push_back(a);
                }
                else
                {
                    if (summary == 1)
                    {
                        shp.push_back(2);
                    }
                    else if (summary == 2)
                    {
                        shp.push_back(7);
                    }
                }
                i++;
            }

            // summary 2: series of quantiles across samples
            if (summary == 2)
            {
                xt::xarray<double> v = xt::zeros<double>(shp);

                // compute quantiles
                auto quantiles = xt::quantile(
                        values,
                        {0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95},
                        axis
                );

                // transfer quantiles into correct axis
                // (since xt::quantile puts the quantiles on the first axis)
                for (std::size_t q = 0; q < 7; q++)
                {
                    xt::view(v, xt::all(), xt::all(), q) =
                            xt::view(quantiles, q);
                }

                return v;
            }
            // summary 1: mean and standard deviation across samples
            else if (summary == 1)
            {
                xt::xarray<double> v = xt::zeros<double>(shp);

                // compute mean
                xt::view(v, xt::all(), xt::all(), 0) =
                        xt::mean(values, {2});
                // compute standard deviation
                xt::view(v, xt::all(), xt::all(), 1) =
                        xt::stddev(values, {2});

                return v;
            }
            // summary 0: raw (keep all samples)
            else
            {
                return values;
            }
        }

        inline auto summarise_p(const xt::xarray<double>& values, int summary)
        {
            // define axis along which samples are
            std::size_t axis = 3;

            // determine shape for output values
            std::vector<std::size_t> shp;
            std::size_t i = 0;
            for (auto a : values.shape())
            {
                if (i != axis)
                {
                    shp.push_back(a);
                }
                else
                {
                    if (summary == 1)
                    {
                        shp.push_back(2);
                    }
                    else if (summary == 2)
                    {
                        shp.push_back(7);
                    }
                }
                i++;
            }

            // summary 2: series of quantiles across samples
            if (summary == 2)
            {
                xt::xarray<double> v = xt::zeros<double>(shp);

                // compute quantiles
                auto quantiles = xt::quantile(
                        values,
                        {0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95},
                        axis
                );

                // transfer quantiles into correct axis
                // (since xt::quantile puts the quantiles on the first axis)
                for (std::size_t q = 0; q < 7; q++)
                {
                    xt::view(v, xt::all(), xt::all(), xt::all(), q) =
                            xt::view(quantiles, q);
                }

                return v;
            }
            // summary 1: mean and standard deviation across samples
            else if (summary == 1)
            {
                xt::xarray<double> v = xt::zeros<double>(shp);

                // compute mean
                xt::view(v, xt::all(), xt::all(), xt::all(), 0) =
                        xt::mean(values, {axis});
                // compute standard deviation
                xt::view(v, xt::all(), xt::all(), xt::all(), 1) =
                        xt::stddev(values, {axis});

                return v;
            }
            // summary 0: raw (keep all samples)
            else
            {
                return values;
            }
        }
    }
}

#endif //EVALHYD_UNCERTAINTY_HPP
