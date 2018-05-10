from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^createorder/', views.create_order, name='createorder'),
    url(r'^topay/(\d+)/', views.to_pay, name='topay'),
    url(r'^changeorderstatus/', views.change_order_status, name='changeorderstatus'),
    url(r'^order_pay/', views.order_pay, name='pay'),
    url(r'^order_wait/', views.order_wait, name='wait'),
]
