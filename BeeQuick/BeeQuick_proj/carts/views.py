from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from carts.models import CartModel


def show_carts(request):

    if request.method == 'GET':

        user = request.user
        path = request.path
        ticket = request.COOKIES.get('ticket')

        if not user.id or not ticket:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': path}))

        carts = user.cartmodel_set.all()
        result = {
            'carts': carts,
            'select_all': 1,
        }
        for cart in carts:
            if not cart.is_select:
                result['select_all'] = 0
                break

        result = set_total(carts, result)

        return render(request, 'cart/cart.html', result)


def sub_goods(request):

    if request.method == 'POST':

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        cart_id = request.POST.get('cart_id')
        user = request.user
        if not user.id:
            data = set_need_login(data)
            return JsonResponse(data)

        carts = CartModel.objects.all()
        try:
            cart = carts.get(id=cart_id, user_id=user.id)
        except Exception as e:
            data['c_num'] = 0
            return JsonResponse(data)

        if cart.c_num == 1:
            cart.delete()
            data = cart_is_none(data, '商品已移除')
        else:
            cart.c_num -= 1
            cart.save()
            data['c_num'] = cart.c_num

        data = set_total(carts, data)

        return JsonResponse(data)


def add_goods(request):

    if request.method == 'POST':

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        cart_id = request.POST.get('cart_id')
        user = request.user
        if not user.id:
            data = set_need_login(data)
            return JsonResponse(data)

        carts = CartModel.objects.all()
        cart = carts.filter(id=cart_id, user_id=user.id)
        if cart.exists():
            cart = cart[0]
            cart.c_num += 1
            cart.save()
            data['c_num'] = cart.c_num
        else:
            data = cart_is_none(data, '订单不存在')

        data = set_total(carts, data)

        return JsonResponse(data)


def change_select(request):

    if request.method == 'POST':

        result = {
            'code': 200,
            'msg': '请求成功',
            'select_all': 1,
        }

        cart_id = request.POST.get('cart_id')
        carts = CartModel.objects.all()
        cart = carts.filter(id=cart_id)

        if not request.user.id:
            result = set_need_login(result)
            return JsonResponse(result)

        if cart:
            is_select = cart[0].is_select
            is_select = not is_select
            cart[0].is_select = is_select
            cart[0].save()
            result['is_select'] = is_select

        else:
            result = cart_is_none(result, '订单不存在')

        for car in carts:
            if not car.is_select:
                result['select_all'] = 0
                break
        result = set_total(carts, result)

        return JsonResponse(result)


def change_all(request):

    if request.method == 'POST':

        result = {
            'code': 200,
            'msg': '请求成功',
        }

        is_select = request.POST.get('is_select')
        user = request.user

        if not user.id:
            result = set_need_login(result)
            return JsonResponse(result)

        carts = CartModel.objects.filter(user_id=user.id)
        for cart in carts:
            cart.is_select = int(is_select)
            cart.save()

        result = set_total(carts, result)

        result['select_all'] = int(is_select)

        return JsonResponse(result)


def set_total(carts, result):
    result['total'] = 0.0
    for cart in carts:
        if cart.is_select:
            result['total'] += float(cart.goods.prefer_price) * int(cart.c_num)

    result['total'] = '%.2f' % result['total']

    return result


def set_need_login(result):
    result['code'] = 400
    result['msg'] = '请先登录'

    return result


def cart_is_none(result, msg):
    result['code'] = 201
    result['msg'] = msg

    return result
