$(document).ready(function () {
    $('#m_order_btn_vip').click(function () {
        var phone = document.getElementById('m_order_tele_vip').value;
        if (!(/^1(3|4|5|6|7|8|9)\d{9}$/.test(phone))) {
            alert("请输入有效的手机号码!");
            return false;
        }
    });
    $('.no_vip_wenan_close').click(function () {
        $('.no_vip_kkk').css('display', 'none')
    });
    // $('.no_vip_kkk').click(function () {
    //     $('.no_vip_kkk').css('display','none')
    // });
    $('.no_vip_kkkt').click(function () {
        $('.no_vip_kkk').css('display', 'none')
        $("#m_pay_tanchuang").css("display","block")
    });
})