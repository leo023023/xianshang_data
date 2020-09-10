$(document).ready(function () {
    $('.m_zffs_zffs_wx').click(function () {
        $('#wechat_pay_pay').attr("value","1");
        $('#wechat_pay_pay').prop("checked", "checked");
        $('#zfb_pay_pay').removeAttr("checked");
        $('.m_zffs_zffs_wx>i').addClass('m_zffs_active');
        $('.m_zffs_zffs_zfb>i').removeClass('m_zffs_active');
    });
    $('.m_zffs_zffs_zfb').click(function () {
        $('#wechat_pay_pay').attr("value","2");
        $('#wechat_pay_pay').prop("checked", "checked");
        $('#zfb_pay_pay').removeAttr("checked");
        $('.m_zffs_zffs_zfb>i').addClass('m_zffs_active');
        $('.m_zffs_zffs_wx>i').removeClass('m_zffs_active');
    });
    $('.pay_tc_colse').click(function () {
        $("#m_pay_tanchuang").css({"display": "none",})
    });
    $('.m_pay_tanchuang_bj').click(function () {
        $("#m_pay_tanchuang").css({"display": "none",})
    });
    $('#m_db_btn').click(function () {
        $("#m_pay_tanchuang").css({"display": "block",})
    });
     $('#m_gl_db_btn').click(function () {
        $("#m_pay_tanchuang").css({"display": "block",})
    });

    $('.m_xb_xz_nan').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_xb_xz_nv').removeClass('m_xb_xz_active');
        $('.m_xb_xz_nobirth').removeClass('m_xb_xz_active');
        $('#m_xb_xz_put').attr('value', '1');
    });
    $('.m_xb_xz_nv').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_xb_xz_nan').removeClass('m_xb_xz_active');
        $('.m_xb_xz_nobirth').removeClass('m_xb_xz_active');
        $('#m_xb_xz_put').attr('value', '0');
    });
    $('.m_xb_xz_nobirth').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_xb_xz_nv').removeClass('m_xb_xz_active');
        $('.m_xb_xz_nan').removeClass('m_xb_xz_active');
        $('#m_xb_xz_put').attr('value', '9');
    });


    $('.m_dz_xz_sz').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_dz_xz_mz').removeClass('m_xb_xz_active');
        $('.m_dz_xz_bh').removeClass('m_xb_xz_active');
        $('#m_xb_dz_put').attr('value', '1');
    });
    $('.m_dz_xz_mz').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_dz_xz_sz').removeClass('m_xb_xz_active');
        $('.m_dz_xz_bh').removeClass('m_xb_xz_active');
        $('#m_xb_dz_put').attr('value', '2');
    });
    $('.m_dz_xz_bh').click(function () {
        $(this).addClass('m_xb_xz_active');
        $('.m_dz_xz_sz').removeClass('m_xb_xz_active');
        $('.m_dz_xz_mz').removeClass('m_xb_xz_active');
        $('#m_xb_dz_put').attr('value', '9');
    });


    $('.m_dz_xz_ul>li').click(function () {
        $(this).addClass('m_dz_xz_active').siblings().removeClass('m_dz_xz_active')
    });

})