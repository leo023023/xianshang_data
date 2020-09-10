!function (o) {
    o.fn.numberRock = function (e) {
        var n = o.extend({}, {lastNumber: 100, duration: 2e3, easing: "swing"}, e);
        o(this).animate({num: "numberRock"}, {
            duration: n.duration, easing: n.easing, complete: function () {
            }, step: function (e, i) {
                o(this).html(parseInt(i.pos * n.lastNumber))
            }
        })
    }
}(jQuery), $(function () {
    var e, t, n, o, a, s, l = $("#video-slide").find(".bd");
    function r() {
        t && (t.pause(), $(t).parent().next(".play-control").show(), $(t).remove(), t = null)
    }
    function d(i) {
        n = new Swiper(i, {
            loop: !0,
            navigation: {nextEl: ".next", prevEl: ".prev"},
            pagination: {el: ".pages"},
            on: {
                init: function () {
                    var e = $(i).find(".li.swiper-slide-active").find(".alink").data("bgurl");
                    $("#approve-bg").css({backgroundImage: "url(" + e + ")"})
                }, slideChange: function () {
                    var e = n.slides[n.activeIndex], i = $(e).find(".alink").data("bgurl");
                    $("#approve-bg").css({backgroundImage: "url(" + i + ")"})
                }, slideChangeTransitionEnd: function () {
                    $("div.lazy").lazyload(), $(window).trigger("scroll")
                }
            }
        })
    }
    setInterval(function () {
        l.find(".li:eq(1)").addClass("active").siblings().removeClass("active"), l.find(".li:eq(0)").appendTo(l)
    },
        5e3), new Swiper("#taocan-items", {loop: !0, slidesPerView: "auto"}), new Swiper("#ding-items", {
        loop: !0,
        slidesPerView: "auto"
    }),
        a = new Swiper("#gonglue-column", {
        slidesPerView: "auto",
        spaceBetween: 12,
        centeredSlidesBounds: !0
    }),
        s = "#article-slide", o && o.destroy(), o = new Swiper(s, {
        slidesPerView: "auto",
        spaceBetween: 12,
        controller: a,
        on: {
            slideChange: function () {
                $("#gonglue-column .li").eq(this.activeIndex).addClass("on").siblings().removeClass("on")
            }, slideChangeTransitionEnd: function () {
                $("div.lazy").lazyload(), $(window).trigger("scroll")
            }
        }
    }),
        $(document).scroll(function () {
        150 < $(this).scrollTop() ? $("#fix-tip").addClass("show") : $("#fix-tip").removeClass("show")
    });
    if($('.gonglue_neirong2').css('transform')=='translate3d(-1445px,0px,0px)'){
        $('.gonglue_bt').css('transform','translate3d(-168px,0px,0px)')
    };
    if($('.gonglue_neirong2').css('transform')=='translate3d(-1734px,0px,0px)'){
        $('.gonglue_bt').css('transform','translate3d(-168px,0px,0px)')
    }

});