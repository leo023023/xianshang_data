$(function () {
    // 设置出生时间还是预产期
    $(".m_xb_xz_nv").click(function () {
        $("#m_cssj_bd_title").text("出生时间");
        // parent.location.reload();
        // val_jsjs =3;
    });
    $(".m_xb_xz_nan").click(function () {
        $("#m_cssj_bd_title").text("出生时间");
        // parent.location.reload();
        val_jsjs = 3;
    });
    $(".m_xb_xz_nobirth").click(function () {
        $("#m_cssj_bd_title").text("预产期");
        // parent.location.reload();
        val_jsjs = 3;
    });


    // function m_bdtj_bdtj(){
    //     var m_qm_si_name = document.getElementById('m_qm_si_name').value;
    //     var name = document.getElementById('name').value;
    //     var phone = document.getElementById('user_phone').value;
    // }
})

$(document).ready(function () {
    $(".m_grqm_flbg").click(function () {
        $(this).css('z-index', '2');
        $(this).addClass('m_grqm_flbg_active');
        $(this).removeClass('m_grqm_flbg_active_no');
        $('.m_mzdf_flbg').removeClass('m_mzdf_flbg_active')
        $('.m_mzdf_flbg').css('z-index', '1');
        $('.m_dingzhi').removeClass('qimingordafen_dis');
        $('#m_index_biaodan .m_xb_xz_ul').css('display','flex');
        $('.m_xb_xz_nobirth').removeClass('qimingordafen_dis');
        $(".m_qsr_xingnanme").text("姓氏");
        $("#m_bd_xx_name").attr('placeholder','请输入姓氏');
        $(".m_xb_xz_nan").prop("checked",false);
        $(".m_xb_xz_nv").prop("checked",false);
        $(".m_xb_xz_nobirth").prop("checked",true);
        $(".m_xb_xz_nobirth").addClass('m_xb_xz_active');
        $(".m_xb_xz_nan").removeClass('m_xb_xz_active');
        $(".m_xb_xz_nv").removeClass('m_xb_xz_active');
        $("#m_index_biaodan .m_xb_xz_ul > li").removeClass('width_48');
        $('#m_biaodan_shouji_form_tijiao').removeClass('bd_lijiceming_hide');
        $('.bd_lijiceming').addClass('bd_lijiceming_hide');
    });
    $(".m_mzdf_flbg").click(function () {
        $(this).css('z-index', '2');
        $('.m_grqm_flbg').css('z-index', '1');
        $(this).addClass('m_mzdf_flbg_active');
        $('.m_grqm_flbg').removeClass('m_grqm_flbg_active');
        $('.m_grqm_flbg').addClass('m_grqm_flbg_active_no');
        $('.m_dingzhi').addClass('qimingordafen_dis');
        $('#m_index_biaodan .m_xb_xz_ul').css('display','block');
        $('.m_xb_xz_nobirth').addClass('qimingordafen_dis');
        $(".m_qsr_xingnanme").text("姓名");
        $("#m_bd_xx_name").attr('placeholder','请输入姓名');
        $(".m_xb_xz_nan").prop("checked",true);
        $(".m_xb_xz_nobirth").prop("checked",false);
        $(".m_xb_xz_nv").prop("checked",false);
        $(".m_xb_xz_nan").addClass('m_xb_xz_active');
        $(".m_xb_xz_nv").removeClass('m_xb_xz_active');
        $(".m_xb_xz_nobirth").removeClass('m_xb_xz_active');
        $("#m_index_biaodan .m_xb_xz_ul > li").addClass('width_48');
        $('#m_biaodan_shouji_form_tijiao').addClass('bd_lijiceming_hide');
        $('.bd_lijiceming').removeClass('bd_lijiceming_hide');
    });

    $('#bd_lijidafeng').click(function () {
        // var mizi_ku_nm = document.getElementByclassName('name_xingming').val();
        // var birthtime = document.getElementid('date-input').value;

        var mizi_ku_nm = $('#m_bd_xx_name').val();
        // var xingbie_js = $('input[name="xingbie"]:checked').val();
        var xingbie_js = $('.m_xb_xz_active').val();
        var birthtime = $('#demo_datetime').val();
        var birthplace = $('#picker').val();

        var myRegttzw = /^[\u4e00-\u9fa5]+$/;
        console.log('这个是获取懂啊的名字', mizi_ku_nm)
        console.log('这个是获取懂啊的出生日期', birthtime)
        console.log('这个是获取的性别', xingbie_js)
        console.log('这个是获取懂啊的地点', birthplace)
        if ($('#m_bd_xx_name').val() == '') {
            alert("请输入正确的名字信息!");
            return false;
        }
        else if ($('#m_bd_xx_name').val().length < 2)
        {
            alert("请输入完整的名字信息!");
            return false;
        }
        else if (myRegttzw.test(mizi_ku_nm)) {
            console.log('获取数据成功');
            url_js = 'http://www.qmg365.com/'+'qmb_dafeng_qd?'+'　&name='+mizi_ku_nm+"&xb="+xingbie_js+'&birthtime='+birthtime+'&birthplace='+birthplace
            window.location.href=url_js
        }
        else {
            alert("名字格式有误，请重新输入!");
        }

    })

})