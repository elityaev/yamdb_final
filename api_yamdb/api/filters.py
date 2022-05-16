from django_filters import rest_framework
from reviews.models import Title


class FilterSetTitle(rest_framework.FilterSet):
    genre = rest_framework.CharFilter(field_name='genre__slug')
    category = rest_framework.CharFilter(field_name='category__slug')
    name = rest_framework.CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = 'name', 'year', 'category', 'genre'
