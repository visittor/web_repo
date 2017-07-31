/**
 * Created by PHURINPAT on 4/7/2560.
 */



function call_borrow_admin(respond)
{
    // $("#page-inner").hide()
    var detail = " <div class='row'>" +
                    "<center><h2>รายการการยืมของนักศึกษา (ที่ยังไม่ได้รับของ)</h2></center>" +
					"<div class='col-md-12'>" +
						"<table class='table table-hover'>" +
											"<tr>" +
												"<th>#</th>" +
												"<th>รหัสการของยืม</th>" +
												"<th>รหัสนักศึกษา</th>"+
												"<th>ชื่อ สกุล</th>"+
												"<th>อาจารย์ผู้รับผิดชอบ </th>"+
												"<th>ระหว่างวันที่</th>"+
												"<th>การจัดการ</th>"+
											"</tr>"

    for (j in respond)
    {
        detail = detail+"<tr>"+
												"<td>"+ parseInt(parseInt(j)+1)+"</td>"+
												"<td>"+respond[j].id+"</td>"+
												"<td>"+respond[j].owner_id+"</td>"+
												"<td>"+respond[j].owner.first_name+" "+respond[j].owner.last_name+ "</td>"+
												"<td>"+respond[j].teacher.first_name+" "+respond[j].teacher.last_name+"</td>"+
												"<td>"+respond[j].start_date + "-" + respond[j].stop_date +"</td>"+
												"<td>"+
													"<a><button type='button' class='btn btn-success' onclick='edit_borrow_admin_button("+ respond[j].id +")'><i class='glyphicon glyphicon-floppy-saved'></i></button></a>"+
													"<button type='button' class='btn btn-danger' onclick='delete_borrow_list_admin("+ respond[j].id +")'><i class='glyphicon glyphicon-trash'></i></button>"+
												"</td>"+
											"</tr>"
    }
    document.getElementById("page-inner").innerHTML=detail+"</table></div></div>"

}


function call_return_admin(respond)
{
    var detail = " <div class='row'>" +
                    "<center><h2>รายการการยืมของนักศึกษา (ที่รับของไปแล้วรอส่งคืน)</h2></center>" +
					"<div class='col-md-12'>" +
						"<table class='table table-hover'>" +
											"<tr>" +
												"<th>#</th>" +
												"<th>รหัสการของยืม</th>" +
												"<th>รหัสนักศึกษา</th>"+
												"<th>ชื่อ สกุล</th>"+
												"<th>อาจารย์ผู้รับผิดชอบ </th>"+
												"<th>ระหว่างวันที่</th>"+
												"<th>การจัดการ</th>"+
											"</tr>"

    for (j in respond)
    {
        detail = detail+"<tr>"+
												"<td>"+ parseInt(parseInt(j)+1)+"</td>"+
												"<td>"+respond[j].id+"</td>"+
												"<td>"+respond[j].owner_id+"</td>"+
												"<td>"+respond[j].owner.first_name+" "+respond[j].owner.last_name+ "</td>"+
												"<td>"+respond[j].teacher.first_name+" "+respond[j].teacher.last_name+"</td>"+
												"<td>"+respond[j].start_date + "-" + respond[j].stop_date +"</td>"+
												"<td>"+
													"<a><button type='button' class='btn btn-success' onclick='edit_return_admin_button("+ respond[j].id +")'><i class='glyphicon glyphicon-floppy-saved'></i></button></a>"+
												"</td>"+
											"</tr>"
    }
    document.getElementById("page-inner").innerHTML=detail+"</table></div></div>"

}


function edit_borrow_admin(respond) {
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_borrow_admin.html";
	$("#page-inner").load(url_static, function () {
		$("#owner_full_name").html(respond.owner.first_name+" "+respond.owner.last_name);
		$("#owner_id").html(respond.owner.student_id);
		$("#owner_years").html(parseInt(61-(parseInt(respond.owner.student_id)/1000000000)));
		$("#teacher_name").html(respond.teacher.first_name+" "+respond.teacher.last_name);
		$("#start_borrow_date").html(respond.start_date);//EDIT LATER
		$("#stop_borrow_date").html(respond.stop_date);
		var inner_detail = "<table class='table table-hover'> <tr> <th>#</th> <th>รหัสอุปกรณ์</th> <th>ชื่ออุปกรณ์</th> <th>จำนวน</th> <th>โมดูล / ที่มา</th> <th>สถานที่เก็บ</th> </tr>"
		for( i in respond.items){
		inner_detail = inner_detail + "<tr> <td><input type='checkbox' value='' /></td> <td>"+ respond.items[i].id +"</td> <td>"+ respond.items[i].name +"</td> <td>1</td> <td>"+ respond.items[i].sub_category +"</td> <td>"+ respond.items[i].storage +"</td> <tr>"
		}
		inner_detail = inner_detail+"</table>"
		$("#inner_request").html(inner_detail);
		$('#submit_edit').attr("onclick", "").click(function() {
			var id_cart = respond.id;
                  submit_edit_borrow(id_cart);
		});
		$('#cancle_edit').attr("onclick", "").click(function() {
                  cancle_edit_borrow();
		});
    });
}


