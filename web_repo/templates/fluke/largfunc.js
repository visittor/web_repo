/**
 * Created by PHURINPAT on 4/7/2560.
 */

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function edit_borrow_admin_button(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_borrow.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            id: i,
        },
        dataType: 'json',

        success:edit_borrow_admin
    });
}


function summit_edit_borrow(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_borrow.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            id: i,
            note: document.getElementById("note").value,
            to_student: document.getElementById("dm_std").value,
            to_advisor: document.getElementById("dm_tch").value
        },
        dataType: 'json',

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
        type: 'get',
        data: {
            requestByAjax: 1,
        },
        dataType: 'json',

        success:call_borrow_admin
    });
}


function edit_return_admin_button(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_return.json";
    alert(url);
    $.ajax({
        url: url,
        type: 'get',
        data: {
            id: i,
        },
        dataType: 'json',

        success:edit_return_admin
    });
}


function summit_edit_return(i)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_return.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            id: i,
            note: document.getElementById("note").value,
            to_student: document.getElementById("dm_std").value,
            to_advisor: document.getElementById("dm_tch").value
        },
        dataType: 'json',

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
        type: 'get',
        data: {
            requestByAjax: 1,
        },
        dataType: 'json',

        success:call_return_admin
    });
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


function go_main_category()
{
    var url = document.getElementById('url_').innerHTML+"admin_main_category.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            requestByAjax: 1
        },
        dataType: 'json',

        success:call_main_category
    });
}

function summit_add_category(a)
{
    var url = document.getElementById('url_').innerHTML+"admin_insert_main_category.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            name: a
        },
        dataType: 'json',

        success:go_main_category
    });
}

function send_new_category_name(a,b)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_main_category.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            old_name: a,
            new_name: b
        },
        dataType: 'json',

        success:function (respond) {
            alert(a+" "+typeof a);
            alert(b+" "+typeof b);
            if (respond.exception == 1){
                alert('wrong');
            }
            go_main_category();
        }
    });
}

function delete_main_category(name)
{
    var url = document.getElementById('url_').innerHTML+"admin_delete_main_category.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            name: name
        },
        dataType: 'json',

        success:function (respond) {
            alert(name+" "+typeof name);
            if (respond.exception == 1){
                alert('wrong');
            }
            go_main_category();
        }
    });
}

function go_sub_category()
{
    var url = document.getElementById('url_').innerHTML+"admin_sub_category.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            requestByAjax: 1
        },
        dataType: 'json',

        success:call_sub_category
    });
}

function send_new_subcategory_name(main,old,new_name)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_sub_category.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            main_category: main,
            old_name: old,
            new_name: new_name
        },
        dataType: 'json',

        success:function (respond) {
            if (respond.exception == 1){
                alert('wrong');
            }
            go_main_category();
        }
    });
}

function delete_sub_category(main,sub)
{
    var url = document.getElementById('url_').innerHTML+"admin_delete_sub_category.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            main_category: main,
            sub_category: sub
        },
        dataType: 'json',

        success:function (respond) {
            if (respond.exception == 1){
                alert('wrong');
            }
            go_sub_category();
        }
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function go_list_devicetype()
{
    var url = document.getElementById('url_').innerHTML+"admin_type.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            requestByAjax: 1,
        },
        dataType: 'json',

        success:call_list_devicetype
    });
}

function send_new_devicetype_name(a,b,c)
{
    var url = document.getElementById('url_').innerHTML+"admin_edit_type.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            old_name: a,
            new_name: b,
            code: c
        },
        dataType: 'json',

        success:function (respond) {
            if (respond.exception == 1){
                alert('wrong');
            }
            go_list_devicetype();
        }
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function go_list_place()
{
    var url = document.getElementById('url_').innerHTML+"admin_storage.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            requestByAjax: 1,
        },
        dataType: 'json',

        success:function (respond) {
            call_list_place();
        }
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function go_list_device()
{
    var url = document.getElementById('url_').innerHTML+"admin_device.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            requestByAjax: 1,
        },
        dataType: 'json',

        success:function (respond) {
            call_list_device();
        }
    });
}