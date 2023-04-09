from django.contrib import admin
from django.urls import path
from django.urls import include

# Sample JWT toke configuration setting
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Apps Urls 
from blog_app import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('care-box/v1/', include(blog_urls)),
]

#JWT Tocken path
urlpatterns += [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