function edit_return_admin(respond)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_borrow_admin.html";
	$("#page-inner").load(url_static, function () {
		$("#owner_full_name").html(respond.owner.first_name+" "+respond.owner.last_name);
		$("#owner_id").html(respond.owner.student_id);
		$("#owner_years").html(parseInt(61-(parseInt(respond.owner.student_id)/1000000000)));
		$("#teacher_name").html(respond.teacher.first_name+" "+respond.teacher.last_name);
		$("#start_borrow_date").html(respond.start_date);//EDIT LATER
		$("#stop_borrow_date").html(respond.stop_date);
		var inner_detail = "<table class='table table-hover'> <tr> <th>#</th> <th>รหัสอุปกรณ์</th> <th>ชื่ออุปกรณ์</th> <th>จำนวน</th> <th>โมดูล / ที่มา</th> <th>สถานที่เก็บ</th> </tr>"
		for( i in respond.items){
		inner_detail = inner_detail + "<tr> <td><input type='checkbox' value='' /></td> <td>"+ respond.items[i].id +"</td> <td>"+ respond.items[i].name +"</td> <td>"+ respond.items[i].value +"</td> <td>"+ respond.items[i].subject_name +"</td> <td>"+ respond.items[i].storage +"</td> <tr>"
		}
		inner_detail = inner_detail+"</table>"
		$("#inner_request").html(inner_detail);
		$('#submit_edit').attr("onclick", "").click(function() {
			var id_cart = respond.id;
                  submit_edit_return(id_cart);
		});
		$('#cancle_edit').attr("onclick", "").click(function() {
                  cancle_edit_return();
		});
    });
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function call_main_category(respond){
	var url_static = document.getElementById('url_static').innerHTML+"fluke/list_category.html";
	$("#page-inner").load(url_static, function () {
		var j = 1;
		var inner_detail = "<tr> <th>#</th> <th>ชื่อหมวดหมู่หลัก</th> <th>การจัดการ</th> </tr>";
		for( i in respond){
		inner_detail = inner_detail + "<tr> <td>"+ j +"</td> <td>" + respond[i] + "</td> <td> <a><button type='button' onclick= \"edit_main_category('" + respond[i] + "')\" class='btn btn-warning'><i class='glyphicon glyphicon-pencil'></i></button></a> <button type='button' onclick=\"delete_main_category('" + respond[i] + "')\" class='btn btn-danger'><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>";
		j++;
		}
		$("#category_table").html(inner_detail);
    });
}

function add_category()
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/add_category.html";
	$("#page-inner").load(url_static, function () {
		$('#submit_add_category_button').attr("onclick", "").click(function() {
			var name_to_add = document.getElementById("category_to_add").value;
                  submit_add_category(name_to_add);
		});
    });
}

function edit_main_category(name)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_category.html";
	$("#page-inner").load(url_static, function () {
		var old_name = name;
		$('#submit_main_category_name').attr("onclick", "").click(function() {
			var new_name = document.getElementById("new_name").value;
                  send_new_category_name(old_name,new_name);
		});
    });
}

function call_sub_category(respond)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/list_subcategory.html";
	$("#page-inner").load(url_static, function () {
		console.log(respond);
		var inner_detail = "<tr> <th>#</th> <th>ชื่อหมวดหมู่หลัก</th> <th>ชื่อหมวดหมู่ย่อย</th> <th>การจัดการ</th> </tr>";
		var k =1;
		for(i in respond){
			for(j in respond[i]){
				inner_detail = inner_detail + "<tr><td>"+ k +"</td><td>"+ i +"</td><td>"+ respond[i][j] +"</td><td> <a><button type='button' onclick=\"edit_sub_category('" + i + "'" + "," + "'" + respond[i][j] + "')\" class='btn btn-warning'><i class='glyphicon glyphicon-pencil'></i></button></a><button type='button' class='btn btn-danger' onclick=\"delete_sub_category('" + i + "'" + "," + "'" + respond[i][j] + "')\" ><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>";
				k++;
			}
		}
		$("#subcategory_table").html(inner_detail);
    });
}

