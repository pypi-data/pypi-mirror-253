// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_DETERMINIST_EVALUATOR_HPP
#define EVALHYD_DETERMINIST_EVALUATOR_HPP

#include <vector>

#include <xtl/xoptional.hpp>
#include <xtensor/xexpression.hpp>
#include <xtensor/xtensor.hpp>

#include "diagnostics.hpp"
#include "errors.hpp"
#include "efficiencies.hpp"
#include "events.hpp"


namespace evalhyd
{
    namespace determinist
    {
        template <class XD2, class XB3>
        class Evaluator
        {
        private:
            // members for input data
            const XD2& q_obs;
            const XD2& q_prd;
            // members for optional input data
            const XD2& _q_thr;
            xtl::xoptional<const std::string, bool> _events;
            xt::xtensor<bool, 3> t_msk;
            const std::vector<xt::xkeep_slice<int>>& b_exp;

            // members for dimensions
            std::size_t n_tim;
            std::size_t n_msk;
            std::size_t n_srs;
            std::size_t n_thr;
            std::size_t n_exp;

            // members for computational elements
            xtl::xoptional<xt::xtensor<double, 3>, bool> t_counts;
            xtl::xoptional<xt::xtensor<double, 4>, bool> mean_obs;
            xtl::xoptional<xt::xtensor<double, 4>, bool> mean_prd;
            xtl::xoptional<xt::xtensor<double, 2>, bool> err;
            xtl::xoptional<xt::xtensor<double, 2>, bool> abs_err;
            xtl::xoptional<xt::xtensor<double, 2>, bool> quad_err;
            xtl::xoptional<xt::xtensor<double, 4>, bool> err_obs;
            xtl::xoptional<xt::xtensor<double, 4>, bool> quad_err_obs;
            xtl::xoptional<xt::xtensor<double, 4>, bool> err_prd;
            xtl::xoptional<xt::xtensor<double, 4>, bool> quad_err_prd;
            xtl::xoptional<xt::xtensor<double, 3>, bool> r_pearson;
            xtl::xoptional<xt::xtensor<double, 3>, bool> r_spearman;
            xtl::xoptional<xt::xtensor<double, 3>, bool> alpha;
            xtl::xoptional<xt::xtensor<double, 3>, bool> gamma;
            xtl::xoptional<xt::xtensor<double, 3>, bool> alpha_np;
            xtl::xoptional<xt::xtensor<double, 3>, bool> bias;
            xtl::xoptional<xt::xtensor<double, 3>, bool> obs_event;
            xtl::xoptional<xt::xtensor<double, 3>, bool> prd_event;
            xtl::xoptional<xt::xtensor<double, 3>, bool> ct_a;
            xtl::xoptional<xt::xtensor<double, 3>, bool> ct_b;
            xtl::xoptional<xt::xtensor<double, 3>, bool> ct_c;
            xtl::xoptional<xt::xtensor<double, 3>, bool> ct_d;

            // members for evaluation metrics
            xtl::xoptional<xt::xtensor<double, 3>, bool> MAE;
            xtl::xoptional<xt::xtensor<double, 3>, bool> MARE;
            xtl::xoptional<xt::xtensor<double, 3>, bool> MSE;
            xtl::xoptional<xt::xtensor<double, 3>, bool> RMSE;
            xtl::xoptional<xt::xtensor<double, 3>, bool> NSE;
            xtl::xoptional<xt::xtensor<double, 3>, bool> KGE;
            xtl::xoptional<xt::xtensor<double, 4>, bool> KGE_D;
            xtl::xoptional<xt::xtensor<double, 3>, bool> KGEPRIME;
            xtl::xoptional<xt::xtensor<double, 4>, bool> KGEPRIME_D;
            xtl::xoptional<xt::xtensor<double, 3>, bool> KGENP;
            xtl::xoptional<xt::xtensor<double, 4>, bool> KGENP_D;
            xtl::xoptional<xt::xtensor<double, 5>, bool> CONT_TBL;

            // methods to get optional parameters
            auto get_q_thr()
            {
                if (_q_thr.size() < 1)
                {
                    throw std::runtime_error(
                            "threshold-based metric requested, "
                            "but *q_thr* not provided"
                    );
                }
                else{
                    return _q_thr;
                }
            }

            bool is_high_flow_event()
            {
                if (_events.has_value())
                {
                    if (_events.value() == "high")
                    {
                        return true;
                    }
                    else if (_events.value() == "low")
                    {
                        return false;
                    }
                    else
                    {
                        throw std::runtime_error(
                                "invalid value for *events*: " + _events.value()
                        );
                    }
                }
                else
                {
                    throw std::runtime_error(
                            "threshold-based metric requested, "
                            "but *events* not provided"
                    );
                }
            }

