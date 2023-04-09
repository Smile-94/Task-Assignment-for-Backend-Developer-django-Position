from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include


# Import blog app Views
from blog_app.views import blog_view
from blog_app.views import manage_blog

app_name = 'blog_app'

# Router configuration
router = DefaultRouter()
router.register(r'blogs', manage_blog.AuthorBlogView)

# Router Urls path
urlpatterns = [
     path('', include(router.urls)),
]

# Blog View urls
urlpatterns += [
    path('blog-list/', blog_view.BlogListDisplayView.as_view(), name='blog_list'),
    path('blog-detail/<int:pk>/', blog_view.BlogDetailView.as_view(), name='blog_detail')
]
