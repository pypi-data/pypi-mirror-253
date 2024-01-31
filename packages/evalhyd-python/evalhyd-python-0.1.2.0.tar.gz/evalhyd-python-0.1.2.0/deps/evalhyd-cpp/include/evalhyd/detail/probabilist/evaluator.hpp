// Copyright (c) 2023, INRAE.
// Distributed under the terms of the GPL-3 Licence.
// The full licence is in the file LICENCE, distributed with this software.

#ifndef EVALHYD_PROBABILIST_EVALUATOR_HPP
#define EVALHYD_PROBABILIST_EVALUATOR_HPP

#include <stdexcept>
#include <vector>

#include <xtl/xoptional.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xview.hpp>

#include "diagnostics.hpp"
#include "brier.hpp"
#include "cdf.hpp"
#include "quantiles.hpp"
#include "contingency.hpp"
#include "ranks.hpp"
#include "intervals.hpp"
#include "multivariate.hpp"


namespace evalhyd
{
    namespace probabilist
    {
        template <class XD2, class XD4, class XB4>
        class Evaluator
        {
        private:
            // members for input data
            const XD2& q_obs;
            const XD4& q_prd;
            // members for optional input data
            const XD2& _q_thr;
            const xt::xtensor<double, 1>& _c_lvl;
            xtl::xoptional<const std::string, bool> _events;
            xt::xtensor<bool, 4> t_msk;
            const std::vector<xt::xkeep_slice<int>>& b_exp;

            // member for "reproducible randomness"
            const long int random_seed;

            // members for dimensions
            std::size_t n_sit;
            std::size_t n_ldt;
            std::size_t n_tim;
            std::size_t n_msk;
            std::size_t n_mbr;
            std::size_t n_thr;
            std::size_t n_itv;
            std::size_t n_exp;

            // members for computational elements
            // > Diagnostics
            xtl::xoptional<xt::xtensor<double, 4>, bool> t_counts;
            // > Brier-based
            xtl::xoptional<xt::xtensor<double, 3>, bool> o_k;
            xtl::xoptional<xt::xtensor<double, 5>, bool> bar_o;
            xtl::xoptional<xt::xtensor<double, 4>, bool> sum_f_k;
            xtl::xoptional<xt::xtensor<double, 4>, bool> y_k;
            // > Quantiles-based
            xtl::xoptional<xt::xtensor<double, 4>, bool> q_qnt;
            // > Contingency table-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> a_k;
            xtl::xoptional<xt::xtensor<double, 5>, bool> ct_a;
            xtl::xoptional<xt::xtensor<double, 5>, bool> ct_b;
            xtl::xoptional<xt::xtensor<double, 5>, bool> ct_c;
            xtl::xoptional<xt::xtensor<double, 5>, bool> ct_d;
            // > Ranks-based
            xtl::xoptional<xt::xtensor<double, 3>, bool> r_k;
            xtl::xoptional<xt::xtensor<double, 5>, bool> o_j;
            // > Intervals-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> itv_bnds;
            xtl::xoptional<xt::xtensor<double, 4>, bool> obs_in_itv;
            xtl::xoptional<xt::xtensor<double, 4>, bool> itv_width;

            // members for intermediate evaluation metrics
            // (i.e. before the reduction along the temporal axis)
            // > Brier-based
            xtl::xoptional<xt::xtensor<double, 4>, bool> bs;
            // > CDF-based
            xtl::xoptional<xt::xtensor<double, 3>, bool> crps_from_ecdf;
            // > Quantiles-based
            xtl::xoptional<xt::xtensor<double, 4>, bool> qs;
            xtl::xoptional<xt::xtensor<double, 3>, bool> crps_from_qs;
            // > Contingency table-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> pod;
            xtl::xoptional<xt::xtensor<double, 5>, bool> pofd;
            xtl::xoptional<xt::xtensor<double, 5>, bool> far;
            xtl::xoptional<xt::xtensor<double, 5>, bool> csi;
            // > Intervals-based
            xtl::xoptional<xt::xtensor<double, 4>, bool> ws;
            // > Multi-variate
            xtl::xoptional<xt::xtensor<double, 2>, bool> es;

