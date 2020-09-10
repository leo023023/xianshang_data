$(document).ready(function () {
    $('.m_ad_close').click(function () {
        // $('#m_dinbuad').hide();
        $('.m_csjg_kong').css('height', '0px');
        $('#m_csjg_kong').css('height', '0px');
    })
    $('.closed').click(function () {
        $('#dingbuad').hide();
        $('#headnav').css('margin-top', '0px');
        // $('#m_csjg_kong').css('height','0px');
    })
    $('.qiwang_tc_close').click(function () {
        $('#myModal').modal('hide');
        // $('#m_csjg_kong').css('height','0px');
    })
})