// $(".dianji_1").click(function () {
//     dnum_1 = dnum_1 + 1;
//     if (dnum_1 % 2 != 0) {
//         $(".fanwei_1").css("height","100px")
//         $(".guanggao_1").animate({
//             top: "10px"
//         }, 50)
//         $(".dianji_1").css({"background":"url(./templates/images/fq_arrow_up.svg)","background-repeat":"no-repeat",
//     "background-position":"center",})
//         $(".fq_h3_1").css({"background-color":"#0C1222","color":"#fff",})
//     }
//     else {
//          $(".fanwei_1").css("height","0px")
//         $(".guanggao_1").stop(true, true).animate({
//             top: "-150px"
//         }, 50)
//         $(".dianji_1").css({"background":"url(./templates/images/fq_arrow_down.svg)","background-repeat":"no-repeat",
//     "background-position":"center",})
//         $(".dianji_1").css({"background":"url(./templates/images/fq_arrow_down.svg)","background-repeat":"no-repeat",
//     "background-position":"center",})
//         $(".fq_h3_1").css({"background-color":"#fff","color":"#0C1222"})
//     }
// })
var dnum_1 = 0
dnum_2 = 0
dnum_3 = 0
dnum_4 = 0
$(".fq_toubu_1").click(function () {
    dnum_1 = dnum_1 + 1;
    if (dnum_1 % 2 != 0) {
        $(".fanwei_1").css("height", "100px")
        $(".guanggao_1").animate({
            top: "10px"
        }, 500)
        $(".dianji_1").css({
            "background": "url(/static/images/fq_arrow_up.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_1").css({"background-color": "#0C1222", "color": "#fff",})
    }
    else {
        $(".fanwei_1").css("height", "0px")
        $(".guanggao_1").stop(true, true).animate({
            top: "-150px"
        }, 50)
        $(".dianji_1").css({
            "background": "url(/static/images/fq_arrow_down.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_1").css({"background-color": "#fff", "color": "#0C1222"})
    }
})
$(".fq_toubu_2").click(function () {
    dnum_2 = dnum_2 + 1;
    if (dnum_2 % 2 != 0) {
        $(".fanwei_2").css("height", "100px")
        $(".guanggao_2").animate({
            top: "10px"
        }, 500)
        $(".dianji_2").css({
            // ../static/images/mzys_lunbo_bj.png
            "background": "url(/static/images/fq_arrow_up.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_2").css({"background-color": "#0C1222", "color": "#fff"})
    }
    else {
        $(".fanwei_2").css("height", "0px")
        $(".guanggao_2").stop(true, true).animate({
            top: "-150px"
        }, 50)
        $(".dianji_2").css({
            "background": "url(/static/images/fq_arrow_down.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_2").css({"background-color": "#fff", "color": "#0C1222"})
    }
})
$(".fq_toubu_3").click(function () {
    dnum_3 = dnum_3 + 1;
    if (dnum_3 % 2 != 0) {
        $(".fanwei_3").css("height", "100px")
        $(".guanggao_3").animate({
            top: "10px"
        }, 500)
        $(".dianji_3").css({
            "background": "url(/static/images/fq_arrow_up.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_3").css({"background-color": "#0C1222", "color": "#fff"})
    }
    else {
        $(".fanwei_3").css("height", "0px")
        $(".guanggao_3").stop(true, true).animate({
            top: "-150px"
        }, 50)
        $(".dianji_3").css({
            "background": "url(/static/images/fq_arrow_down.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_3").css({"background-color": "#fff", "color": "#0C1222"})
    }
})
$(".fq_toubu_4").click(function () {
    dnum_4 = dnum_4 + 1;
    if (dnum_4 % 2 != 0) {
        $(".fanwei_4").css("height", "100px")
        $(".guanggao_4").animate({
            top: "10px"
        }, 500)
        $(".dianji_4").css({
            "background": "url(/static/images/fq_arrow_up.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_4").css({"background-color": "#0C1222", "color": "#fff"})
    }
    else {
        $(".fanwei_4").css("height", "0px")
        $(".guanggao_4").stop(true, true).animate({
            top: "-150px"
        }, 50)
        $(".dianji_4").css({
            "background": "url(/static/images/fq_arrow_down.svg)", "background-repeat": "no-repeat",
            "background-position": "center",
        })
        $(".fq_h3_4").css({"background-color": "#fff", "color": "#0C1222"})
    }
})