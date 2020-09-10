$(document).ready(function () {
    (function ($) {
        $.getUrlParam = function (name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
            if (r != null) return unescape(r[2]);
            return null;
        }
    })(jQuery);
    $(function () {
        // alert();
        if ($.getUrlParam('goodname')) {
            $(".kong_tishi_dv").css({"display": "block",})
            setTimeout(function (event) {
                $(".kong_tishi_dv").css({"display": "none",});
            }, 3500);
        }
    });
    // $(function () {
    //     $(".desc").html("<span style='color: red'>11111111111</span>");
    // })
})