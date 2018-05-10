from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from random import choice
from time import time
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .models import UserModel, TicketModel
from .serializers import UserSerializer
from .filters import UserFilter


def regist(request, r_path):

    if request.method == 'GET':

        # r_path = request.GET.get('r_path')

        return render(request, 'user/user_register.html', {'r_path': r_path})

    if request.method == 'POST':

        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        icon = request.FILES.get('icon')
        r_path = request.POST.get('r_path')

        if not username:
            return render(request, 'user/user_register.html', {'name_result': '请输入正确的用户名'})

        user = UserModel.objects.filter(user_name=username)
        if user:
            return render(request, 'user/user_register.html', {'name_result': '用户名已存在'})

        UserModel.objects.create(
            user_name=username,
            email=email,
            password=make_password(password),
            icon=icon,
        )
        r_path = r_path if r_path else '/homepage/homepage/'
        return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': r_path}))


def login(request, r_path='/homepage/homepage/'):
    if request.method == 'GET':

        return render(request, 'user/user_login.html', {'r_path': r_path})

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        rpath = request.POST.get('r_path')

        try:
            user = UserModel.objects.get(user_name=username)
        except Exception as e:
            return render(request, 'user/user_login.html', {'name_result': '用户名不存在'})

        if not check_password(password, user.password):
            return render(request, 'user/user_login.html', {'password_result': '密码错误'})

        choice_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        ticket = 'TK_'
        for _ in range(12):
            ticket += choice(choice_str)
        ticket += str(int(time()))

        http_respon = HttpResponseRedirect(rpath)
        http_respon.set_cookie('ticket', ticket, max_age=3600)

        TicketModel.objects.create(
            ticket=ticket,
            user_id=user.id,
            create_time=int(time()),
        )

        return http_respon


class CheckUser(mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter


def logout(request):

    if request.method == 'GET':

        response = HttpResponseRedirect('/mine/mine/')
        response.delete_cookie('ticket')

        return response
