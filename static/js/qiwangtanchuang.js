$(function () {
    lanPosScroll();
    modelConfirm();
    shortcutChoice();
})

function lanPosScroll() {
    var index = 0;
    var shortcutBox = $('.modal .modal-dialog .shortcut-add-box');
    var shortcutBoxList = $('.shortcut-add-box-left');
    $('.lanPos').css('top', $('.shortcut-add-box-left .active').position().top);
    $('.shortcut-add-box-left ul li').hover(function () {
        $('.lanPos').css('top', $(this).position().top);
    }, function () {
        $('.lanPos').css('top', $('.shortcut-add-box-left .active').position().top);
    })
    $('.shortcut-add-box-left ul li').click(function () {
        for (var i = 0; i < $('.shortcut-add-box-left ul li').size(); i++) {
            if (this == $('.shortcut-add-box-left ul li').get(i)) {
                $('.shortcut-add-box-left ul li').eq(i).addClass('active');
                $('.shortcut-add-box-left ul li input').eq(i).attr("name", 'qiwang');
            } else {
                $('.shortcut-add-box-left ul li').eq(i).removeClass('active');
                // $('.shortcut-add-box-left ul li input').eq(i).attr("name",'');
            }
        }
        ;index = $('.shortcut-add-box-left ul li').index(this);
    })
};

function shortcutChoice() {
    var shortcutBtn = $('.shortcut-add-box-left ul>li');
    shortcutBtn.click(function () {
        if ($(this).hasClass('shortcut-selected')) {
            $(this).removeClass('shortcut-selected');
            $('.shortcut-add-box-left ul>li input').attr("name", '');
        }
        else {
            $(this).addClass('shortcut-selected');
            // $('.shortcut-add-box-left ul>li input').attr("name",'qiwang');
        }
    })
};

function modelConfirm() {
    var selectShortcut_box = $('#select-shortcut-box');
    var shortcutBoxLi = $('.shortcut-box li:not(:last)');

    $('#shortcutEnter').click(function () {
        $('#myModal').modal('hide');
        shortcutBoxLi.remove();

        function init_hasShortcut_html() {
            var select_iClass_data = [];
            var select_spanText_data = [];
            var shortcutSelected_data = [];
            var has_p_data = [];
            var has_iclass_data = [];
            var hasShortcut_html = '';
            var acticveSelect = null;
            acticveSelect = $('.shortcut-add-box-left').find('.shortcut-selected');
            $.each(acticveSelect, function (i) {
                select_iClass_data.push(acticveSelect.eq(i).find('i').attr('class'));
                select_spanText_data.push(acticveSelect.eq(i).find('span').text());
            });
            $.each($('.shortcut-box li:not(:last)'), function (i) {
                has_p_data.push($('.shortcut-box li:not(:last)').find('p').text());
            });
            $.each($('.shortcut-box li:not(:last)'), function (i) {
                has_iclass_data.push($('.shortcut-box li:not(:last)').find('i').attr('class'));
            });

            function test(a, b) {
                var c = [];
                var tmp = a.concat(b);
                var o = {};
                for (var i = 0; i < tmp.length; i++) (tmp[i] in o) ? o[tmp[i]]++ : o[tmp[i]] = 1;
                for (var x in o) if (o[x] == 1) c.push(x);
                return c;
            }

            for (var i = 0; i < test(has_iclass_data, select_iClass_data).length; i++) {
                var select_i_class = test(has_iclass_data, select_iClass_data)[i];
                var select_i_span = test(has_p_data, select_spanText_data)[i];
                var select_person = {"iClass": select_i_class, 'spanText': select_i_span};
                shortcutSelected_data.push(select_person);
            }
            ;console.log(shortcutSelected_data);
            for (var j = 0; j < shortcutSelected_data.length; j++) {
                var hasObj = shortcutSelected_data[j];
                hasShortcut_html += '<li class="col-xs-4 col-sm-4 col-md-3 col-lg-3">';
                hasShortcut_html += '<div>';
                hasShortcut_html += '<i class="' + hasObj.iClass + '">' + '</i>';
                hasShortcut_html += '<p>' + hasObj.spanText + '</p>';
                hasShortcut_html += '</div>';
                hasShortcut_html += '</li>';
            }
            ;
            return hasShortcut_html;
        }

        $('.shortcut-box li:not(:last)').remove();
        $('.shortcut-box li').before(init_hasShortcut_html());
        $.each($('.shortcut-box li:not(:last)'), function (i) {
            var bgIndex = (i + 0) % 5;
            switch (bgIndex) {
                case 1:
                    $('.shortcut-box li:not(:last)').eq(i).find('div').css('background', '#303849');
                    break;
                case 2:
                    $('.shortcut-box li:not(:last)').eq(i).find('div').css('background', '#303849');
                    break;
                case 3:
                    $('.shortcut-box li:not(:last)').eq(i).find('div').css('background', '#303849');
                    break;
                case 4:
                    $('.shortcut-box li:not(:last)').eq(i).find('div').css('background', '#303849');
                    break;
                case 0:
                    $('.shortcut-box li:not(:last)').eq(i).find('div').css('background', '#303849');
                    break;
            }
        })
    });
}

