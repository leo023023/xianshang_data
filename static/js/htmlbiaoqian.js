// $(document).ready(function () {
//     $(function () {
//         $.ajax({
//             type: 'get',
//             url: '/shujuku/',
//             dataType:'json',
//             success: function (data) {
//                 // alert("请求成功")
//                 for (let i=0;i<5;i++){
//                     $('.wz_contant_active').html(
//                         '<a href="http://www.tell520.com/langman/2891820.html">'+
//                             '<div class="info">'+
//                                 '<div class="title">'+
//                                     data.article_title[i]
//                                 +'</div>'+
//                                 '<div class="desc">'+
//                                     data.article_content[i]
//                                 +'</div>'+
//                             '</div>'+
//                         '</a>'
//                     )
//                 }
//                 // $(".desc").html(data.article_content[0]);
//                 // console.log('123ttttt')
//                 console.log(data.article_title[0])
//                 // console.log(data)
//                 console.log('aaaaabbbbb')
//             },
//             error: function () {
//                 alert("请求失败,请刷新页面ahhhaaaa重新提交")
//             }
//         })
//     })
// })