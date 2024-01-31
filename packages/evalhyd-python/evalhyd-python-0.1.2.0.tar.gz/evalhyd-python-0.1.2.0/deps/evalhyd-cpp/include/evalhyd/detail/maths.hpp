// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_MATHS_HPP
#define EVALHYD_MATHS_HPP

#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xbuilder.hpp>
#include <xtensor/xutils.hpp>

#include <cmath>

namespace evalhyd
{
    namespace maths
    {
        // TODO: substitute with `xt::stddev` when performance fixed
        //       (see https://github.com/xtensor-stack/xtensor/pull/2656)
        // function to calculate standard deviation on last axis of n-dim expressions
        template <class A1, class A2>
        inline auto nanstd(A1&& arr, A2&& mean_arr)
        {
            return xt::sqrt(
                    xt::nanmean(xt::square(xt::abs(arr - mean_arr)), -1)
            );
        }
    }
}

#endif //EVALHYD_MATHS_HPP
