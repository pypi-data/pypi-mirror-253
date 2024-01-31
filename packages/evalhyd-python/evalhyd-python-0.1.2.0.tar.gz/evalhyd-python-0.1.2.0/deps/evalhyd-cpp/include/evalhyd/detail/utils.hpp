// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_UTILS_HPP
#define EVALHYD_UTILS_HPP

#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <stdexcept>

#include <xtl/xoptional.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xrandom.hpp>


namespace evalhyd
{
    namespace utils
    {
        // Procedure to check that all elements in the list of metrics are
        // valid metrics.
        //
        // \param requested_metrics
        //     Vector of strings for the metric(s) to be computed.
        // \param valid_metrics
        //     Vector of strings for the metric(s) to can be computed.
        inline void check_metrics (
                const std::vector<std::string>& requested_metrics,
                const std::vector<std::string>& valid_metrics
        )
        {
            for (const auto& metric : requested_metrics)
            {
                if (std::find(valid_metrics.begin(), valid_metrics.end(), metric)
                        == valid_metrics.end())
                {
                    throw std::runtime_error(
                            "invalid evaluation metric: " + metric
                    );
                }
            }
        }

        // Procedure to check that all elements in the list of diagnostics are
        // valid diagnostics.
        //
        // \param requested_diags
        //     Vector of strings for the diagnostic(s) to be computed.
        // \param valid_diags
        //     Vector of strings for the diagnostic(s) to can be computed.
        inline void check_diags (
                const std::vector<std::string>& requested_diags,
                const std::vector<std::string>& valid_diags
        )
        {
            for (const auto& diag : requested_diags)
            {
                if (std::find(valid_diags.begin(), valid_diags.end(), diag)
                    == valid_diags.end())
                {
                    throw std::runtime_error(
                            "invalid evaluation diagnostic: " + diag
                    );
                }
            }
        }

        // Procedure to check that all elements for a bootstrap experiment
        // are provided and valid.
        //
        // \param bootstrap
        //     Map of parameters for the bootstrap experiment.
        inline void check_bootstrap (
                const std::unordered_map<std::string, int>& bootstrap
        )
        {
            // check n_samples
            if (bootstrap.find("n_samples") == bootstrap.end())
            {
                throw std::runtime_error(
                        "number of samples missing for bootstrap"
                );
            }
            auto n_samples = bootstrap.find("n_samples")->second;
            if (n_samples < 1)
            {
                throw std::runtime_error(
                        "number of samples must be greater than zero"
                );
            }
            // check len_sample
            if (bootstrap.find("len_sample") == bootstrap.end())
            {
                throw std::runtime_error(
                        "length of sample missing for bootstrap"
                );
            }
            auto len_sample = bootstrap.find("len_sample")->second;
            if (len_sample < 1)
            {
                throw std::runtime_error(
                        "length of sample must be greater than zero"
                );
            }
            // check summary
            if (bootstrap.find("summary") == bootstrap.end())
            {
                throw std::runtime_error(
                        "summary missing for bootstrap"
                );
            }
            auto summary = bootstrap.find("summary")->second;
            if ((summary < 0) || (summary > 2))
            {
                throw std::runtime_error(
                        "invalid value for bootstrap summary"
                );
            }
        }

        // Function to get a seed for random generators
        //
        // \param seed
        //     Optional value to use to set the seed for random generators.
        // \return
        //     A seed value to use in random generators.
        inline long int get_seed(xtl::xoptional<int, bool> seed)
        {
            if (seed.has_value())
            {
                return seed.value();
            }
            else
            {
                return std::time(nullptr);
            }
        }
    }
}

#endif //EVALHYD_UTILS_HPP
