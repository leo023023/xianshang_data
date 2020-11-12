// pc端名字提交


$(function () {
    $(".mz_ku_la").each(function () {
        $(this).find("a input").first().addClass("active_miziku");
        $(this).find(" .mzku_btn_bg ").first().addClass("active_miziku");
    });
    $('.mzku_btn_bg').click(function () {
        $(".loader_bg").css({"display": "block",})
        var birthtime = $('.csjg_birthtime').val();
        var mizi_ku_nm = $(this).val();
        var data = {
            birthtime: birthtime,
            mizi_ku_nm: mizi_ku_nm,
            // qiwang: qiwang,
        }
        $(".loader_bg").css({"display": "block",})
        $(this).addClass('active_miziku')
        $(this).siblings().removeClass('active_miziku')
        $.ajax({
            type: 'POST',
            url: '/m_ajax/',
            data: data,
            success: function (neirog, status) {
                var x = document.cookie;
                neirog = eval("(" + neirog + ")");
                $('.jxhm_zongshu .name').html(mizi_ku_nm);
                $('.jxhm_zongshu .pingying').html(neirog.q_m_pingying);
                $('.q_m_hanyi_1_1').html(neirog.q_m_hanyi_1_1);
                $('.q_m_hanyi_2_2').html(neirog.q_m_hanyi_2_2);
                $('.fenshu_fenshu').html(neirog.q_m_zh_df+'分');
                $('.q_m_zh_df').html(neirog.q_m_zh_df);
                $('.q_m_qt_df_qx_lt_1').html(neirog.q_m_qt_df_qx_lt[1]);
                $('.q_m_qt_df_qx_lt_2').html(neirog.q_m_qt_df_qx_lt[2]);
                $('.q_m_qt_df_qx_lt_3').html(neirog.q_m_qt_df_qx_lt[3]);
                $('.q_m_qt_df_qx_lt_4').html(neirog.q_m_qt_df_qx_lt[4]);
                $('.q_m_qt_df_qx_lt_5').html(neirog.q_m_qt_df_qx_lt[5]);
                $('.q_m_qt_df_qx_lt_0').html(neirog.q_m_qt_df_qx_lt[0]);

                $('.q_m_qt_df_qx_lt_1_1').html(neirog.q_m_qt_df_qx_lt[1]);
                $('.q_m_qt_df_qx_lt_2_2').html(neirog.q_m_qt_df_qx_lt[2]);
                $('.q_m_qt_df_qx_lt_3_3').html(neirog.q_m_qt_df_qx_lt[3]);
                $('.q_m_qt_df_qx_lt_4_4').html(neirog.q_m_qt_df_qx_lt[4]);
                $('.q_m_qt_df_qx_lt_5_5').html(neirog.q_m_qt_df_qx_lt[5]);
                $('.q_m_qt_df_qx_lt_0_0').html(neirog.q_m_qt_df_qx_lt[0]);


                $(".yjjd_nr").empty();
                html_q_m_yjjd = ''
                for (var i = 0; i < neirog.q_m_yjjd_qx_3.length; i++) {
                    html_q_m_yjjd += '<p class="q_m_yjjd_qx_cnm">"'+"来自"+neirog.q_m_yjjd_qx_3[i]+'</p><br>'
                };
                $(".yjjd_nr").html(html_q_m_yjjd);



                $('.q_m_bzky_qx').html(neirog.q_m_bzky_qx);
                $('.q_m_dsdp').html(neirog.q_m_dsdp);
                $('.mz_yx_lt_qx_qp_0').html(neirog.mz_yx_lt_qx_qp[0]);
                $('.mz_yx_lt_qx_qp_1').html(neirog.mz_yx_lt_qx_qp[1]);
                $('.mz_yx_lt_qx_qp_2').html(neirog.mz_yx_lt_qx_qp[2]);
                $('.mz_yx_lt_qx_qp_3').html(neirog.mz_yx_lt_qx_qp[3]);
                $('.mz_yx_lt_qx_qp_4').html(neirog.mz_yx_lt_qx_qp[4]);
                $('.mz_yx_lt_qx_qp_5').html(neirog.mz_yx_lt_qx_qp[5]);
                $('.li_lt_mz_noxing_1').html(neirog.li_lt_mz_noxing_1);
                $('.q_m_bzky_qx').html(neirog.q_m_bzky_qx);
                $('.q_m_dsdp').html(neirog.q_m_dsdp);

                $(".rzml_shengxiao_abcd").empty();
                shengxiao_abcd = ''


                for (var i = 0; i < neirog.q_m_sxxg_qp.length; i++) {
                    shengxiao_abcd += '<p class="sxsx_xingge sxsx_xingge_cnm">"'+neirog.q_m_sxxg_qp[i]+'</p>'
                };
                $(".rzml_shengxiao_abcd").html(shengxiao_abcd);



                $(".rzml_xbt_fr_bcde").empty();
                html_q_m_bcde = ''
                for (var i = 0; i < neirog.q_m_sxxg_qd_qp_2.length; i++) {
                    html_q_m_bcde += '<p class="sxsx_xingge sxsx_xingge_cnm">"'+neirog.q_m_sxxg_qd_qp_2[i]+'</p>'
                };
                $(".rzml_xbt_fr_bcde").html(html_q_m_bcde);

                $('.q_m_sxxg_jies').html(neirog.q_m_sxxg_jies);
                $('.xz_xz').html(neirog.q_m_sm_xz);


                $(".rzml_xbt_fr_cdef").empty();
                html_q_m_cdef = ''
                for (var i = 0; i < neirog.q_m_sm_xz_yd_qx_qp.length; i++) {
                    html_q_m_cdef += '<p class="sxsx_xingge sxsx_xingge_cnm">"'+neirog.q_m_sm_xz_yd_qx_qp[i]+'</p>'
                };
                $(".rzml_xbt_fr_abcd").html(html_q_m_cdef);


                $(".rzml_xbt_fr_defg").empty();
                html_q_m_cdef = ''
                for (var i = 0; i < neirog.q_m_sm_xz_qd_qp.length; i++) {
                    html_q_m_cdef += '<p class="sxsx_xingge sxsx_xingge_cnm">"'+neirog.q_m_sm_xz_qd_qp[i]+'</p>'
                };
                $(".rzml_xbt_fr_defg").html(html_q_m_cdef);

                $('.q_m_xz_pfjs_pf').html(neirog.q_m_xz_pfjs_pf);
                $('.q_m_scwg_qb_1').html(neirog.q_m_scwg_qb[0]);
                $('.q_m_scwg_qb_2').html(neirog.q_m_scwg_qb[1]);
                $('.q_m_scwg_ming_2_qx').html(neirog.q_m_scwg_ming_2_qx);
                $('.q_m_scwg_tiange').html(neirog.q_m_scwg_tiange);
                $('.q_m_scwg_dige').html(neirog.q_m_scwg_dige);
                $('.q_m_scwg_renge').html(neirog.q_m_scwg_renge);
                $('.q_m_scwg_zongge').html(neirog.q_m_scwg_zongge);
                $('.q_m_scwg_tiange_jx').html(neirog.q_m_scwg_tiange_jx);
                $('.q_m_scwg_dige_jx').html(neirog.q_m_scwg_dige_jx);
                $('.q_m_scwg_renge_jx').html(neirog.q_m_scwg_renge_jx);
                $('.q_m_scwg_waige').html(neirog.q_m_scwg_waige);
                $('.q_m_scwg_zongge_jx').html(neirog.q_m_scwg_zongge_jx);
                $('.q_m_scwg_scwg_jx').html(neirog.q_m_scwg_scwg_jx);
                $('.q_m_scwg_jcy_jx').html(neirog.q_m_scwg_jcy_jx);
                $('.q_m_scwg_cgy_jx').html(neirog.q_m_scwg_cgy_jx);
                $('.q_m_scwg_rjgx_jx').html(neirog.q_m_scwg_rjgx_jx);
                $('.q_m_scwg_xg_jx').html(neirog.q_m_scwg_xg_jx);
                $('.q_m_gx_jx_qp_2_0').html(neirog.q_m_gx_jx_qp_2[0]);
                $('.q_m_gx_jx_qp_2_1').html(neirog.q_m_gx_jx_qp_2[1]);


                $(".xz_xbt_fr_jg_list").empty();
                xz_xbt_fr_jg_efgh = ''
                for (var i = 0; i < neirog.q_m_zybg_jg_qx2.length; i++) {
                    xz_xbt_fr_jg_efgh += '<p class="gx_rzml_p gx_rzml_p_cnm">"'+neirog.q_m_zybg_jg_qx2[i]+'</p>'
                };
                $(".xz_xbt_fr_jg_list").html(xz_xbt_fr_jg_efgh);



                $('.q_m_gxys_jx_dx').html(neirog.q_m_gxys_dx_qx);
                $('.q_m_gxys_jx_zl').html(neirog.q_m_gxys_zl_qx);
                $('.q_m_gxys_jx_jy').html(neirog.q_m_gxys_jy_qx);
                $('.q_m_gxys_jx_sy').html(neirog.q_m_gxys_sy_qx);
                $('.q_m_gxys_jx_js').html(neirog.q_m_gxys_js_qx);
                $('.q_m_gxys_jx_qm').html(neirog.q_m_gxys_qm_qx);
                $('.q_m_gxys_jx_hl').html(neirog.q_m_gxys_hl_qx);


                $('.q_m_yxy_ming_1').html(neirog.li_lt_mz_noxing_1[0]);
                $('.q_m_yxy_ming_2').html(neirog.li_lt_mz_noxing_1[1]);

                $('.q_m_yxy_zyjs1').html(neirog.q_m_yxy_zyjs1);
                $('.q_m_yxy_zyjs2').html(neirog.q_m_yxy_zyjs2);

                $('.q_m_yxy_yzjs1_qx').html(neirog.q_m_yxy_yzjs1_qx);
                $('.q_m_yjjd_qx_3_0').html(neirog.q_m_yjjd_qx_3[0]);
                $('.q_m_yxy_zyjs2').html(neirog.q_m_yxy_zyjs2);
                $('.q_m_yxy_yzjs22_qx').html(neirog.q_m_yxy_yzjs22_qx);

                $('.q_m_yjjd_qx_3').html(neirog.q_m_yjjd_qx_3);


                $(".xz_xbt_fr_fghi").empty();
                xz_xbt_fr_jg_fghi = ''
                for (var i = 0; i < neirog.q_m_yxy_zyfx_qx1.length; i++) {
                    xz_xbt_fr_jg_fghi += '<p class="zyfx_p zyfx_p_cnm">"'+neirog.q_m_yxy_zyfx_qx1[i]+'</p>'
                };
                $(".xz_xbt_fr_fghi").html(xz_xbt_fr_jg_fghi);



                $('.q_m_yxy_ylfx_qx').html(neirog.q_m_yxy_ylfx_qx);





                $(".xz_list_zsfx").empty();
                xz_xbt_fr_jg_ghij = ''
                for (var i = 0; i < neirog.q_m_yxy_zxfx_lt2.length; i++) {
                    xz_xbt_fr_jg_ghij += '<p class="zyfx_p zyfx_p_cnm">"'+neirog.q_m_yxy_zxfx_lt2[i]+'</p>'
                };
                $(".xz_list_zsfx").html(xz_xbt_fr_jg_ghij);

                $('.q_m_yxy_dsdp_qx').html(neirog.q_m_yxy_dsdp_qx);
                $(".loader_bg").css({"display": "none",});
                $(".loader_bg").css({"display": "none",});
            },
        })
    });
})

