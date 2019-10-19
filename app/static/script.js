$(document).ready(function(){
    $("form").submit(function(e){
        e.preventDefault(e);
    });
    $(".fileinput-upload").removeAttr("type");
    $(".fileinput-upload").attr("id","upload_button");
    $(".fileinput-upload").on('click', function() { 
        console.log("i'm here1")
        $(".spinner-grow").show()
        var form = document.getElementById('form');
        var formData = new FormData(form);
        var xhr = new XMLHttpRequest();
        // Add any event handlers here...
        xhr.open('POST', 'https://deeppoet-2.appspot.com/upload', true);
        xhr.send(formData);
        xhr.onload  = function() {
            var jsonResponse = JSON.parse(xhr.responseText);
            $(".clearfix").css("font-weight","bold")
            $(".clearfix").css("color","green")
            $(".kv-preview-thumb").each(function(index){
                thumb = $(this)
                $(thumb).find(".clearfix").append(jsonResponse[index]['class'])
                $(".spinner-grow").hide(50)
            })
         };
    }); 
    
})
