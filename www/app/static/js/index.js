/**
 * Created by user on 18-9-26.
 */

window.onload=function(){
    var len = document.getElementById('number');
    var box = document.getElementById('box');
    var addbtn = document.getElementById('addbtn');
    var arr = Array();
    var text = '<div class="mui-input-row"><label>请输入商品</label><input type="text" class="mui-input-clear" placeholder="请输入关键字" data-input-clear="5"><span class="mui-icon mui-icon-clear mui-hidden"></span></div>';
    len.onchange=function() {
        var inpt = box.getElementsByTagName('input');
        var lens = inpt.length;
        arr = [];
        for(var i=0;i<lens;i++){
            arr[i] = inpt[i].value;
        }
        box.innerHTML = '';
        for (var i = 0; i < Number(len.value); i++) {
            box.innerHTML += text;
        }
        var inpt = box.getElementsByTagName('input');
        var label = box.getElementsByTagName('label');
        var lest = inpt.length>arr.length?arr.length:inpt.length;
        for(var i=0;i<lest;i++){
            inpt[i].value = arr[i];
        }
        for(var i=0;i<inpt.length;i++){
            inpt[i].name='data'+i;
            label[i].innerHTML = '关键词 '+(i+1)
        }
    }



    addbtn.onclick=function () {
        if (Number(len.value)<20){
            var inpt = box.getElementsByTagName('input');
            var lens = inpt.length;
            arr=[];
            for(var i=0;i<lens;i++){
                arr[i] = inpt[i].value;
            }
            len.value=Number(len.value)+1;
            len.name=Number(len.name)+1;
            box.innerHTML+=text;
            var inpt = box.getElementsByTagName('input');
            var label = box.getElementsByTagName('label');
            for(var i=0;i<lens;i++){
                inpt[i].value = arr[i];
            }
            for(var i=0;i<inpt.length;i++){
                inpt[i].name='data'+i;
                label[i].innerHTML = '关键词 '+(i+1)
            }
        }
    }
}