import django_filters
from .models import *


class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = '__all__'
