"""BeeQuick_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', include('home_page.urls', namespace='home')),
    url(r'^quickbuy/', include('quick_buy.urls', namespace='quickbuy')),
    url(r'^carts/', include('carts.urls', namespace='carts')),
    url(r'^mine/', include('mine.urls', namespace='mine')),
    url(r'^user/', include('users.urls', namespace='user')),
    url(r'^order/', include('order.urls', namespace='order')),
]

from . import settings

from django.contrib.staticfiles.urls import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
