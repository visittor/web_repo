/**
 * Created by PHURINPAT on 4/7/2560.
 */

function main()
{
    $.ajax({
        url: ' http://localhost:6543/test_admin_borrow.json',
        type: 'get', //หรือ post (ค่าเริ่มต้นเป็นแบบ get)
        data: {
            requestByAjax: 1,
        },
        dataType: 'json', //หรือ json หรือ xml

        success:editt
    });
}