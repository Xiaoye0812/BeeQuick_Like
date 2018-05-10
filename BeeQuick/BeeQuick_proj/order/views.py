from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from carts.models import CartModel
from .models import OrderModel
from goods.models import OrderGoodsModel


def create_order(request):

    if request.method == 'GET':

        user = request.user
        ticket = request.COOKIES.get('ticket')

        if not user.id or not ticket:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': request.path}))

        carts_all = CartModel.objects.all()
        carts = carts_all.filter(user_id=user.id, is_select=1)
        if carts:
            order = OrderModel.objects.create(
                user_id=user.id,
                o_num=len(carts),
                o_status=0,
            )
            for cart in carts:
                OrderGoodsModel.objects.create(
                    goods_id=cart.goods_id,
                    order_id=order.id,
                    good_num=cart.c_num,
                )
                cart.delete()

            return HttpResponseRedirect(reverse('order:topay', args=(order.id,)))


def to_pay(request, order_id):

    if request.method == 'GET':

        order = OrderModel.objects.filter(id=order_id)
        result = {
            'order': order[0],
            'order_goods': order[0].ordergoodsmodel_set.all(),
        }

        return render(request, 'order/order_info.html', result)


def change_order_status(request):

    if request.method == 'GET':

        result = {
            'code': 200,
            'msg': '请求成功',
        }

        order_id = request.GET.get('order_id')
        status = request.GET.get('status')

        orders = OrderModel.objects.filter(id=order_id)

        if not orders:
            result['code'] = 201
            result['msg'] = '订单不存在'

            return JsonResponse(result)

        orders[0].o_status = int(status)
        orders[0].save()

        return JsonResponse(result)


def order_pay(request):

    if request.method == 'GET':

        user = request.user
        ticket = request.COOKIES.get('ticket')

        if not user.id or not ticket:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': request.path}))

        orders = OrderModel.objects.filter(user_id=user.id, o_status=0)

        result = {
            'orders': orders,
        }

        return render(request, 'order/order_list_wait_pay.html', result)


def order_wait(request):

    if request.method == 'GET':

        user = request.user
        ticket = request.COOKIES.get('ticket')

        if not user.id or not ticket:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': request.path}))

        orders = OrderModel.objects.filter(user_id=user.id, o_status=1)

        result = {
            'orders': orders,
        }

        return render(request, 'order/order_list_payed.html', result)
