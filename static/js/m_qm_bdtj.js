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
})