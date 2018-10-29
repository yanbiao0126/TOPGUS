$(function(){
    $('#submit').click(function(){
        $('#pay').show();
    });
    $('.details').click(function(){
        $('.goods').toggle(500);
    })
    $('#delete').click(function(){
        isss = confirm('确认删除');
        if(isss){
            hrefs = $(this).attr('data-href');
            window.location.href = hrefs;
        }
    });
    var ind = document.getElementsByClassName('inde')
    for(var i=0;i<ind.length;i++){
        ind[i].innerHTML = '关键词 '+(i+1);
    }
})