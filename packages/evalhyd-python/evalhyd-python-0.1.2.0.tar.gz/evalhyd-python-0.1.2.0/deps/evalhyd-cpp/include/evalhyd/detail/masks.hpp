// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_MASKS_HPP
#define EVALHYD_MASKS_HPP

#include <map>
#include <set>
#include <vector>
#include <array>
#include <string>
#include <regex>
#include <stdexcept>

#include <xtensor/xexpression.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xindex_view.hpp>


typedef std::map<std::string, std::vector<std::vector<std::string>>> msk_tree;

namespace evalhyd
{
    namespace masks
    {
        /// Function to parse a string containing masking conditions.
        inline msk_tree parse_masking_conditions(std::string msk_str)
        {
            msk_tree subset;

            // pattern supported to specify conditions to generate masks on
            // observed or predicted (median or mean for probabilist) streamflow
            // e.g. q{>9.} q{<9} q{>=99.0} q{<=99} q{>9,<99} q{==9} q{!=9}
            std::regex exp_q (
                    R"((q_obs|q_prd_median|q_prd_mean)\{(((<|>|<=|>=|==|!=)(mean,?|median,?|qtl(0|1)\.(0|1|2|3|4|5|6|7|8|9)+,?|(0|1|2|3|4|5|6|7|8|9)+\.?(0|1|2|3|4|5|6|7|8|9)*,?))+)\})"
                    // NOTE: this should be `R"((q_obs|q_prd_median|q_prd_mean)\{(((<|>|<=|>=|==|!=)(mean,?|median,?|qtl[0-1]\.[0-9]+,?|[0-9]+\.?[0-9]*,?))+)\})"`
                    //       but there is a bug in the building chain for R packages
                    //       https://gitlab.irstea.fr/HYCAR-Hydro/evalhyd/evalhyd-r/-/issues/6
            );

            for (std::sregex_iterator i =
                    std::sregex_iterator(msk_str.begin(), msk_str.end(), exp_q);
                 i != std::sregex_iterator(); i++)
            {
                const std::smatch & mtc = *i;

                std::string var = mtc[1];
                std::string str = mtc[2];

                // process masking conditions on streamflow
                std::vector<std::vector<std::string>> conditions;

                // pattern supported to specify masking conditions based on streamflow
                std::regex ex (
                        R"((<|>|<=|>=|==|!=)(mean|median|qtl(0|1)\.(0|1|2|3|4|5|6|7|8|9)+|(0|1|2|3|4|5|6|7|8|9)+\.?(0|1|2|3|4|5|6|7|8|9)*))"
                        // NOTE: this should be `R"((<|>|<=|>=|==|!=)(mean|median|qtl[0-1]\.[0-9]+|[0-9]+\.?[0-9]*))"`
                        //       but there is a bug in the building chain for R packages
                        //       https://gitlab.irstea.fr/HYCAR-Hydro/evalhyd/evalhyd-r/-/issues/6
                );

                for (std::sregex_iterator j =
                        std::sregex_iterator(str.begin(), str.end(), ex);
                     j != std::sregex_iterator(); j++)
                {
                    const std::smatch & mt = *j;

                    if ((mt[2].str() == "median")
                        || (mt[2].str() == "mean"))
                    {
                        conditions.push_back({mt[1].str(), mt[2].str(), ""});
                    }
                    else if ((mt[2].str().length() >= 3)
                             && (mt[2].str().substr(0, 3) == "qtl"))
                    {
                        conditions.push_back(
                            {mt[1].str(), "qtl", mt[2].str().substr(3)}
                        );
                    }
                    else
                    {
                        // it is a simple numerical value
                        conditions.push_back({mt[1].str(), "", mt[2].str()});
                    }
                }

                // check that a maximum of two conditions were provided
                if (conditions.size() > 2)
                {
                    throw std::runtime_error(
                            "no more than two streamflow masking conditions "
                            "can be provided"
                    );
                }

                subset[var] = conditions;
            }

            // pattern supported to specify conditions to generate masks on time index
            // e.g. t{0:10} t{0:10,20:30} t{0,1,2,3} t{0:10,30,40,50} t{:}
            std::regex exp_t (
                    R"((t)\{(:|((0|1|2|3|4|5|6|7|8|9)+:(0|1|2|3|4|5|6|7|8|9)+,?|(0|1|2|3|4|5|6|7|8|9)+,?)+)\})"
                    // NOTE: this should be `R"((t)\{(:|([0-9]+:[0-9]+,?|[0-9]+,?)+)\})"`
                    //       but there is a bug in the building chain for R packages
                    //       https://gitlab.irstea.fr/HYCAR-Hydro/evalhyd/evalhyd-r/-/issues/6
            );

            for (std::sregex_iterator i =
                    std::sregex_iterator(msk_str.begin(), msk_str.end(), exp_t);
                 i != std::sregex_iterator(); i++)
            {
                const std::smatch & mtc = *i;

                std::string var = mtc[1];
                std::string s = mtc[2];

                // process masking conditions on time index
                std::vector<std::vector<std::string>> condition;

                // check whether it is all indices (i.e. t{:})
                if (s == ":")
                {
                    condition.emplace_back();
                }
                else
                {
                    // pattern supported to specify masking conditions based on time index
                    std::regex e (
                            R"((0|1|2|3|4|5|6|7|8|9)+:(0|1|2|3|4|5|6|7|8|9)+|(0|1|2|3|4|5|6|7|8|9)+)"
                            // NOTE: this should be `R"([0-9]+:[0-9]+|[0-9]+)"`
                            //       but there is a bug in the building chain for R packages
                            //       https://gitlab.irstea.fr/HYCAR-Hydro/evalhyd/evalhyd-r/-/issues/6
                    );

                    for (std::sregex_iterator j =
                            std::sregex_iterator(s.begin(), s.end(), e);
                         j != std::sregex_iterator(); j++)
                    {
                        const std::smatch & m = *j;

                        // check whether it is a range of indices, or an index
                        if (m[0].str().find(':') != std::string::npos)
                        {
                            // it is a range of indices (i.e. t{#:#})
                            std::string s_ = m[0].str();
                            std::string beg = s_.substr(0, s_.find(':'));
                            std::string end = s_.substr(s_.find(':') + 1);

                            // generate sequence of integer indices from range
                            std::vector<int> vi(std::stoi(end) - std::stoi(beg));
                            std::iota(vi.begin(), vi.end(), std::stoi(beg));
                            // convert to sequence of integer indices to string indices
                            std::vector<std::string> vs;
                            std::transform(std::begin(vi), std::end(vi),
                                           std::back_inserter(vs),
                                           [](int d) { return std::to_string(d); });

                            condition.push_back(vs);
                        }
                        else
                        {
                            // it is an index (i.e. t{#})
                            condition.push_back({m[0].str()});
                        }
                    }
                }

                subset[var] = condition;
            }

            return subset;
        }

