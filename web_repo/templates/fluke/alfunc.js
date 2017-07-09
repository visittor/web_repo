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
													"<button type='button' class='btn btn-danger'><i class='glyphicon glyphicon-trash'></i></button>"+
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
	
	$("#page-inner").load("edit_borrow_admin.html", function () {
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
		$('#summit_edit').attr("onclick", "").click(function() {
			var id_cart = respond.id;
                  summit_edit_borrow(id_cart);
		});
		$('#cancle_edit').attr("onclick", "").click(function() {
                  cancle_edit_borrow();
		});
    });
}


function edit_return_admin(respond) {

	$("#page-inner").load("edit_borrow_admin.html", function () {
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
		$('#summit_edit').attr("onclick", "").click(function() {
			var id_cart = respond.id;
                  summit_edit_return(id_cart);
		});
		$('#cancle_edit').attr("onclick", "").click(function() {
                  cancle_edit_return();
		});
    });
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function call_main_category(respond){
	$("#page-inner").load("list_category.html", function () {
		var j = 1;
		var inner_detail = "<tr> <th>#</th> <th>ชื่อหมวดหมู่หลัก</th> <th>การจัดการ</th> </tr>";
		for( i in respond){
		inner_detail = inner_detail + "<tr> <td>"+ j +"</td> <td>" + respond[i] + "</td> <td> <a><button type='button' onclick= \"edit_main_category(' " + respond[i] + " ')\" class='btn btn-warning'><i class='glyphicon glyphicon-pencil'></i></button></a> <button type='button' onclick=\"delete_main_category(' " + respond[i] + " ')\" class='btn btn-danger'><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>";
		j++;
		}
		$("#category_table").html(inner_detail);
    });
}

function edit_main_category(name)
{
	$("#page-inner").load("edit_category.html", function () {
		var old_name = name;
		$('#summit_main_category_name').attr("onclick", "").click(function() {
			var new_name = document.getElementById("new_name").value;
                  send_new_category_name(old_name,new_name);
		});
    });
}

function call_sub_category(respond)
{
	$("#page-inner").load("list_subcategory.html", function () {
		var inner_detail = "<tr> <th>#</th> <th>ชื่อหมวดหมู่หลัก</th> <th>ชื่อหมวดหมู่ย่อย</th> <th>การจัดการ</th> </tr> </table>";
		var k =1;
		for(i in respond){
			for(j in respond){
				inner_detail = inner_detail + "<tr><td>"+ k +"</td><td>"+ i +"</td><td>"+ respond[i] +"</td><td> <a><button type='button' onclick=\"edit_sub_category('" + i +","+ respond[i] + "')\" class='btn btn-warning'><i class='glyphicon glyphicon-pencil'></i></button></a><button type='button' class='btn btn-danger' onclick=\"delete_sub_category('" + i +","+ respond[i] + "')\" ><i class='glyphicon glyphicon-remove'></i></button> </td> </tr>";
				k++;
			}
		}
		$("#subcategory_table").html(inner_detail);
    });
}

function edit_sub_category(main,sub)
{
	$("#page-inner").load("edit_subcategory.html", function () {
		var main_name = main;
		var old_name = sub;
		$('#option_forwhat').html(main_name)
		$('#summit_sub_category_name').attr("onclick", "").click(function() {
			var new_name = document.getElementById("new_name").value;
                  send_new_subcategory_name(main_name,old_name,new_name);
		});
    });
}