import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    published_date = django_filters.DateFilter(field_name='published_date', lookup_expr='exact')
    language = django_filters.CharFilter(field_name='language', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'published_date', 'language']
