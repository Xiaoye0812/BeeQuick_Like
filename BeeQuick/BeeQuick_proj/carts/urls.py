from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^carts/$', views.show_carts, name='carts'),
    url(r'^subgoods/', views.sub_goods, name='sungoods'),
    url(r'^addgoods/', views.add_goods, name='addgoods'),
    url(r'^change_select/$', views.change_select, name='change_select'),
    url(r'^change_all', views.change_all, name='change_all'),
]
