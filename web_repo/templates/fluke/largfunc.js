/**
 * Created by PHURINPAT on 4/7/2560.
 */

function test_borrow()
{
    var url = document.getElementById('url_').innerHTML+"test_admin_return.json";
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

function edit_borrow_admin_button(i)
{
    var url = document.getElementById('url_').innerHTML+"test_admin_borrow.json";
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

function test_return()
{
    var url = document.getElementById('url_').innerHTML+"test_admin_return.json";
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