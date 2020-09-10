$(function () {
	//鼠标移入显示左右箭头和关闭按钮
	var timer = '';
	$('.hwhm_Cooldog_container').mouseover(function () {
		// $('.btn_left').show('1000');
		// $('.btn_right').show('1000');
		// $('.btn_close').show('1000');
		clearInterval(timer);
	});

	var arr = ['hwhm_p1', 'hwhm_p2', 'hwhm_p3', 'hwhm_p4', 'hwhm_p5', 'hwhm_p6', 'hwhm_p7', 'hwhm_p8', 'hwhm_p9', 'hwhm_p10', 'hwhm_p11', 'hwhm_p12'];
	var index = 0;

	//上一张
	$('.hwhm_btn_left').on('click', function () {
		hwhm_btn_left();
	});

	//下一张
	$('.hwhm_btn_right').on('click', function () {
		hwhm_btn_right();
	});


	//滑动上一张
	$('.hwhm_Cooldog_content').on('swipeleft', function () {
		hwhm_btn_left();
	});

	//滑动下一张
	$('.hwhm_Cooldog_content').on('swiperight', function () {
		hwhm_btn_right();
	});




	//图片自动轮播
	timer = setInterval(hwhm_btn_right, 2000);

	//点击上一张的封装函数
	function hwhm_btn_left() {
		arr.unshift(arr[6]);
		arr.pop();
		$('.hwhm_Cooldog_content li').each(function (i, e) {
			$(e).removeClass().addClass(arr[i]);
		})
		index--;
		if (index < 0) {
			index = 6;
		}
		show();
	}

	//点击下一张的封装函数
	function hwhm_btn_right() {
		arr.push(arr[0]);
		arr.shift();
		$('.hwhm_Cooldog_content li').each(function (i, e) {
			$(e).removeClass().addClass(arr[i]);
		})
		index++;
		if (index > 6) {
			index = 0;
		}
		show();
	}

	//点击底部的按钮切换图片
	$('.hwhm_buttons a').each(function () {
		$(this).on('click', function () {
			var myindex = $(this).index();
			var mindex = myindex - index;
			if (mindex == 0) {
				return;
			}
			else if (mindex > 0) {
				var newarr = arr.splice(0, mindex);
				//$.merge() 函数用于合并两个数组内容到第一个数组
				arr = $.merge(arr, newarr);
				$('.hwhm_Cooldog_content li').each(function (i, e) {
					$(e).removeClass().addClass(arr[i]);
				})
				index = myindex;
				show();
			}
			else if (mindex < 0) {
				//reverse() 方法用于颠倒数组中元素的顺序。
				arr.reverse();
				var oldarr = arr.splice(0, -mindex);
				arr = $.merge(arr, oldarr);
				arr.reverse();
				$('.hwhm_Cooldog_content li').each(function (i, e) {
					$(e).removeClass().addClass(arr[i]);
				})
				index = myindex;
				show();
			}
		})
	})

	//底部按钮高亮
	function show() {
		$('.hwhm_buttons a').eq(index).addClass('hwhm_color').siblings().removeClass('hwhm_color');
	}

})