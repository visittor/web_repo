/**
 * Created by PHURINPAT on 16/7/2560.
 */
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Rent Item */

function call_list_device_from_container(respond)
{
    var x = 1;
    console.log(respond);
    $('#select_category').html('<option value="">เลือกหมวดหมู่หลัก</option>');
    $('#select_subcategory').html('<option value="">เลือกหมวดหมู่หลักก่อน</option>');
    for(i in respond.sub_category){
        $('#select_category').append("<option value='"+ i +"'>"+ i +"</option>")
    }

    $("#select_category").attr('onChange', '').change( function() {
			console.log('change');
			main_category = document.getElementById("select_category").value;
			list_sub_category = respond.sub_category[main_category];
			console.log(list_sub_category);
			for (i in list_sub_category) {
				$('#select_subcategory').append("<option value='" + list_sub_category[i] + "'>" + list_sub_category[i] + "</option>");
			}
		});
    var url_static = document.getElementById('url_static').innerHTML+"/earth/rentitem_container.html"
    $.get(url_static, function(data){
        document.getElementById('card_row').innerHTML = '';
        for(i in respond.items){
            $("#card_row").append(data);
            $('#outer_status_').attr('id','outer_status_'+i);
            $('#inner_status_').attr('id','inner_status_'+i);
            $('#borrow_button_').attr('id','borrow_button_'+i);
            $('#borrow_button_').attr('value',respond.items[i].id);
            $('#item_name_').attr('id','item_name_'+i);
            $('#main_category_').attr('id','main_category_'+i);
            $('#storage_').attr('id','storage_'+i);
            $('#note_').attr('id','note_'+i);
            $('#choose_button_').attr('id','choose_button_'+i);
            if(!respond.items[i].cart_id){
                $('#choose_button_'+i).html("<button type='button' class='btn btn-primary' onclick='send_borrow_request("+ respond.items[i].id +")'>เลือก</button>")
                $('#outer_status_'+i).html("<a class='label label-success glyphicon glyphicon-time'>Available</a>");
                $('#inner_status_'+i).html("<a class='label label-success glyphicon glyphicon-time'>Available</a>");
            }

            else{

                $('#borrow_button_'+i).remove();
                $('#outer_status_'+i).html("<a class='label label-danger glyphicon glyphicon-time'>CheckedOut </a>");
                $('#inner_status_'+i).html("<a class='label label-danger glyphicon glyphicon-time'>ยืมโดย ...</a>")

            }

            $('#item_name_'+i).append(' '+respond.items[i].name);
            $('#main_category_'+i).append(' '+respond.items[i].main_category);
            $('#storage_'+i).append(' '+respond.items[i].storage);
            if(!respond.items[i].note){
                $('#note_'+i).val('ไม่มีบันทึกจากเจ้าหน้าที่');
            }
            else {
                $('#note_'+i).val(respond.items[i].note);
            }
            $('#detail_item_button_').attr('id','detail_item_button_'+i);
            $('#detail_item_button_'+i).attr('data-target','#Modal_'+i);
            $('#Modal_').attr('id','Modal_'+i);
        }
        // $("#card_row").html(data)

    });
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* Approve Item */

function call_order_detail(respond)
{
    console.log(respond);
    $('#user_name').html(respond.owner.first_name + " " + respond.owner.last_name);
    $('#user_id').html(respond.owner.id);
    $('#user_years').html(1);
    for(i in respond.teacher){
        $("#teacher_list").append("<option value='"+ respond.teacher[i].id +"'>"+ respond.teacher[i].first_name +" "+ respond.teacher[i].first_name +"</option>")
    }

    for(j in respond.item){
        $("#item_table").append("<tr id='"+respond.item[j].id+"'><td id='"+respond.item[j].id+"'>"+respond.item[j].code_name+"</td> <td id='"+respond.item[j].id+"'>"+respond.item[j].name+"</td> <td id='"+respond.item[j].id+"'>1</td> <td id='"+respond.item[j].id+"'>"+respond.item[j].sub_category+"</td> <td id='"+respond.item[j].id+"'>"+respond.item[j].storage+"</td> <td id='"+respond.item[j].id+"'><button id='"+respond.item[j].id+"' onclick='send_delete_order(" + respond.item[j].id + ")' type='button' class='close' data-dismiss='modal' aria-label='Close'><span id='"+respond.item[j].id+"' aria-hidden='true'>&times;</span></button></td> <tr id='"+respond.item[j].id+"'>")
    }
}

function delete_order(id)
{
    $("#"+id).remove();
}

function save_order()
{
    var teacher_name = $("#teacher_list").val();
    var start_date = $("#start_date").val();
    var stop_date = $("#stop_date").val();
    var note = $("#student_note").val();
    console.log("teacher id = "+teacher_name+typeof teacher_name+"\nstart date = "+start_date+typeof start_date+"\nstop date = "+stop_date+typeof stop_date)
    if(teacher_name == ""){
        alert("กรุณาเลือกชื่ออาจารย์");
    }
    else if(start_date == ""){
        alert("กรุณาเลือกวันยืมอุปกรณ์");
    }
    else if(stop_date == ""){
        alert("กรุณาเลือกวันคืนอุปกรณ์")
    }
    else {
        send_save_order(teacher_name, start_date, stop_date, note);
    }
}