function call_add_subcategory(respond)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/add_subcategory.html";
	$("#page-inner").load(url_static, function (){
		console.log(respond);
		var list_main =  "<option value=''>โปรดเลือกหมวดหมูหลัก</option>";
		for(i in respond){
			list_main = list_main + "<option value='" + respond[i] + "'>"+respond[i]+"</option>";
		}
		$("#select_main").html(list_main);
		$('#submit_add_subcategory_button').attr("onclick", "").click(function() {
		alert('Press');
			var name_to_add = document.getElementById("new_subcategory").value;
			var main_category_to_add = document.getElementById("select_main").value;
                  submit_add_subcategory(main_category_to_add, name_to_add);
		});
    });

}

function edit_sub_category(main,sub)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_subcategory.html";
	$("#page-inner").load(url_static, function () {
		var main_name = main;
		var old_name = sub;
		$('#option_forwhat').html(main_name)
		$('#new_name').on('keypress', function (e) {
			 if(e.which == 13){

				//Disable textbox to prevent multiple submit
				$('#new_name').attr("disabled", "disabled");

				//Do Stuff, submit, etc..
				var new_name = document.getElementById("new_name").value;
				e.preventDefault();
				$('#new_name').removeAttr("disabled");
				send_new_subcategory_name(main_name,old_name,new_name);
         	}
  		 });
		$('#submit_subcategory_name').attr("onclick", "").click(function() {
				var new_name = document.getElementById("new_name").value;
				send_new_subcategory_name(main_name,old_name,new_name);
		});
		// $('#submit_sub_category_name').attr("onclick", "onclick_submit_sub_category_name("+main_name+","+old_name+")")
    });
}

// function onclick_submit_sub_category_name(main_name, old_name) {
// 	new_name  = document.getElementById("new_name").value;
// 	send_new_subcategory_name(main_name,old_name,new_name);
// }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function call_list_devicetype(respond)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/list_devicetype.html";
	$("#page-inner").load(url_static, function () {
	    console.log(respond);
	    var inner_detail = "<tr> <th>#</th> <th>ชื่อประเภทอุปกรณ์</th> <th>ชื่อย่อประเภทอุปกรณ์</th> <th>การจัดการ</th> </tr>";
        var x = 1;
        for(i in respond){
	        console.log(i+respond[i]);
	        inner_detail = inner_detail + "<tr> <td>"+ x +"</td> <td>"+ i +"</td> <td>"+ respond[i] +"</td> <td> <a><button type='button' class='btn btn-warning' onclick='edit_devicetype("+"\""+ i +"\""+","+"\""+ respond[i] +"\""+")' ><i class='glyphicon glyphicon-pencil'></i></button></a> <button onclick=\"delete_device_type('"+ i +"')\" type='button' class='btn btn-danger'><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>";
            x++;
        }
        $("#devicetype_table").html(inner_detail);
    });
}

function edit_devicetype(old,code,new_name)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_devicetype.html";
	$("#page-inner").load(url_static, function () {
	    document.getElementById("input_code").value = code;
	    $("#submit_edit_devicetype").attr("onclick", "").click(function () {
            new_name = document.getElementById("new_devicetype").value;
            alert(old+' '+new_name+' '+code);
            send_new_devicetype_name(old,new_name,code);
        })
    });
}

