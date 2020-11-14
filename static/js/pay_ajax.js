$(document).ready(function () {
    $("#tc_pay_tijiao").click(function () {
        var phone = document.getElementById('telephne').value;
        if(!(/^1(3|4|5|6|7|8|9)\d{9}$/.test(phone))){
        alert("请输入有效的手机号码!");
            return false;
        }
        else {
        	var sUsrAgent=navigator.userAgent;  
    		var isSF=sUsrAgent.indexOf("Safari")!=-1;
    		var moz = (typeof document.implementation != 'undefined')   && (typeof document.implementation.createDocument != 'undefined');
    		if(isSF){
    			var data = {}
            	data = $("#pay_form").serialize();
	            $.ajax({
	                type:'post',
	                url:'/pay/',
	                data:data,
	                dataType:'json',
	                success: function(pay_url) {
	                    // alert("请求成功")
	                    parent.location.href=pay_url
	                },
	                error: function() {
	                     alert("请求失败,请刷新页面重新提交")
	                }
	            })
	            $("#pay_tanchuang").hide();	
    		}
    		else if(moz){
    			var data = {}
            	data = $("#pay_form").serialize();
            	myRequest = new XMLHttpRequest(); 
	            $.ajax({
	                type:'post',
	                url:'/pay/',
	                data:data,
	                dataType:'json',
	                success: function(pay_url) {
	                    // alert("请求成功")
	                    pay_url = pay_url.replace('http://qmg365.com/csjg/','')
	                    parent.location.href=pay_url
	                },
	                error: function() {
	                     alert("请求失败,请刷新页面重新提交")
	                }
	            })
	            $("#pay_tanchuang").hide();		
    		}
    		else{
    			var data = {}
            	data = $("#pay_form").serialize();
	            $.ajax({
	                type:'post',
	                url:'/pay/',
	                data:data,
	                success: function(pay_url) {
	                    // alert("请求成功")
	                    window.location.href=pay_url
	                },
	                error: function() {
	                     alert("请求失败,请刷新页面重新提交")
	                }
	            })
	            $("#pay_tanchuang").hide();		
    		}
        	
    
        }
    })

})