//Ajax for check a username is taken

$(document).ready(function (){

    $("#id_username").blur(function (){
        var usrName = this.value
        $.ajax({
            type:'GET',
            url: '/check-username/?q=' + usrName,
            success: function (response){
                if(response.taken >0 ) { //如果用户名占用，将用户名的输入框背景色设置为红色，需要重新选择用户名。
                    $("#id_username").css("background-color", "#ff0000");
                }
                else//用户名未被占用，用户名输入框的背景色不变，与其它输入框颜色一致。
                    $("#id_username").css("background-color","#e8f8e9");
            }
        });
    });

});