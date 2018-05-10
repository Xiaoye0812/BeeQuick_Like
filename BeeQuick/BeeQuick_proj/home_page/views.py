from django.shortcuts import render

from .models import HomeBanner, HomeNav, HomeShop, HomeMustBuy, HomeShow


def show_homepage(request):

    if request.method == 'GET':

        banners = HomeBanner.objects.all()
        navs = HomeNav.objects.all()
        shops = HomeShop.objects.all()
        must_buys = HomeMustBuy.objects.all()
        shows = HomeShow.objects.all()

        return render(request, 'home/home.html',
                      {'banners': banners,
                       'navs': navs,
                       'shops': shops,
                       'must_buys': must_buys,
                       'shows': shows})
