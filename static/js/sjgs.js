function check_form(){
    var phone = document.getElementById('telephne').value;
    if(!(/^1(3|4|5|6|7|8|9)\d{9}$/.test(phone))){
        alert("请输入有效的手机号码!");
        return false;
    }
    
}

