$(function () {

    $("#order_payed_list").click(function () {

        window.open("/order/order_wait/", target="_self");

    });

    $("#wait_pay_list").click(function () {

        window.open("/order/order_pay/", target="_self");

    })

});