            // members for evaluation metrics
            // > Brier-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> BS;
            xtl::xoptional<xt::xtensor<double, 7>, bool> REL_DIAG;
            xtl::xoptional<xt::xtensor<double, 6>, bool> BS_CRD;
            xtl::xoptional<xt::xtensor<double, 6>, bool> BS_LBD;
            xtl::xoptional<xt::xtensor<double, 5>, bool> BSS;
            xtl::xoptional<xt::xtensor<double, 4>, bool> CRPS_FROM_BS;
            // > CDF-based
            xtl::xoptional<xt::xtensor<double, 4>, bool> CRPS_FROM_ECDF;
            // > Quantiles-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> QS;
            xtl::xoptional<xt::xtensor<double, 4>, bool> CRPS_FROM_QS;
            // > Contingency table-based
            xtl::xoptional<xt::xtensor<double, 7>, bool> CONT_TBL;
            xtl::xoptional<xt::xtensor<double, 6>, bool> POD;
            xtl::xoptional<xt::xtensor<double, 6>, bool> POFD;
            xtl::xoptional<xt::xtensor<double, 6>, bool> FAR;
            xtl::xoptional<xt::xtensor<double, 6>, bool> CSI;
            xtl::xoptional<xt::xtensor<double, 5>, bool> ROCSS;
            // > Ranks-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> RANK_HIST;
            xtl::xoptional<xt::xtensor<double, 4>, bool> DS;
            xtl::xoptional<xt::xtensor<double, 4>, bool> AS;
            // > Intervals-based
            xtl::xoptional<xt::xtensor<double, 5>, bool> CR;
            xtl::xoptional<xt::xtensor<double, 5>, bool> AW;
            xtl::xoptional<xt::xtensor<double, 5>, bool> AWN;
            xtl::xoptional<xt::xtensor<double, 5>, bool> WS;
            // > Multi-variate
            xtl::xoptional<xt::xtensor<double, 4>, bool> ES;

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