        /// Function to generate temporal mask based on masking conditions
        template<class X1, class X2>
        inline xt::xtensor<bool, 1> generate_mask_from_conditions(
                const std::array<char, 32>& msk_char_arr,
                const X1& q_obs,
                const X2& q_prd
        )
        {
            // parse string to identify masking conditions
            std::string msk_str(msk_char_arr.begin(), msk_char_arr.end());
            msk_tree subset = parse_masking_conditions(msk_str);

            // check if conditions were found in parsing
            if (subset.empty())
            {
                throw std::runtime_error(
                        "no valid condition found to generate mask(s)"
                );
            }

            // initialise a boolean expression for the masks
            xt::xtensor<bool, 1> t_msk = xt::zeros<bool>(q_obs.shape());

            // populate the masks given the conditions
            for (const auto & var_cond : subset)
            {
                auto var = var_cond.first;
                auto cond = var_cond.second;

                // condition on streamflow
                if ((var == "q_obs") || (var == "q_prd_median")
                    || (var == "q_prd_mean"))
                {
                    // preprocess streamflow depending on kind
                    auto get_q = [&]() {
                        if (var == "q_obs")
                        {
                            return xt::xtensor<double, 1>(q_obs);
                        }
                        else if (var == "q_prd_median")
                        {
                            if (q_prd.shape(0) == 1)
                            {
                                throw std::runtime_error(
                                        "condition on streamflow predictions "
                                        "not allowed for generating masks"
                                );
                            }
                            xt::xtensor<double, 1> q_prd_median =
                                    xt::median(q_prd, 0);
                            return q_prd_median;
                        }
                        else
                        {
                            // i.e. (var == "q_prd_mean")
                            if (q_prd.shape(0) == 1)
                            {
                                throw std::runtime_error(
                                        "condition on streamflow predictions "
                                        "not allowed for generating masks"
                                );
                            }
                            xt::xtensor<double, 1> q_prd_mean =
                                    xt::mean(q_prd, 0);
                            return q_prd_mean;
                        }
                    };
                    auto q = get_q();

                    // define lambda function to precompute mean/median/quantile
                    auto get_val =
                            [&](const std::string& str, const std::string& num)
                    {
                        if (str.empty())  // it is a simple numerical value
                        {
                            return std::stod(num);
                        }
                        else
                        {
                            auto q_filtered = xt::filter(q, !xt::isnan(q));

                            if (q_filtered.size() > 0)
                            {
                                if (str == "median")
                                {
                                    return xt::median(q_filtered);
                                }
                                else if (str == "mean")
                                {
                                    return xt::mean(q_filtered)();
                                }
                                else  // (str == "qtl")
                                {
                                    return xt::quantile(q_filtered, {std::stod(num)})();
                                }
                            }
                            else
                            {
                                return double(NAN);
                            }
                        }
                    };

                    // preprocess conditions to identify special cases
                    // within/without
                    bool within = false;
                    bool without = false;

                    std::string opr1, opr2;
                    double val1, val2;

                    if (cond.size() == 2)
                    {
                        opr1 = cond[0][0];
                        val1 = get_val(cond[0][1], cond[0][2]);
                        opr2 = cond[1][0];
                        val2 = get_val(cond[1][1], cond[1][2]);

                        if ((opr1 == "<") || (opr1 == "<="))
                        {
                            if ((opr2 == ">") || (opr2 == ">="))
                            {
                                if (val2 > val1)
                                {
                                    without = true;
                                }
                                else
                                {
                                    within = true;
                                }
                            }
                        }
                        else if ((opr1 == ">") || (opr1 == ">="))
                        {
                            if ((opr2 == "<") || (opr2 == "<="))
                            {
                                if (val2 > val1)
                                {
                                    within = true;
                                }
                                else
                                {
                                    without = true;
                                }
                            }
                        }
                    }

                    // process conditions, starting with special cases
                    // within/without
                    if (within)
                    {
                        if ((opr1 == "<") && (opr2 == ">"))
                        {
                            t_msk = xt::where((q < val1) && (q > val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<=") && (opr2 == ">"))
                        {
                            t_msk = xt::where((q <= val1) && (q > val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<") && (opr2 == ">="))
                        {
                            t_msk = xt::where((q < val1) && (q >= val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<=") && (opr2 == ">="))
                        {
                            t_msk = xt::where((q <= val1) && (q >= val2),
                                              1, t_msk);
                        }

                        if ((opr2 == "<") && (opr1 == ">"))
                        {
                            t_msk = xt::where((q < val2) && (q > val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<=") && (opr1 == ">"))
                        {
                            t_msk = xt::where((q <= val2) && (q > val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<") && (opr1 == ">="))
                        {
                            t_msk = xt::where((q < val2) && (q >= val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<=") && (opr1 == ">="))
                        {
                            t_msk = xt::where((q <= val2) && (q >= val1),
                                              1, t_msk);
                        }
                    }
                    else if (without)
                    {
                        if ((opr1 == "<") && (opr2 == ">"))
                        {
                            t_msk = xt::where((q < val1) || (q > val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<=") && (opr2 == ">"))
                        {
                            t_msk = xt::where((q <= val1) || (q > val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<") && (opr2 == ">="))
                        {
                            t_msk = xt::where((q < val1) || (q >= val2),
                                              1, t_msk);
                        }
                        else if ((opr1 == "<=") && (opr2 == ">="))
                        {
                            t_msk = xt::where((q <= val1) && (q >= val2),
                                              1, t_msk);
                        }

                        if ((opr2 == "<") && (opr1 == ">"))
                        {
                            t_msk = xt::where((q < val2) || (q > val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<=") && (opr1 == ">"))
                        {
                            t_msk = xt::where((q <= val2) || (q > val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<") && (opr1 == ">="))
                        {
                            t_msk = xt::where((q < val2) || (q >= val1),
                                              1, t_msk);
                        }
                        else if ((opr2 == "<=") && (opr1 == ">="))
                        {
                            t_msk = xt::where((q <= val2) || (q >= val1),
                                              1, t_msk);
                        }
                    }
                    else
                    {
                        for (const auto & opr_val : cond)
                        {
                            auto opr = opr_val[0];
                            double val = get_val(opr_val[1], opr_val[2]);

                            // apply masking condition to given subset
                            if (opr == "<")
                            {
                                t_msk = xt::where(
                                        q < val, 1, t_msk
                                );
                            }
                            else if (opr == ">")
                            {
                                t_msk = xt::where(
                                        q > val, 1, t_msk
                                );
                            }
                            else if (opr == "<=")
                            {
                                t_msk = xt::where(
                                        q <= val, 1, t_msk
                                );
                            }
                            else if (opr == ">=")
                            {
                                t_msk = xt::where(
                                        q >= val, 1, t_msk
                                );
                            }
                            else if (opr == "==")
                            {
                                t_msk = xt::where(
                                        xt::equal(q, val), 1, t_msk
                                );
                            }
                            else if (opr == "!=")
                            {
                                t_msk = xt::where(
                                        xt::not_equal(q, val), 1, t_msk
                                );
                            }
                        }
                    }
                }
                // condition on time index
                else if (var == "t")
                {
                    for (const auto & sequence : cond)
                    {
                        if (sequence.empty())
                        {
                            // i.e. t{:}
                            xt::view(t_msk, xt::all()) = 1;
                        }
                        else
                        {
                            // convert string indices to integer indices
                            std::vector<int> vi;
                            std::transform(std::begin(sequence),
                                           std::end(sequence),
                                           std::back_inserter(vi),
                                           [](const std::string& s)
                                           { return std::stoi(s); });
                            // apply masked indices to given subset
                            xt::index_view(t_msk, vi) = 1;
                        }
                    }
                }
            }

            return t_msk;
        }
    }
}

#endif //EVALHYD_MASKS_HPP
