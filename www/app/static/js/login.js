$(function(){
    var submi = true;
    $('#get_code').click(function() {
        if(submi){
            var dat = $('#phone').val();
            var myreg=/^[1][3,4,5,7,8][0-9]{9}$/;
            if(!myreg.test(dat)) {
                alert('手机格式错误');
            } else {
                submi = false;
                var shi = 60;
                function tim(){
                    setTimeout(function(){
                        shi--;
                        if(shi>0){
                            $('#get_code').text(shi+'秒后重试');
                            tim();
                        }else{
                            $('#get_code').text('获取验证码');
                            submi = true;
                        }
                    },1000)
                }

                $.ajax({
                    type: "POST",
                    url: "/code",
                    data: {phone: dat},
                    dataType: "json",
                    success: function (data) {
                        $('#get_code').text('获取成功');
                        tim();
                    }
                });
            }
        }
    });
})