            auto get_c_lvl()
            {
                if (_c_lvl.size() < 1)
                {
                    throw std::runtime_error(
                            "interval-based metric requested, "
                            "but *c_lvl* not provided"
                    );
                }
                else{
                    return _c_lvl;
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
            xt::xtensor<double, 4> get_t_counts()
            {
                if (!t_counts.has_value())
                {
                    t_counts = elements::calc_t_counts(
                            t_msk, b_exp, n_sit, n_ldt, n_msk, n_exp
                    );
                }
                return t_counts.value();
            };

            xt::xtensor<double, 3> get_o_k()
            {
                if (!o_k.has_value())
                {
                    o_k = elements::calc_o_k(
                            q_obs, get_q_thr(), is_high_flow_event()
                    );
                }
                return o_k.value();
            };

            xt::xtensor<double, 5> get_bar_o()
            {
                if (!bar_o.has_value())
                {
                    bar_o = elements::calc_bar_o(
                            get_o_k(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_msk, n_exp
                    );
                }
                return bar_o.value();
            };

            xt::xtensor<double, 4> get_sum_f_k()
            {
                if (!sum_f_k.has_value())
                {
                    sum_f_k = elements::calc_sum_f_k(
                            q_prd, get_q_thr(), is_high_flow_event()
                    );
                }
                return sum_f_k.value();
            };

            xt::xtensor<double, 4> get_y_k()
            {
                if (!y_k.has_value())
                {
                    y_k = elements::calc_y_k(
                            get_sum_f_k(), n_mbr
                    );
                }
                return y_k.value();
            };

            xt::xtensor<double, 4> get_q_qnt()
            {
                if (!q_qnt.has_value())
                {
                    q_qnt = elements::calc_q_qnt(
                            q_prd
                    );
                }
                return q_qnt.value();
            };

            xt::xtensor<double, 5> get_a_k()
            {
                if (!a_k.has_value())
                {
                    a_k = elements::calc_a_k(
                            get_sum_f_k(), n_mbr
                    );
                }
                return a_k.value();
            };

            xt::xtensor<double, 5> get_ct_a()
            {
                if (!ct_a.has_value())
                {
                    ct_a = elements::calc_ct_a(
                            get_o_k(), get_a_k()
                    );
                }
                return ct_a.value();
            };

            xt::xtensor<double, 5> get_ct_b()
            {
                if (!ct_b.has_value())
                {
                    ct_b = elements::calc_ct_b(
                            get_o_k(), get_a_k()
                    );
                }
                return ct_b.value();
            };

            xt::xtensor<double, 5> get_ct_c()
            {
                if (!ct_c.has_value())
                {
                    ct_c = elements::calc_ct_c(
                            get_o_k(), get_a_k()
                    );
                }
                return ct_c.value();
            };

            xt::xtensor<double, 5> get_ct_d()
            {
                if (!ct_d.has_value())
                {
                    ct_d = elements::calc_ct_d(
                            get_o_k(), get_a_k()
                    );
                }
                return ct_d.value();
            };

            xt::xtensor<double, 3> get_r_k()
            {
                if (!r_k.has_value())
                {
                    r_k = elements::calc_r_k(
                            q_obs, get_q_qnt(), n_mbr, random_seed
                    );
                }
                return r_k.value();
            };

            xt::xtensor<double, 5> get_o_j()
            {
                if (!o_j.has_value())
                {
                    o_j = elements::calc_o_j(
                            get_r_k(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return o_j.value();
            };

            xt::xtensor<double, 5> get_itv_bnds()
            {
                if (!itv_bnds.has_value())
                {
                    itv_bnds = elements::calc_itv_bnds(
                            q_prd, get_c_lvl(),
                            n_sit, n_ldt, n_itv, n_tim
                    );
                }
                return itv_bnds.value();
            };

            xt::xtensor<double, 4> get_obs_in_itv()
            {
                if (!obs_in_itv.has_value())
                {
                    obs_in_itv = elements::calc_obs_in_itv(
                            q_obs, get_itv_bnds()
                    );
                }
                return obs_in_itv.value();
            };

            xt::xtensor<double, 4> get_itv_width()
            {
                if (!itv_width.has_value())
                {
                    itv_width = elements::calc_itv_width(
                            get_itv_bnds()
                    );
                }
                return itv_width.value();
            };

            // methods to compute intermediate metrics
            xt::xtensor<double, 4> get_bs()
            {
                if (!bs.has_value())
                {
                    bs = intermediate::calc_bs(
                            get_o_k(), get_y_k()
                    );
                }
                return bs.value();
            };

            xt::xtensor<double, 3> get_crps_from_ecdf()
            {
                if (!crps_from_ecdf.has_value())
                {
                    crps_from_ecdf = intermediate::calc_crps_from_ecdf(
                            q_obs, get_q_qnt(), n_sit, n_ldt, n_mbr, n_tim
                    );
                }
                return crps_from_ecdf.value();
            };

            xt::xtensor<double, 4> get_qs()
            {
                if (!qs.has_value())
                {
                    qs = intermediate::calc_qs(
                            q_obs, get_q_qnt(), n_mbr
                    );
                }
                return qs.value();
            };

            xt::xtensor<double, 3> get_crps_from_qs()
            {
                if (!crps_from_qs.has_value())
                {
                    crps_from_qs = intermediate::calc_crps_from_qs(
                            get_qs(), n_mbr
                    );
                }
                return crps_from_qs.value();
            };

            xt::xtensor<double, 5> get_pod()
            {
                if (!pod.has_value())
                {
                    pod = intermediate::calc_pod(
                            get_ct_a(), get_ct_c()
                    );
                }
                return pod.value();
            };

            xt::xtensor<double, 5> get_pofd()
            {
                if (!pofd.has_value())
                {
                    pofd = intermediate::calc_pofd(
                            get_ct_b(), get_ct_d()
                    );
                }
                return pofd.value();
            };

            xt::xtensor<double, 5> get_far()
            {
                if (!far.has_value())
                {
                    far = intermediate::calc_far(
                            get_ct_a(), get_ct_b()
                    );
                }
                return far.value();
            };

            xt::xtensor<double, 5> get_csi()
            {
                if (!csi.has_value())
                {
                    csi = intermediate::calc_csi(
                            get_ct_a(), get_ct_b(), get_ct_c()
                    );
                }
                return csi.value();
            };

            xt::xtensor<double, 4> get_ws()
            {
                if (!ws.has_value())
                {
                    ws = intermediate::calc_ws(
                            q_obs, get_c_lvl(), get_itv_bnds()
                    );
                }
                return ws.value();
            };

            xt::xtensor<double, 2> get_es()
            {
                if (!es.has_value())
                {
                    es = intermediate::calc_es(
                            q_obs, q_prd, n_ldt, n_mbr, n_tim
                    );
                }
                return es.value();
            };

        public:
            // constructor method
            Evaluator(const XD2& obs,
                      const XD4& prd,
                      const XD2& thr,
                      const xt::xtensor<double, 1>& lvl,
                      xtl::xoptional<const std::string&, bool> events,
                      const XB4& msk,
                      const std::vector<xt::xkeep_slice<int>>& exp,
                      const long int seed) :
                    q_obs{obs}, q_prd{prd},
                    _q_thr{thr}, _c_lvl{lvl}, _events{events},
                    t_msk(msk), b_exp(exp),
                    random_seed{seed}
            {
                // initialise a mask if none provided
                // (corresponding to no temporal subset)
                if (msk.size() < 1)
                {
                    t_msk = xt::ones<bool>(
                            {q_prd.shape(0), q_prd.shape(1),
                             std::size_t {1}, q_prd.shape(3)}
                    );
                }

                // determine size for recurring dimensions
                n_sit = q_prd.shape(0);
                n_ldt = q_prd.shape(1);
                n_mbr = q_prd.shape(2);
                n_tim = q_prd.shape(3);
                n_msk = t_msk.shape(2);
                n_thr = _q_thr.shape(1);
                n_itv = _c_lvl.size();
                n_exp = b_exp.size();

                // drop time steps where observations and/or predictions are NaN
                for (std::size_t s = 0; s < n_sit; s++)
                {
                    for (std::size_t l = 0; l < n_ldt; l++)
                    {
                        auto obs_nan =
                                xt::isnan(xt::view(q_obs, s));
                        auto prd_nan =
                                xt::isnan(xt::view(q_prd, s, l));
                        auto sum_nan =
                                xt::eval(xt::sum(prd_nan, -1));

                        if (xt::amin(sum_nan) != xt::amax(sum_nan))
                        {
                            throw std::runtime_error(
                                    "predictions across members feature "
                                    "non-equal lengths"
                            );
                        }

                        auto msk_nan =
                                xt::where(obs_nan || xt::row(prd_nan, 0))[0];

                        xt::view(t_msk, s, l, xt::all(), xt::keep(msk_nan)) =
                                false;
                    }
                }
            };

            // methods to compute metrics
            xt::xtensor<double, 5> get_BS()
            {
                if (!BS.has_value())
                {
                    BS = metrics::calc_BS(
                            get_bs(), get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_msk, n_exp
                    );
                }
                return BS.value();
            };

            xt::xtensor<double, 7> get_REL_DIAG()
            {
                if (!REL_DIAG.has_value())
                {
                    REL_DIAG = metrics::calc_REL_DIAG(
                            get_q_thr(), get_o_k(), get_y_k(),
                            t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return REL_DIAG.value();
            };

            xt::xtensor<double, 6> get_BS_CRD()
            {
                if (!BS_CRD.has_value())
                {
                    BS_CRD = metrics::calc_BS_CRD(
                            get_q_thr(), get_bar_o(), get_REL_DIAG(),
                            get_t_counts(),
                            n_sit, n_ldt, n_thr, n_msk, n_exp
                    );
                }
                return BS_CRD.value();
            };

            xt::xtensor<double, 6> get_BS_LBD()
            {
                if (!BS_LBD.has_value())
                {
                    BS_LBD = metrics::calc_BS_LBD(
                            get_q_thr(), get_o_k(), get_y_k(),
                            t_msk, b_exp, get_t_counts(),
                            n_sit, n_ldt, n_thr, n_msk, n_exp
                    );
                }
                return BS_LBD.value();
            };

            xt::xtensor<double, 5> get_BSS()
            {
                if (!BSS.has_value())
                {
                    BSS = metrics::calc_BSS(
                            get_bs(), get_q_thr(), get_o_k(), get_bar_o(), t_msk,
                            b_exp, n_sit, n_ldt, n_thr, n_msk, n_exp
                    );
                }
                return BSS.value();
            };

            xt::xtensor<double, 4> get_CRPS_FROM_BS()
            {
                if (!CRPS_FROM_BS.has_value())
                {
                    CRPS_FROM_BS = metrics::calc_CRPS_FROM_BS(
                            q_obs, q_prd, is_high_flow_event(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return CRPS_FROM_BS.value();
            };

            xt::xtensor<double, 4> get_CRPS_FROM_ECDF()
            {
                if (!CRPS_FROM_ECDF.has_value())
                {
                    CRPS_FROM_ECDF = metrics::calc_CRPS_FROM_ECDF(
                            get_crps_from_ecdf(), t_msk, b_exp,
                            n_sit, n_ldt, n_msk, n_exp
                    );
                }
                return CRPS_FROM_ECDF.value();
            };

            xt::xtensor<double, 5> get_QS()
            {
                if (!QS.has_value())
                {
                    QS = metrics::calc_QS(
                            get_qs(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return QS.value();
            };

            xt::xtensor<double, 4> get_CRPS_FROM_QS()
            {
                if (!CRPS_FROM_QS.has_value())
                {
                    CRPS_FROM_QS = metrics::calc_CRPS_FROM_QS(
                            get_crps_from_qs(), t_msk, b_exp,
                            n_sit, n_ldt, n_msk, n_exp
                    );
                }
                return CRPS_FROM_QS.value();
            };

            xt::xtensor<double, 7> get_CONT_TBL()
            {
                if (!CONT_TBL.has_value())
                {
                    CONT_TBL = metrics::calc_CONT_TBL(
                            get_ct_a(), get_ct_b(), get_ct_c(), get_ct_d(),
                            get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return CONT_TBL.value();
            };

            xt::xtensor<double, 6> get_POD()
            {
                if (!POD.has_value())
                {
                    POD = metrics::calc_POD(
                            get_pod(), get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return POD.value();
            };

            xt::xtensor<double, 6> get_POFD()
            {
                if (!POFD.has_value())
                {
                    POFD = metrics::calc_POFD(
                            get_pofd(), get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return POFD.value();
            };

            xt::xtensor<double, 6> get_FAR()
            {
                if (!FAR.has_value())
                {
                    FAR = metrics::calc_FAR(
                            get_far(), get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return FAR.value();
            };

            xt::xtensor<double, 6> get_CSI()
            {
                if (!CSI.has_value())
                {
                    CSI = metrics::calc_CSI(
                            get_csi(), get_q_thr(), t_msk, b_exp,
                            n_sit, n_ldt, n_thr, n_mbr, n_msk, n_exp
                    );
                }
                return CSI.value();
            };

            xt::xtensor<double, 5> get_ROCSS()
            {
                if (!ROCSS.has_value())
                {
                    ROCSS = metrics::calc_ROCSS(
                            get_POD(), get_POFD(), get_q_thr()
                    );
                }
                return ROCSS.value();
            };

            xt::xtensor<double, 5> get_RANK_HIST()
            {
                if (!RANK_HIST.has_value())
                {
                    RANK_HIST = metrics::calc_RANK_HIST(
                            get_o_j(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return RANK_HIST.value();
            };

            xt::xtensor<double, 4> get_DS()
            {
                if (!DS.has_value())
                {
                    DS = metrics::calc_DS(
                            get_o_j(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return DS.value();
            };

            xt::xtensor<double, 4> get_AS()
            {
                if (!AS.has_value())
                {
                    AS = metrics::calc_AS(
                            get_r_k(), t_msk, b_exp,
                            n_sit, n_ldt, n_mbr, n_msk, n_exp
                    );
                }
                return AS.value();
            };

            xt::xtensor<double, 5> get_CR()
            {
                if (!CR.has_value())
                {
                    CR = metrics::calc_CR(
                            get_obs_in_itv(), t_msk, b_exp,
                            n_sit, n_ldt, n_itv, n_msk, n_exp
                    );
                }
                return CR.value();
            };

            xt::xtensor<double, 5> get_AW()
            {
                if (!AW.has_value())
                {
                    AW = metrics::calc_AW(
                            get_itv_width(), t_msk, b_exp,
                            n_sit, n_ldt, n_itv, n_msk, n_exp
                    );
                }
                return AW.value();
            };

            xt::xtensor<double, 5> get_AWN()
            {
                if (!AWN.has_value())
                {
                    AWN = metrics::calc_AWN(
                            q_obs, get_AW(), t_msk, b_exp,
                            n_sit, n_ldt, n_msk, n_exp
                    );
                }
                return AWN.value();
            };

            xt::xtensor<double, 5> get_WS()
            {
                if (!WS.has_value())
                {
                    WS = metrics::calc_WS(
                            get_ws(), t_msk, b_exp,
                            n_sit, n_ldt, n_itv, n_msk, n_exp
                    );
                }
                return WS.value();
            };

            xt::xtensor<double, 4> get_ES()
            {
                if (!ES.has_value())
                {
                    ES = metrics::calc_ES(
                            get_es(), t_msk, b_exp, n_ldt, n_msk, n_exp
                    );
                }
                return ES.value();
            };

            // methods to compute diagnostics
            xt::xtensor<double, 4> get_completeness()
            {
                return get_t_counts();
            };
        };
    }
}

#endif //EVALHYD_PROBABILIST_EVALUATOR_HPP
