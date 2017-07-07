/**
 * Created by PHURINPAT on 4/7/2560.
 */

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function edit_borrow_admin_button(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_borrow.json";
    $.ajax({
        url: url,
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            id: i,
        },
        dataType: 'json', //หรือ json หรือ xml

        success:edit_borrow_admin
    });
}


function summit_edit_borrow(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_borrow.json";
    $.ajax({
        url: url,
        type: 'post', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            id: i,
            note: document.getElementById("note").value,
            to_student: document.getElementById("dm_std").value,
            to_advisor: document.getElementById("dm_tch").value
        },
        dataType: 'json', //หรือ json หรือ xml

        success: function(respond){
            if(respond.exception == 1){
                alert('something wrong');
            }
            cancle_edit_borrow();
        }
    });
}


function cancle_edit_borrow()
{
    var url = document.getElementById('url_').innerHTML+"admin_borrow.json";
    $.ajax({
        url: url,
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            requestByAjax: 1,
        },
        dataType: 'json', //หรือ json หรือ xml

        success:call_borrow_admin
    });
}


function edit_return_admin_button(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_return.json";
    alert(url);
    $.ajax({
        url: url,
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            id: i,
        },
        dataType: 'json', //หรือ json หรือ xml

        success:edit_return_admin
    });
}


function summit_edit_return(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_return.json";
    $.ajax({
        url: url,
        type: 'post', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            id: i,
            note: document.getElementById("note").value,
            to_student: document.getElementById("dm_std").value,
            to_advisor: document.getElementById("dm_tch").value
        },
        dataType: 'json', //หรือ json หรือ xml

        success:function (respond) {
            if (respond.exception == 1){
                alert('wrong');
            }
            cancle_edit_return();
        }
    });
}

function cancle_edit_return()
{
    var url = document.getElementById('url_').innerHTML+"admin_return.json";
    $.ajax({
        url: url,
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            requestByAjax: 1,
        },
        dataType: 'json', //หรือ json หรือ xml

        success:call_return_admin
    });
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


function go_main_category()
{
    var url = document.getElementById('url_').innerHTML+"admin_main_category.json";
    $.ajax({
        url: url,
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            requestByAjax: 1
        },
        dataType: 'json', //หรือ json หรือ xml

        success:call_main_category
    });
}


function send_new_category_name(a,b)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_main_category.json";
    $.ajax({
        url: url,
        type: 'post', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            old_name: a,
            new_name: b
        },
        dataType: 'json', //หรือ json หรือ xml

        success:function (respond) {
            if (respond.exception == 1){
                alert('wrong');
            }
            go_main_category();
        }
    });
}