            // methods to compute elements
            xt::xtensor<double, 3> get_t_counts()
            {
                if (!t_counts.has_value())
                {
                    t_counts = elements::calc_t_counts(
                            t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return t_counts.value();
            };

            xt::xtensor<double, 4> get_mean_obs()
            {
                if (!mean_obs.has_value())
                {
                    mean_obs = elements::calc_mean_obs(
                            q_obs, t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return mean_obs.value();
            };

            xt::xtensor<double, 4> get_mean_prd()
            {
                if (!mean_prd.has_value())
                {
                    mean_prd = elements::calc_mean_prd(
                            q_prd, t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return mean_prd.value();
            };

            xt::xtensor<double, 2> get_err()
            {
                if (!err.has_value())
                {
                    err = elements::calc_err(
                            q_obs, q_prd
                    );
                }
                return err.value();
            };

            xt::xtensor<double, 2> get_abs_err()
            {
                if (!abs_err.has_value())
                {
                    abs_err = elements::calc_abs_err(
                            get_err()
                    );
                }
                return abs_err.value();
            };

            xt::xtensor<double, 2> get_quad_err()
            {
                if (!quad_err.has_value())
                {
                    quad_err = elements::calc_quad_err(
                            get_err()
                    );
                }
                return quad_err.value();
            };

            xt::xtensor<double, 4> get_err_obs()
            {
                if (!err_obs.has_value())
                {
                    err_obs = elements::calc_err_obs(
                            q_obs, get_mean_obs(), t_msk,
                            n_srs, n_tim, n_msk, n_exp
                    );
                }
                return err_obs.value();
            };

            xt::xtensor<double, 4> get_quad_err_obs()
            {
                if (!quad_err_obs.has_value())
                {
                    quad_err_obs = elements::calc_quad_err_obs(
                            get_err_obs()
                    );
                }
                return quad_err_obs.value();
            };

            xt::xtensor<double, 4> get_err_prd()
            {
                if (!err_prd.has_value())
                {
                    err_prd = elements::calc_err_prd(
                            q_prd, get_mean_prd(), t_msk,
                            n_srs, n_tim, n_msk, n_exp
                    );
                }
                return err_prd.value();
            };

            xt::xtensor<double, 4> get_quad_err_prd()
            {
                if (!quad_err_prd.has_value())
                {
                    quad_err_prd = elements::calc_quad_err_prd(
                            get_err_prd()
                    );
                }
                return quad_err_prd.value();
            };

            xt::xtensor<double, 3> get_r_pearson()
            {
                if (!r_pearson.has_value())
                {
                    r_pearson = elements::calc_r_pearson(
                            get_err_obs(), get_err_prd(),
                            get_quad_err_obs(), get_quad_err_prd(),
                            t_msk, b_exp,
                            n_srs, n_msk, n_exp
                    );
                }
                return r_pearson.value();
            };

            xt::xtensor<double, 3> get_r_spearman()
            {
                if (!r_spearman.has_value())
                {
                    r_spearman = elements::calc_r_spearman(
                            q_obs, q_prd, t_msk, b_exp,
                            n_srs, n_msk, n_exp
                    );
                }
                return r_spearman.value();
            };

            xt::xtensor<double, 3> get_alpha()
            {
                if (!alpha.has_value())
                {
                    alpha = elements::calc_alpha(
                            q_obs, q_prd, get_mean_obs(), get_mean_prd(),
                            t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return alpha.value();
            };

            xt::xtensor<double, 3> get_gamma()
            {
                if (!gamma.has_value())
                {
                    gamma = elements::calc_gamma(
                            get_mean_obs(), get_mean_prd(), get_alpha()
                    );
                }
                return gamma.value();
            };

            xt::xtensor<double, 3> get_alpha_np()
            {
                if (!alpha_np.has_value())
                {
                    alpha_np = elements::calc_alpha_np(
                            q_obs, q_prd, get_mean_obs(), get_mean_prd(),
                            t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return alpha_np.value();
            };

            xt::xtensor<double, 3> get_bias()
            {
                if (!bias.has_value())
                {
                    bias = elements::calc_bias(
                            q_obs, q_prd, t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return bias.value();
            };

            xt::xtensor<double, 3> get_obs_event()
            {
                if (!obs_event.has_value())
                {
                    obs_event = elements::calc_obs_event(
                            q_obs, get_q_thr(), is_high_flow_event()
                    );
                }
                return obs_event.value();
            };

            xt::xtensor<double, 3> get_prd_event()
            {
                if (!prd_event.has_value())
                {
                    prd_event = elements::calc_prd_event(
                            q_prd, get_q_thr(), is_high_flow_event()
                    );
                }
                return prd_event.value();
            };

            xt::xtensor<double, 3> get_ct_a()
            {
                if (!ct_a.has_value())
                {
                    ct_a = elements::calc_ct_a(
                            get_obs_event(), get_prd_event()
                    );
                }
                return ct_a.value();
            };

            xt::xtensor<double, 3> get_ct_b()
            {
                if (!ct_b.has_value())
                {
                    ct_b = elements::calc_ct_b(
                            get_obs_event(), get_prd_event()
                    );
                }
                return ct_b.value();
            };

            xt::xtensor<double, 3> get_ct_c()
            {
                if (!ct_c.has_value())
                {
                    ct_c = elements::calc_ct_c(
                            get_obs_event(), get_prd_event()
                    );
                }
                return ct_c.value();
            };

            xt::xtensor<double, 3> get_ct_d()
            {
                if (!ct_d.has_value())
                {
                    ct_d = elements::calc_ct_d(
                            get_obs_event(), get_prd_event()
                    );
                }
                return ct_d.value();
            };

        public:
            // constructor method
            Evaluator(const XD2& obs,
                      const XD2& prd,
                      const XD2& thr,
                      xtl::xoptional<const std::string&, bool> events,
                      const XB3& msk,
                      const std::vector<xt::xkeep_slice<int>>& exp) :
                    q_obs{obs}, q_prd{prd},
                    _q_thr{thr}, _events{events},
                    t_msk{msk}, b_exp{exp}
            {
                // initialise a mask if none provided
                // (corresponding to no temporal subset)
                if (msk.size() < 1)
                {
                    t_msk = xt::ones<bool>(
                            {q_prd.shape(0), std::size_t {1}, q_prd.shape(1)}
                    );
                }

                // determine size for recurring dimensions
                n_srs = q_prd.shape(0);
                n_tim = q_prd.shape(1);
                n_msk = t_msk.shape(1);
                n_thr = _q_thr.shape(1);
                n_exp = b_exp.size();

                // drop time steps where observations or predictions are NaN
                for (std::size_t s = 0; s < n_srs; s++)
                {
                    auto obs_nan = xt::isnan(xt::view(q_obs, 0));
                    auto prd_nan = xt::isnan(xt::view(q_prd, s));

                    auto msk_nan = xt::where(obs_nan || prd_nan)[0];

                    xt::view(t_msk, s, xt::all(), xt::keep(msk_nan)) = false;
                }
            };

            // methods to compute metrics
            xt::xtensor<double, 3> get_MAE()
            {
                if (!MAE.has_value())
                {
                    MAE = metrics::calc_MAE(
                            get_abs_err(), t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return MAE.value();
            };

            xt::xtensor<double, 3> get_MARE()
            {
                if (!MARE.has_value())
                {
                    MARE = metrics::calc_MARE(
                            get_MAE(), get_mean_obs(), n_srs, n_msk, n_exp
                    );
                }
                return MARE.value();
            };

            xt::xtensor<double, 3> get_MSE()
            {
                if (!MSE.has_value())
                {
                    MSE = metrics::calc_MSE(
                            get_quad_err(), t_msk, b_exp, n_srs, n_msk, n_exp
                    );
                }
                return MSE.value();
            };            
            
            xt::xtensor<double, 3> get_RMSE()
            {
                if (!RMSE.has_value())
                {
                    RMSE = metrics::calc_RMSE(
                            get_MSE()
                    );
                }
                return RMSE.value();
            };

            xt::xtensor<double, 3> get_NSE()
            {
                if (!NSE.has_value())
                {
                    NSE = metrics::calc_NSE(
                            get_quad_err(), get_quad_err_obs(), t_msk, b_exp,
                            n_srs, n_msk, n_exp
                    );
                }
                return NSE.value();
            };

            xt::xtensor<double, 3> get_KGE()
            {
                if (!KGE.has_value())
                {
                    KGE = metrics::calc_KGE(
                            get_r_pearson(), get_alpha(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGE.value();
            };

            xt::xtensor<double, 4> get_KGE_D()
            {
                if (!KGE_D.has_value())
                {
                    KGE_D = metrics::calc_KGE_D(
                            get_r_pearson(), get_alpha(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGE_D.value();
            };

            xt::xtensor<double, 3> get_KGEPRIME()
            {
                if (!KGEPRIME.has_value())
                {
                    KGEPRIME = metrics::calc_KGEPRIME(
                            get_r_pearson(), get_gamma(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGEPRIME.value();
            };

            xt::xtensor<double, 4> get_KGEPRIME_D()
            {
                if (!KGEPRIME_D.has_value())
                {
                    KGEPRIME_D = metrics::calc_KGEPRIME_D(
                            get_r_pearson(), get_gamma(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGEPRIME_D.value();
            };

            xt::xtensor<double, 3> get_KGENP()
            {
                if (!KGENP.has_value())
                {
                    KGENP = metrics::calc_KGENP(
                            get_r_spearman(), get_alpha_np(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGENP.value();
            };

            xt::xtensor<double, 4> get_KGENP_D()
            {
                if (!KGENP_D.has_value())
                {
                    KGENP_D = metrics::calc_KGENP_D(
                            get_r_spearman(), get_alpha_np(), get_bias(),
                            n_srs, n_msk, n_exp
                    );
                }
                return KGENP_D.value();
            };

            xt::xtensor<double, 5> get_CONT_TBL()
            {
                if (!CONT_TBL.has_value())
                {
                    CONT_TBL = metrics::calc_CONT_TBL(
                            get_q_thr(), get_ct_a(), get_ct_b(), get_ct_c(),
                            get_ct_d(), t_msk, b_exp,
                            n_srs, n_thr, n_msk, n_exp
                    );
                }
                return CONT_TBL.value();
            };

            // methods to compute diagnostics
            xt::xtensor<double, 3> get_completeness()
            {
                return get_t_counts();
            };
        };
    }
}

#endif //EVALHYD_DETERMINIST_EVALUATOR_HPP
