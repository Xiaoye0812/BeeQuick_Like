function changSelect(cart_id) {
    // console.log('changeselect');
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/change_select/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {

            if (result.code === 200){

                if (result.is_select){
                    $('#select_' + cart_id).text('√');
                }
                else {
                    $('#select_' + cart_id).html('&nbsp;');
                }

                selectChangestate(result);
                $('#total').text('总价:' + result.total);
            }

            removeNoneCart(result, cart_id);
            need_login(result);
        },
        error: alert_error
    });
}

function changeAll(is_select) {
    // console.log('selectall');
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/carts/change_all/',
        type: 'POST',
        data: {'is_select': is_select},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (result) {

            if (result.code === 200){

                var p_node = $('#sele_all').parent();
                $(p_node).html('<span id="sele_all" onclick="changeAll('+ (result.select_all?0:1) + ')"></span>');

                selectAllChangestate(result);
                $('#total').text('总价:' + result.total);
            }

            need_login(result);
        },
        error: alert_error
    });
}

function alert_error(result) {
    alert('请求错误');
}

function need_login(result) {
    if(result.code === 400){
        alert(result['msg']);
    }
}

function selectAllChangestate(result) {
    if (result.select_all === 1){
        $('#sele_all').text('√');
        $('.is_choose > span').html('√');
    }else {
        $('#sele_all').html('&nbsp;');
        $('.is_choose > span').html('&nbsp;');
    }
}

function selectChangestate(result) {
    if (result.select_all === 1){
        $('#sele_all').text('√');
    }else {
        $('#sele_all').html('&nbsp;');
    }
}

function removeNoneCart(result, cart_id) {
    if (result.code === 201){
        alert(result['msg']);
        $('#select_' + cart_id).parent().parent().parent().remove();
    }
}