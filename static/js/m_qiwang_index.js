// 移动端的期望选择
var single = new Dropdown({
    dom: 'singleSelect',//点击触发下拉的选择框的id
    type: 'multiple',//是单选还是多选 单选 single 多选 multiple
    title: '请选择期望性格(不超过3个)',//选择框title
    required: false,//是否必填 true:必填 ，false : 非必填
    requiredTip: '当前为必填项', // required为true，用户没有选择的提示文案
    dataArr: [
        {
            id: '1',
            cont: '优4雅'
        },
        {
            id: '2',
            cont: '爱国'
        },
        {
            id: '3',
            cont: '吉祥'
        },
        {
            id: '4',
            cont: '美好'
        },
        {
            id: '5',
            cont: '明理'
        },
        {
            id: '7',
            cont: '美德'
        },
        {
            id: '8',
            cont: '幸福'
        },
        {
            id: '13',
            cont: '浩大'
        },
        {
            id: '14',
            cont: '英俊'
        },
        {
            id: '15',
            cont: '健壮'
        },
        {
            id: '16',
            cont: '美丽'
        },
        {
            id: '17',
            cont: '安康'
        },
        {
            id: '18',
            cont: '年前'
        },
        {
            id: '19',
            cont: '快乐'
        },
        {
            id: '20',
            cont: '灵巧'
        },
        {
            id: '21',
            cont: '勇敢'
        },
        {
            id: '22',
            cont: '坚强'
        },
        {
            id: '23',
            cont: '稳重'
        },
        {
            id: '24',
            cont: '文静'
        },
        {
            id: '25',
            cont: '贤淑'
        },
        {
            id: '26',
            cont: '才华'
        },
        {
            id: '27',
            cont: '智慧'
        },
        {
            id: '28',
            cont: '谦虚'
        },
        {
            id: '29',
            cont: '正直'
        },
        {
            id: '30',
            cont: '纯洁'
        },
        {
            id: '31',
            cont: '志向'
        },
        {
            id: '33',
            cont: '杰出'
        },
        {
            id: '34',
            cont: '上进心'
        },
        {
            id: '35',
            cont: '财富'
        },
        {
            id: '36',
            cont: '优秀'
        },
    ],//选择的选项数据，为3的倍数，不足用 '' 代替
    success: function (resp) { // 回调函数
        console.log(resp)
        var xinz_html
        if (resp.length > 0) {
            // $('#singleSelect').val(resp[0].cont);
            // for (var i=0;i<resp.length;i++){
            //     $(zxcvcv).html(resp[i].cont);
            // }
            $("#singleSelect").attr("placeholder", '');
            // $(".m_xingge_tags_tags").css({"display": "block",})

            if (resp.length == 1) {
                $("#zxcxzcxzc1").css({"display": "block",});
                $("#zxcxzcxzc2").css({"display": "none",});
                $("#zxcxzcxzc3").css({"display": "none",});
                $('#zxcxzcxzc1').html(resp[0].cont);
                $('#zxcxzcxzc2').html('');
                $('#zxcxzcxzc3').html('');
                xinz_html =$('.zxcxzcxzc_put').remove();
                xinz_html = ["<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>"]
                $('#xzchenggong').append(xinz_html);
                $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                // $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                // $('#zxcxzcxzc2_put').attr('value','');
                // $('#zxcxzcxzc3_put').attr('value','');

            }
            ;
            if (resp.length == 2) {
                $("#zxcxzcxzc1").css({"display": "block",});
                $("#zxcxzcxzc2").css({"display": "block",});
                $("#zxcxzcxzc3").css({"display": "none",});
                $('#zxcxzcxzc1').html(resp[0].cont);
                $('#zxcxzcxzc2').html(resp[1].cont);
                $('#zxcxzcxzc3').html('');
                xinz_html =$('.zxcxzcxzc_put').remove();
                xinz_html = [
                    "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                    "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                ]
                $('#xzchenggong').append(xinz_html);
                $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                // $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                // $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                // $('#zxcxzcxzc3_put').attr('value','');

            }
            ;
            if (resp.length == 3) {
                $("#zxcxzcxzc1").css({"display": "block",});
                $("#zxcxzcxzc2").css({"display": "block",});
                $("#zxcxzcxzc3").css({"display": "block",});
                $('#zxcxzcxzc1').html(resp[0].cont);
                $('#zxcxzcxzc2').html(resp[1].cont);
                $('#zxcxzcxzc3').html(resp[2].cont);
                xinz_html =$('.zxcxzcxzc_put').remove();
                xinz_html = [
                    "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                    "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                    "<input id='zxcxzcxzc3_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                ]
                $('#xzchenggong').append(xinz_html);
                $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                $('#zxcxzcxzc3_put').attr('value',resp[2].id);
                // $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                // $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                // $('#zxcxzcxzc3_put').attr('value',resp[2].id);
            }
            ;
            if (resp.length > 3) {
                $("#zxcxzcxzc1").css({"display": "block",});
                $("#zxcxzcxzc2").css({"display": "block",});
                $("#zxcxzcxzc3").css({"display": "block",});
                $('#zxcxzcxzc1').html(resp[0].cont);
                $('#zxcxzcxzc2').html(resp[1].cont);
                $('#zxcxzcxzc3').html(resp[2].cont);
                xinz_html =$('.zxcxzcxzc_put').remove();
                xinz_html = [
                    "<input id='zxcxzcxzc1_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                    "<input id='zxcxzcxzc2_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                    "<input id='zxcxzcxzc3_put' class='zxcxzcxzc_put' name='qiwang' style='display: none'>",
                ]
                $('#xzchenggong').append(xinz_html);
                $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                $('#zxcxzcxzc3_put').attr('value',resp[2].id);
                // $('#zxcxzcxzc1_put').attr('value',resp[0].id);
                // $('#zxcxzcxzc2_put').attr('value',resp[1].id);
                // $('#zxcxzcxzc3_put').attr('value',resp[2].id);
            }
            ;
        }
        else {
            $("#zxcxzcxzc1").css({"display": "none",});
            $("#zxcxzcxzc2").css({"display": "none",});
            $("#zxcxzcxzc3").css({"display": "none",});
            $('#zxcxzcxzc1').html('');
            $('#zxcxzcxzc2').html('');
            $('#zxcxzcxzc3').html('');
            xinz_html =$('.zxcxzcxzc_put').remove();
        }
    }
})



