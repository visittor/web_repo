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
                alert('เรียบร้อย')
                delete_order(a);
            }
        }
    });
}
