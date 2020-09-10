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
                $('.shortcut-add-box-left ul li input').eq(i).attr("name",'qiwang');
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
            $('.shortcut-add-box-left ul>li input').attr("name",'');
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