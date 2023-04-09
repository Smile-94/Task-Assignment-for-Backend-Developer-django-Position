import django_filters
from django.db.models import Q

# Import Blog Apps Models
from blog_app.models import BlogPost

# Import django defaults Models
from django.contrib.auth import get_user_model
User = get_user_model() #User Model



class BlogPostFilter(django_filters.FilterSet):
    # Filter by title or content using a keyword search
    search = django_filters.CharFilter(method='filter_by_search')

    # Filter by category
    category = django_filters.ChoiceFilter(choices=BlogPost.CATEGORY_CHOICES)

    # Filter by author
    author = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    # Filter by published date
    start_date = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')

    class Meta:
        model = BlogPost
        fields = ['search', 'category', 'author', 'start_date', 'end_date']

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(content__icontains=value))