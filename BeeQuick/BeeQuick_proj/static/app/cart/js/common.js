var csrf = $('input[name="csrfmiddlewaretoken"]').val();
function subshop(cart_id) {
    $.ajax({
        url: '/carts/subgoods/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {
            if (result.code == 200) {
                $('#num_' + cart_id).text(result['c_num']);
                $('#total').text('总价:' + result.total);
            }
            removeNoneCart(result, cart_id);
            need_login(result);
        },
        error: alert_error
    });
}

function addshop(cart_id) {
    $.ajax({
        url: '/carts/addgoods/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {
            if (result.code === 200) {
                $('#num_' + cart_id).text(result['c_num']);
                $('#total').text('总价:' + result.total);
            }
            removeNoneCart(result, cart_id);
            need_login(result);
        },
        error: alert_error
    });
}