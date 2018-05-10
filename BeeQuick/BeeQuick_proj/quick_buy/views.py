from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from goods.models import GoodModel
from .models import GoodType
from carts.models import CartModel


def market(request):

    if request.method == 'GET':

        good_type = GoodType.objects.all().order_by('type_sort').first()
        # goods = good_types.first().goodmodel_set.all()

        # result = {
        #     'good_types': good_types,
        #     'goods': goods
        # }

        # return render(request, 'market/market.html', {'result': result})
        return HttpResponseRedirect(reverse('quickbuy:market_category', args=(good_type.type_id, '0', '0')))


def market_category(request, category_id, child_id, sort_id):

    if request.method == 'GET':

        good_types = GoodType.objects.all().order_by('type_sort')
        try:
            good_type = good_types.get(type_id=category_id)
        except Exception as e:
            result = {
                'good_types': good_types,
                'category_id': category_id,
                'child_id': child_id,
                'sort_id': sort_id,
            }
            return render(request, 'market/market.html', result)
        else:
            goods = good_type.goodmodel_set.all()

        if child_id != '0':
            goods = goods.filter(child_cid=child_id)

        if sort_id != '0':
            if sort_id == '1':
                goods = goods.order_by('product_num')
            elif sort_id == '2':
                goods = goods.order_by('-prefer_price')
            elif sort_id == '3':
                goods = goods.order_by('prefer_price')

        category_str = good_type.child_type_names
        category_str_list = category_str.split('#')
        category_list = []
        for category_substr in category_str_list:
            category_substr_list = category_substr.split(':')
            category_list.append(category_substr_list)

        result = {
            'good_types': good_types,
            'goods': goods,
            'category_list': category_list,
            'category_id': int(category_id),
            'child_id': child_id,
            'sort_id': sort_id
        }

        return render(request, 'market/market.html', result)


def sub_goods(request):
    if request.method == 'POST':

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        good_id = request.POST.get('good_id')
        user = request.user
        if not user.id:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': request.path}))

        try:
            cart = CartModel.objects.get(goods_id=good_id, user_id=user.id)
        except Exception as e:
            data['c_num'] = 0
            return JsonResponse(data)

        if cart.c_num == 1:
            cart.delete()
            data['c_num'] = 0
        else:
            cart.c_num -= 1
            cart.save()
            data['c_num'] = cart.c_num

        return JsonResponse(data)


def add_goods(request):
    if request.method == 'POST':

        data = {
            'code': 200,
            'msg': '请求成功',
        }

        good_id = request.POST.get('good_id')
        user = request.user
        if not user.id:
            return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': request.path}))

        cart = CartModel.objects.filter(goods_id=good_id, user_id=user.id)
        if cart.exists():
            cart = cart[0]
            cart.c_num += 1
            cart.save()
            data['c_num'] = cart.c_num
        else:
            cart = CartModel.objects.create(
                goods_id=good_id,
                user_id=user.id,
                c_num=1,
                is_select=True,
            )
            data['c_num'] = cart.c_num

        return JsonResponse(data)
