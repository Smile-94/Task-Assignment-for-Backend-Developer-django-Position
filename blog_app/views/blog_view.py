from django_filters.rest_framework import DjangoFilterBackend

# Generic Classes
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

# Import Bolog App Models Classes
from blog_app.models import BlogPost

# Import Blog App Serializers Classes
from blog_app.serializers import BlogListSerializers
from blog_app.serializers import BlogDetailsSerializers

# Blog app filters class
from blog_app.filters import BlogPostFilter

# Create your views here.

# Blog list view class
class BlogListDisplayView(ListAPIView):
    queryset = BlogPost.objects.filter(is_active = True)
    serializer_class = BlogListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogPostFilter

# Blog Details Class
class BlogDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.filter(is_active = True)
    serializer_class = BlogDetailsSerializers



