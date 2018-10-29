/**
 * Created by user on 18-9-30.
 */
$('.sh').click(function(){
    // var is_ok=confirm('确认审核？');
    // var data=$(this).attr('data');
    // if(is_ok){
    //
    // }else{
    //     var test = document.getElementById('hre');
    //     test.onclick = function(e) {
    //         stopDefault(e);
    //     }
    // }
})

var obj = null;
var Obj = null;

function noteAjax(obj) {
    Obj = obj;
    obj=$(obj);
    $('.am-modal-prompt-input').val(Obj.innerHTML)
    $('#my-prompt').modal({
      relatedTarget: this,
      onConfirm: function(e) {
        // alert('你输入的是：' + e.data || '')
        $.ajax({
            //请求方式
            type:'POST',
            //发送请求的地址
            url:'https://www.daqianwang.top/TopGus/Data/note',
            //服务器返回的数据类型
            dataType:'json',
            //发送到服务器的数据，对象必须为key/value的格式，jquery会自动转换为字符串格式
            data:{orderno:obj.attr('data'),notes:e.data},
            success:function(data){
                //请求成功函数内容
                Obj.innerHTML = e.data;
            },
            error:function(jqXHR){
                //请求失败函数内容
                alert('修改失败');
            }
        });
      },
      onCancel: function(e) {
        alert('不想说!');
      }
    });
};