function call_add_devicetype()
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/add_devicetype.html";
	$("#page-inner").load(url_static, function () {
	    $("#submit_add_devicetype").attr("onclick", "").click(function () {
            new_type = document.getElementById("new_type").value;
            new_code = document.getElementById("new_code").value;
            alert(new_type+' '+new_code);
            add_devicetype(new_type,new_code);
        })

    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function call_list_place(respond)
{
	console.log(respond)
	var url_static = document.getElementById('url_static').innerHTML+"fluke/list_place.html";
	$("#page-inner").load(url_static, function () {
		var inner_detail = "<tr> <th>#</th> <th>ชื่อสถานที่เก็บอุปกรณ์</th> <th>การจัดการ</th> </tr>"
		for(i in respond){
			inner_detail = inner_detail + "<tr> <td>" + (parseInt(i)+1) + "</td> <td>" + respond[i] + "</td> <td> <a><button type='button' class='btn btn-warning' onclick=\"call_edit_place("+ "'" + respond[i] + "'" +")\"><i class='glyphicon glyphicon-pencil'></i></button></a> <button type='button' class='btn btn-danger' onclick=\"delete_list_place(" + "'" + respond[i] + "'" + ")\"><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>"
		}
		$("#table_list_place").html(inner_detail);
    });
}

function call_edit_place(old_name)
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/edit_place.html";
	$("#page-inner").load(url_static, function () {
		$("#submit_new_place").attr("onclick", "").click(function () {
			var new_name = document.getElementById("new_name").value;
			send_new_place_name(old_name,new_name)
		})
    });
}

function call_add_place()
{
	var url_static = document.getElementById('url_static').innerHTML+"fluke/add_place.html";
	$("#page-inner").load(url_static, function () {
		$("#submit_add_new_place").attr("onclick", "").click(function () {
			var new_place = document.getElementById("new_place").value;
			send_add_place(new_place)
		})
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function call_list_device(respond)
{
	console.log(respond)
	var url_static = document.getElementById('url_static').innerHTML+"fluke/list_device.html";
	$("#page-inner").load(url_static, function () {
		inner_type = "<option value = ''>ประเภทอุปกรณ์</option>";
		inner_category = "<option value = ''>หมวดหมู่ย่อย</option>";
		inner_place = "<option value = ''>สถานที่เก็บ</option>";
		x = 0;
		for(i in respond.type_list){
			inner_type = inner_type + "<option value = '" + i + "'>" + i + "</option>"
		}
		for(j in respond.sub_category){
			inner_category = inner_category + "<option value = '" + j + "'>" + j + "</option>"
		}
		for(k in respond.storage){
			inner_place = inner_place + "<option value = '" + respond.storage[k] + "'>" + respond.storage[k] + "</option>"
			x++
		}
		$("#select_type").html(inner_type);
		$("#select_category").html(inner_category);
		$("#select_place").html(inner_place);
		inner_detail = document.getElementById("big_table").innerHTML;
		for(l in respond.items){
			inner_detail = inner_detail + "<tr> <td>"+ (parseInt(l)+1) +"</td> <td> " + respond.items[l].code_name + " </td> <td>" + respond.items[l].name + "</td> <td>" + respond.items[l].type_ + "</td> <td>" + respond.items[l].sub_category + "</td> <td>" + respond.items[l].storage + "</td> <td> <a><button type='button' class='btn btn-warning'><i class='glyphicon glyphicon-pencil'></i></button></a> <button onclick='delete_items("+ respond.items[l].id +")' type='button' class='btn btn-danger'><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>"
		}
		$("#big_table").html(inner_detail);
		$("#search_button").attr("onclick","").click(function () {
			type = document.getElementById("select_type").value;
			sub_cat = document.getElementById("select_category").value;
			storage = document.getElementById("select_place").value;
			search_item(type,sub_cat,storage);
        })
    });
}

function call_add_item(respond)
{
	console.log('on call_add_iem');
	var url_static = document.getElementById('url_static').innerHTML+"earth/add_item.html";
	$("#page-inner").load( url_static, function () {
		var main_category_list = "<option value=''>เลือกหมวดหมู่หลัก</option>";
		for(i in respond.sub_category){
			main_category_list = main_category_list + "<option value='"+ i +"'>"+ i +"</option>";
		}
		$("#list_category_edit").html(main_category_list);
		var in_type_list = '<option value="">เลือกประเภท</option>';;
		for(i in respond.type_list){
			in_type_list = in_type_list +"<option value='" + i + "'>" + i + "</option>"
		}
		$("#type_list").html(in_type_list);
		var in_storage_list = '<option value="">เลือกที่เก็บ</option>';
		for(i in respond.storage){
			in_storage_list = in_storage_list + "<option value='" + respond.storage[i] + "'>" + respond.storage[i] + "</option>"
		}
		$("#storage_list").html(in_storage_list);
		$("#list_category_edit").attr('onChange', '').change( function() {
			console.log('Change!');
			main_category = document.getElementById("list_category_edit").value;
			console.log(main_category_list + ' ' + respond.sub_category[main_category]);
			list_sub_category = respond.sub_category[main_category];
			$("#div_sub_category").html("<span class='input-group-addon'><i class='glyphicon glyphicon-pencil'></i></span> <select class='form-control' id='sub_category_edit'> ");
			var in_sub_category = " <option value=''>เลือกหมวดหมู่ย่อย</option>";
			for (i in list_sub_category) {
				in_sub_category = in_sub_category + "<option value='" + list_sub_category[i] + "'>" + list_sub_category[i] + "</option>";
			}
			console.log(in_sub_category);
			$("#sub_category_edit").html(in_sub_category);
		});
    });
}

function submit_add_item() {
    var new_name = document.getElementById("new_item_name").value;
    var main_cat = document.getElementById("list_category_edit").value;
    var sub_cat = document.getElementById("sub_category_edit").value;
    var type = document.getElementById("type_list").value;
    var storage = document.getElementById("storage_list").value;
    var note = document.getElementById("note").value;
    var formdata = new FormData();
    // var img = $("#image_inpur").files;
	formdata.append('photo', $("#image_input")[0].files[0]);
	console.log(formdata);
	// var send_pic = JSON.stringify($("#image_input")[0].files[0]);
    add_item(new_name,main_cat,sub_cat,type,storage,note,formdata);
}