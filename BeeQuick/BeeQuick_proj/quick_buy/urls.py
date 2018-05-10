from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.market_category, name='market_category'),
    url(r'^subgoods/', views.sub_goods, name='sungoods'),
    url(r'^addgoods/', views.add_goods, name='addgoods'),
]
