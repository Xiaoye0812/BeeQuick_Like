from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^homepage/$', views.show_homepage, name='homepage'),
]
