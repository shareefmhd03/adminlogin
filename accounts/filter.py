import django_filters
from django_filters import CharFilter
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='username', lookup_expr='icontains', label='Search User ')

    class Meta:
        model =  User
        fields = ['name']