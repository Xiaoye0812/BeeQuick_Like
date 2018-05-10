csrf = $('input[name="csrfmiddlewaretoken"]').val();
function subshop(good_id) {
    $.ajax({
        url: '/quickbuy/subgoods/',
        type: 'POST',
        data: {'good_id': good_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {
            $('#num_' + good_id).text(result['c_num']);
        },
        error: function (result) {
            alert('请求错误');
        }
    });
}

function addshop(good_id) {
    $.ajax({
        url: '/quickbuy/addgoods/',
        type: 'POST',
        data: {'good_id': good_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {
            $('#num_' + good_id).text(result['c_num']);
        },
        error: function (result) {
            alert('请求错误');
        }
    });
}