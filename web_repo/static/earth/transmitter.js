/**
 * Created by PHURINPAT on 16/7/2560.
 */
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Rent Item */

function request_list_device_from_container(a, b)
{
    var url = document.getElementById('url_').innerHTML+"search_item.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            main_category: a,
            sub_category: b
        },
        dataType: 'json',

        success:call_list_device_from_container
    });
}

function send_borrow_request(a) {
    // console.log('อย่นี่นะ')
    var url = document.getElementById('url_').innerHTML+"order_item.json";
    // console.log(a);
    $.ajax({
        url: url,
        type: 'post',
        data: {
            id: a
        },
        dataType: 'json',

        success: function(respond){
            if(respond.exception == 1){
                alert('something wrong');
            }
            else{
                alert('ส่งคำขอเรียบร้อย')
            }
            request_list_device_from_container('', '');
        }
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Approve Item */

function request_order_detail()
{
    var url = document.getElementById('url_').innerHTML+"view_order_detail.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            request_order_detail: 1
        },
        dataType: 'json',

        success:call_order_detail
    });
}

function send_delete_order(a)
{
    var url = document.getElementById('url_').innerHTML+"delete_order.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            id: a
        },
        dataType: 'json',

        success: function(respond){
            if(respond.exception == 1){
                alert('something wrong');
            }
            else{
                alert('ลบข้อมูลเรียบร้อย');
                delete_order(a);
            }
        }
    });
}

function send_save_order(a, b, c, d)
{
    var url = document.getElementById('url_').innerHTML+"confirm_order.json";
    $.ajax({
        url: url,
        type: 'post',
        data: {
            teacher_id: a,
            start_date: b,
            stop_date: c,
            note: d
        },
        dataType: 'json',

        success: function(respond){
            if(respond.exception == 1){
                alert('something wrong');
            }
            else{
                alert('บันทึกสำเร็จ');
            }
        }
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Rent Status */

function request_rent_status(url)
{
    // var url = document.getElementById('url_').innerHTML+"user_all_cart.json";
    $.ajax({
        url: url,
        type: 'get',
        data: {
            request_order_detail: 1
        },
        dataType: 'json',

        success:call_rent_status
    });
}