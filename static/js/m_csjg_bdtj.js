// 移动端预产期选择
$(function () {
    // 这是对开通了VIP的逻辑设计
    $('#m_vipmb').click(function () {

        $("#m_pay_tanchuang").css({"display": "block",})

    });
    $('.m_csjg_kaitong').click(function () {
        $("#m_pay_tanchuang").css({"display": "block",})

    });
    $('.mzku_btn_bg').click(function () {
        var birthtime = $('.csjg_birthtime').val();
        var mizi_ku_nm = $(this).val();
        var data = {
            birthtime: birthtime,
            mizi_ku_nm: mizi_ku_nm,
            // qiwang: qiwang,
        }
        $(".loader_bg").css({"display": "block",})

        if ($(this).val().length < 3) {
            $('.sceond_jieshi').addClass('jieshi_display');
        }
        else {
            $('.sceond_jieshi').removeClass('jieshi_display');
        }


        $.ajax({
            type: 'POST',
            url: '/m_ajax/',
            data: data,
            success: function (neirog) {
                var x = document.cookie;
                neirog = eval("(" + neirog + ")");
                $('.m_big_xingming').html(mizi_ku_nm);
                console.log('到这里来1');
                $('.q_m_pingying').html(neirog.q_m_pingying);
                $('.q_m_hanyi_1_1').html(neirog.q_m_hanyi_1_1);
                $('.q_m_hanyi_2_2').html(neirog.q_m_hanyi_2_2);
                $('.fenshu_fenshu').html(neirog.q_m_zh_df);
                $('.q_m_zh_df').html(neirog.q_m_zh_df);
                console.log('到这里来2');
                $('.q_m_qt_df_qx_lt_1').html(neirog.q_m_qt_df_qx_lt[1]);
                console.log('到这里来3');
                $('.q_m_qt_df_qx_lt_2').html(neirog.q_m_qt_df_qx_lt[2]);
                $('.q_m_qt_df_qx_lt_3').html(neirog.q_m_qt_df_qx_lt[3]);
                $('.q_m_qt_df_qx_lt_4').html(neirog.q_m_qt_df_qx_lt[4]);
                $('.q_m_qt_df_qx_lt_5').html(neirog.q_m_qt_df_qx_lt[5]);
                $('.q_m_qt_df_qx_lt_0').html(neirog.q_m_qt_df_qx_lt[0]);
                console.log('到这里来4');
                $('.q_m_qt_df_qx_lt_1_1').html(neirog.q_m_qt_df_qx_lt[1]);
                $('.q_m_qt_df_qx_lt_2_2').html(neirog.q_m_qt_df_qx_lt[2]);
                $('.q_m_qt_df_qx_lt_3_3').html(neirog.q_m_qt_df_qx_lt[3]);
                $('.q_m_qt_df_qx_lt_4_4').html(neirog.q_m_qt_df_qx_lt[4]);
                $('.q_m_qt_df_qx_lt_5_5').html(neirog.q_m_qt_df_qx_lt[5]);
                $('.q_m_qt_df_qx_lt_0_0').html(neirog.q_m_qt_df_qx_lt[0]);
                for (var i = 0; i < neirog.q_m_yjjd_qx_3.length; i++) {
                    var item = neirog.q_m_yjjd_qx_3[i];
                    $(".q_m_yjjd_qx" + [i]).html(item);
                }
                ;
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
                for (var i = 0; i < neirog.q_m_sxxg_qp.length; i++) {
                    var item_2 = neirog.q_m_sxxg_qp[i];
                    $(".sxsx_xingge_" + [i]).html(item_2);
                }
                ;
                for (var i = 0; i < neirog.q_m_sxxg_qd_qp_2.length; i++) {
                    var item_3 = neirog.q_m_sxxg_qd_qp_2[i];
                    $(".sxsx_xgqd_" + [i]).html(item_3);
                }
                ;
                $('.q_m_sxxg_jies').html(neirog.q_m_sxxg_jies);

                $('.xz_xz').html(neirog.q_m_sm_xz);

                for (var i = 0; i < neirog.q_m_sm_xz_yd_qx_qp.length; i++) {
                    var item_4 = neirog.q_m_sm_xz_yd_qx_qp[i];
                    $(".xz_xingge_" + [i]).html(item_4);
                }
                ;
                for (var i = 0; i < neirog.q_m_sm_xz_qd_qp.length; i++) {
                    var item_5 = neirog.q_m_sm_xz_qd_qp[i];
                    $(".xz_xinggeqd_" + [i]).html(item_5);
                }
                ;
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
                for (var i = 0; i < neirog.q_m_zybg_jg_qx2.length; i++) {
                    var item_6 = neirog.q_m_zybg_jg_qx2[i];
                    $(".gx_rzml_p_" + [i]).html(item_6);
                }
                console.log('到这里来')
                $('.q_m_gxys_jx_dx').html(neirog.q_m_gxys_jx_dx);
                $('.q_m_gxys_jx_zl').html(neirog.q_m_gxys_jx_zl);
                $('.q_m_gxys_jx_jy').html(neirog.q_m_gxys_jx_jy);
                $('.q_m_gxys_jx_sy').html(neirog.q_m_gxys_jx_sy);
                $('.q_m_gxys_jx_js').html(neirog.q_m_gxys_jx_js);
                $('.q_m_gxys_jx_qm').html(neirog.q_m_gxys_jx_qm);
                $('.q_m_yxy_ming_0').html(neirog.li_lt_mz_noxing_1[0]);
                $('.q_m_yxy_ming_1').html(neirog.li_lt_mz_noxing_1[1]);
                $('.q_m_yxy_zyjs1').html(neirog.q_m_yxy_zyjs1);
                $('.q_m_yxy_yzjs1_qx').html(neirog.q_m_yxy_yzjs1_qx);
                $('.q_m_yjjd_qx_3_0').html(neirog.q_m_yjjd_qx_3[0]);
                $('.q_m_yxy_zyjs2').html(neirog.q_m_yxy_zyjs2);
                $('.q_m_yxy_yzjs22_qx').html(neirog.q_m_yxy_yzjs22_qx);
                $('.q_m_yjjd_qx_3').html(neirog.q_m_yjjd_qx_3);
                for (var i = 0; i < neirog.q_m_yxy_zyfx_qx1.length; i++) {
                    var item_7 = neirog.q_m_yxy_zyfx_qx1[i];
                    $(".zyfx_p_0_" + [i]).html(item_7);
                }
                $('.q_m_yxy_ylfx_qx').html(neirog.q_m_yxy_ylfx_qx);
                for (var i = 0; i < neirog.q_m_yxy_zxfx_lt2.length; i++) {
                    var item_8 = neirog.q_m_yxy_zxfx_lt2[i];
                    $(".zyfx_p_1_" + [i]).html(item_8);
                }
                $('.q_m_yxy_dsdp_qx').html(neirog.q_m_yxy_dsdp_qx);
                $(".loader_bg").css({"display": "none",});
            },
        })
    });
})

