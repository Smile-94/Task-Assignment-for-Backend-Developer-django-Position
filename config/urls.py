from django.contrib import admin
from django.urls import path
from django.urls import include

# Apps Urls 
from blog_app import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('care-box/v1/', include(blog_urls)),
]
