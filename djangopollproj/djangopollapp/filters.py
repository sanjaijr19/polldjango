import django_filters
from .models import Poll

class PollFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    pub_date = django_filters.DateFilter()


    class Meta:
        model = Poll
        fields = ['title', 'description','pub_date']
