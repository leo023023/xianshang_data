$(document).ready(function () {
    // if($.cookie('coo_bj')==null){
    //     $(".mizi_ku_cla").first().addClass("mizi_ku_cla_ac")
    // }
    // else{
    //     $(".mizi_ku_cla").first().removeClass("mizi_ku_cla_ac")
    // }
    // $("#ajax_bd a").each(function(){
    //     $this = $(this);
    //     if($this[0].href==String(window.location)){
    //             $(".mizi_ku_cla").removeClass("mizi_ku_cla_ac");
    //             $this.parent().addClass("mizi_ku_cla_ac");  //active表示被选中效果的类名
    //             $(this).attr("name","mizi_ku_nm");
    //     }
    // });
 

    $(".mizi_ku_cla").click(function () {
        // $.cookie('coo_bj',"1")
        $(this).attr("name","mizi_ku_nm");
        $(this).addClass("mizi_ku_cla_ac").siblings('input').removeClass("mizi_ku_cla_ac");
    });
    // // if($(".mizi_ku_cla:not(:first)").hasClass('mizi_ku_cla_ac')){
    //     $(".mizi_ku_cla:first").removeClass("mizi_ku_cla_ac")
    //     $(".mizi_ku_cla").first().addClass("mizi_ku_cla_ac")
    // }
    // else {
    //     $(".mizi_ku_cla").first().addClass("mizi_ku_cla_ac")
    // }

    // 这一段是控制名字列表的样式的
    // if(!$(".mizi_ku_cla").first().siblings('.mizi_ku_cla').hasClass('mizi_ku_cla_ac')){
    //     $(".mizi_ku_cla").first().removeClass("mizi_ku_cla_ac")
    // }
    // if(!$(".mizi_ku_cla").first().siblings('.mizi_ku_cla').no-hasClass('mizi_ku_cla_ac')){
    //     $(".mizi_ku_cla").first().addClass("mizi_ku_cla_ac")
    // }
    // else {
    //     $(".mizi_ku_cla").first().addClass("mizi_ku_cla_ac")
    // }
    // 这一段是控制目录的样式的
    $(".nav li").click(function () {
        //获取要显示或隐藏的对象
        var divShow = $(".content").children('.list');
        //判断当前对象是否被选中，如果没选中的话进入if循环
        if (!$(this).hasClass('selected_0')) {
            //获取当前对象的索引
            var index = $(this).index();
            //当前对象添加选中样式并且其同胞移除选中样式；
            $(this).addClass('selected_'+[index]).siblings('li').removeClass("selected_0").removeClass("selected_1").removeClass("selected_2").removeClass("selected_3").removeClass("selected_4").removeClass("selected_5");
            //索引对应的div块显示
            $(divShow[index]).show();

            // 索引对应的div块背景发送变化
            // $(divShow[index]).addClass(toString("active_"+[index]))
            //索引对应的div块的同胞隐藏
            $(divShow[index]).siblings('.list').hide();
        }
    });
    
    
    $(".vip_kaitong1").click(function () {
        $("#pay_tanchuang").show();
    })
    $(".sm_xj_mu_mb").click(function () {
        $("#pay_tanchuang").show();
    })
    $(".vip_bt").click(function () {
        $("#pay_tanchuang").show();
    })
    $(".mz_ku_mb").click(function () {
        $("#pay_tanchuang").show();
    })
    $(".vip_bt_2").click(function () {
        $("#pay_tanchuang").show();
    })
    $(".tc_bj_bj").click(function () {
        $("#pay_tanchuang").hide();
    })
    $(".pay_right .order_id_z>span").click(function () {
        $("#pay_tanchuang").hide();
    })
})



