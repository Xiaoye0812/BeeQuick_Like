from rest_framework import filters
import django_filters

from .models import UserModel


class UserFilter(filters.FilterSet):

    username = django_filters.CharFilter('user_name')

    class Meta:
        model = UserModel
        fields = ['user_name']