$(document).ready(function () {
    $(".qiminordafen .bd_grqm").click(function () {
        $(this).addClass("active");
        $('.dingzixuantian_1').removeClass("dingzixuantian");
        $(".shuru_dingzi").css('display', 'block');
        $('.bd_mzdf').removeClass("active");
        $(".qiwangtanchuang_js_name").text("请输入姓氏:");
        $(".shortcut-box").css('display', 'block');
        $('.bd_qiwang').removeClass("qiwangtanchang_js_hide");
        $(".qw_biaoti").css('margin-left', '-307px');
        $("#form_tijiao").css('display', 'block');
        $(".bd_lijiceming").css('display', 'none');
        $(".xb_xz_class_cs").css('display', 'inline-block');
        $("#cssj_js").html('预产期:');
        $(".biaodan_neirong .name").css('width', '60px');
        $(".daosnajiao_dafen").css('display', 'block');
        $("#biaodan__xb_nobirth").prop("checked",true);
        $("#biaodan_xb_nan").prop("checked",false);
    })
    $(".qiminordafen .bd_mzdf").click(function () {
        $(this).addClass("active");
        $('.dingzixuantian_1').addClass("dingzixuantian");
        $(".shuru_dingzi").css('display', 'none');
        $('.bd_grqm').removeClass("active");
        $(".qiwangtanchuang_js_name").text("请输入姓名:");
        $(".shortcut-box").css('display', 'none');
        $('.bd_qiwang').addClass("qiwangtanchang_js_hide");
        $(".qw_biaoti").css('margin-left', '-1px');
        $("#form_tijiao").css('display', 'none');
        $(".bd_lijiceming").css('display', 'block');
        $(".xb_xz_class_cs").css('display', 'none');
        $("#cssj_js").html('出生时间:');
        $(".biaodan_neirong .name").css('width', '147px');
        $(".daosnajiao_dafen").css('display', 'none');
        $("#biaodan__xb_nobirth").prop("checked",false);
        $("#biaodan_xb_nan").prop("checked",true);
    })


    $('.bd_lijiceming_in').click(function () {
        // var mizi_ku_nm = document.getElementByclassName('name_xingming').val();
        // var birthtime = document.getElementid('date-input').value;

        var mizi_ku_nm = $('.name_xingming').val();
        var birthtime = $('#date-input').val();
        var xingbie_js = $('input[name="xingbie"]:checked').val();
        var birthplace = $('#btn1').val();
        var myRegttzw = /^[\u4e00-\u9fa5]+$/;
        console.log('这个是获取懂啊的名字', mizi_ku_nm)
        console.log('这个是获取懂啊的出生日期', birthtime)
        console.log('这个是获取的性别', xingbie_js)
        console.log('这个是获取懂啊的地点', birthplace)

        if ($('.name_xingming').val() == '') {
            alert("请输入正确的名字信息!");
            return false;
        }
        else if ($('.name_xingming').val().length < 2)
        {
            alert("请输入完整的名字信息!");
            return false;
        }
        else if (myRegttzw.test(mizi_ku_nm)) {
            console.log('获取数据成功');
            url_js = 'http://www.qmg365.com/'+'qmb_dafeng_qd?'+'　&name='+mizi_ku_nm+"&xb="+xingbie_js+'&birthtime='+birthtime+'&birthplace='+birthplace
            window.open(url_js)

        }
        else {
            alert("名字格式有误，请重新输入!");
        }

    })
});

