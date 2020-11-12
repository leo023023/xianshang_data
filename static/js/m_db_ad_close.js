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
    var tabDom = $('.biaodan');
    var tabDom_a = $('.area_content');
    var h = tabDom.offset().top;
    $(window).scroll(function () {
        var _h = $(window).scrollTop();
        if (_h - h + 90 >= 0) {
            tabDom.addClass('fixed');
            tabDom.addClass('fixed_guai');
            tabDom_a.addClass('fixed');
            tabDom_a.addClass('fixed_guai');
            var wid = $(window).width();
            var newwid = (wid - 1200) / 2;
            $('.fixed').css('right', newwid + 'px')
            $('.fixed_guai').css('right', newwid + 'px')
        } else {
            tabDom.removeClass('fixed');
            tabDom.removeClass('fixed_guai');
            tabDom_a.removeClass('fixed');
            tabDom_a.removeClass('fixed_guai');
        }
    })
    $(window).resize(function () {
        var _h = $(window).scrollTop();
        if (_h - h + 90 >= 0) {
            tabDom.addClass('fixed');
            tabDom.addClass('fixed_guai');
            tabDom_a.addClass('fixed');
            tabDom_a.addClass('fixed_guai');
            var wid = $(window).width();
            var newwid = (wid - 1200) / 2;
            $('.fixed').css('right', newwid + 'px')
            $('.fixed_guai').css('right', newwid + 'px')
        } else {
            tabDom.removeClass('fixed');
            tabDom.removeClass('fixed_guai');
            tabDom_a.removeClass('fixed');
            tabDom_a.removeClass('fixed_guai');
            
        }
    });
    $('.close').click(function(){
    	$('#myModal').modal('hide');
        shortcutBoxLi.remove();
    })
})

