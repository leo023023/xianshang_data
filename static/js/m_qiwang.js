$(function () {

    $('#singleSelectt').click(function () {
        $(".qiwangneirong").css({"display": "block",})
    });
    $('.m_qw_cancel').click(function () {
        $(".qiwangneirong").css({"display": "none",})
    });

    $('.m_qw_finish').click(function () {
        $(".qiwangneirong").css({"display": "none",})

        // 获取多选的value值
        var qiwang = $('.m_qw_qctive').map(function (index, elem) {
            return $(elem).val()
        }).get().join(',');
        var qiwang_sz= new Array();
        qiwang_sz=qiwang.split(",");

        // 获取多选的内容
        var qiwang_qwe = $('.m_qw_qctive').map(function (index, elem) {
            return $(elem).html()
        }).get().join(',');


        //
        if (qiwang.length == 0) {
            $("#zxcxzcxzc1").css({"display": "none",});
            $("#zxcxzcxzc2").css({"display": "none",});
            $("#zxcxzcxzc3").css({"display": "none",});
            $('#zxcxzcxzc1').html('');
            $('#zxcxzcxzc2').html('');
            $('#zxcxzcxzc3').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
        }
        ;

        if (qiwang.length == 1) {
            $("#zxcxzcxzc1").css({"display": "block",});
            $("#zxcxzcxzc2").css({"display": "none",});
            $("#zxcxzcxzc3").css({"display": "none",});
            var length_1 = qiwang_qwe[0] + qiwang_qwe[1]
            $('#zxcxzcxzc1').html(length_1);
            $('.m_qw_btn_moren').html('');
            $('#zxcxzcxzc2').html('');
            $('#zxcxzcxzc3').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
            xinz_html = ["<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>"]
            $('#xzchenggong').append(xinz_html);
            $('#zxcxzcxzc1_put').attr('value', qiwang_sz[0]);
        }
         ;
		
		if (qiwang.length == 2) {
            $("#zxcxzcxzc1").css({"display": "block",});
            $("#zxcxzcxzc2").css({"display": "none",});
            $("#zxcxzcxzc3").css({"display": "none",});
            $('#zxcxzcxzc1').html(qiwang_qwe[0] + qiwang_qwe[1]);
            $('.m_qw_btn_moren').html('');
            $('#zxcxzcxzc2').html('');
            $('#zxcxzcxzc3').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
            xinz_html = ["<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>"]
            $('#xzchenggong').append(xinz_html);
            $('#zxcxzcxzc1_put').attr('value', qiwang_sz[0]);
        }
         ;
		
		
		
		
		
		
		
        if (qiwang_sz.length ==2) {
            $("#zxcxzcxzc1").css({"display": "block",});
            $("#zxcxzcxzc2").css({"display": "block",});
            $("#zxcxzcxzc3").css({"display": "none",});
            qiwang_qwe_1 = qiwang_qwe[0] + qiwang_qwe[1]
            $('#zxcxzcxzc1').html(qiwang_qwe_1);

            qiwang_qwe_2 = qiwang_qwe[3] + qiwang_qwe[4]

            $('#zxcxzcxzc2').html(qiwang_qwe_2);
            $('.m_qw_btn_moren').html('');
            $('#zxcxzcxzc3').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
            xinz_html = [
                "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
            ]
            $('#xzchenggong').append(xinz_html);
            $('#zxcxzcxzc1_put').attr('value', qiwang_sz[0]);
            $('#zxcxzcxzc2_put').attr('value', qiwang_sz[1]);
        };

        if (qiwang_sz.length == 3) {
            $("#zxcxzcxzc1").css({"display": "block",});
            $("#zxcxzcxzc2").css({"display": "block",});
            $("#zxcxzcxzc3").css({"display": "block",});
            qiwang_qwe_1 = qiwang_qwe[0] + qiwang_qwe[1]
            $('#zxcxzcxzc1').html(qiwang_qwe_1);
            qiwang_qwe_2 = qiwang_qwe[3] + qiwang_qwe[4]
            $('#zxcxzcxzc2').html(qiwang_qwe_2);

            qiwang_qwe_3 = qiwang_qwe[6] + qiwang_qwe[7]
            $('#zxcxzcxzc3').html(qiwang_qwe_3);

            $('.m_qw_btn_moren').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
            xinz_html = [
                "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                "<input id='zxcxzcxzc3_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
            ]
            $('#xzchenggong').append(xinz_html);
            $('#zxcxzcxzc1_put').attr('value', qiwang_sz[0]);
            $('#zxcxzcxzc2_put').attr('value', qiwang_sz[1]);
            $('#zxcxzcxzc3_put').attr('value', qiwang_sz[2]);
        };
        if (qiwang_sz.length > 3) {
            $("#zxcxzcxzc1").css({"display": "block",});
            $("#zxcxzcxzc2").css({"display": "block",});
            $("#zxcxzcxzc3").css({"display": "block",});
            qiwang_qwe_1 = qiwang_qwe[0] + qiwang_qwe[1]
            $('#zxcxzcxzc1').html(qiwang_qwe_1);
            qiwang_qwe_2 = qiwang_qwe[3] + qiwang_qwe[4]
            $('#zxcxzcxzc2').html(qiwang_qwe_2);

            qiwang_qwe_3 = qiwang_qwe[6] + qiwang_qwe[7]
            $('#zxcxzcxzc3').html(qiwang_qwe_3);

            $('.m_qw_btn_moren').html('');
            xinz_html = $('.zxcxzcxzc_put').remove();
            xinz_html = [
                "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                "<input id='zxcxzcxzc3_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
            ]
            $('#xzchenggong').append(xinz_html);
            $('#zxcxzcxzc1_put').attr('value', qiwang_sz[0]);
            $('#zxcxzcxzc2_put').attr('value', qiwang_sz[1]);
            $('#zxcxzcxzc3_put').attr('value', qiwang_sz[2]);
        }

		console.log('期望的长度' + qiwang.length)
        console.log('数组的长度' + qiwang_sz.length)
        console.log('选择的数组第二' + qiwang_sz[1])
        console.log('期望属性' + qiwang)


    })


    $('.m_qw_zw_ul>li').click(function () {

        if ($(this).hasClass('m_qw_qctive')) {
            $(this).removeClass('m_qw_qctive');
        }
        else {
            $(this).addClass('m_qw_qctive');
        }

    });


})