from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'checkuser', views.CheckUser)

urlpatterns = [

    url(r'^login/(?P<r_path>.+)', views.login, name='login'),
    url(r'^regist/(.*)', views.regist, name='regist'),
    url(r'^logout/', views.logout, name='logout'),
]

urlpatterns += router.urls
