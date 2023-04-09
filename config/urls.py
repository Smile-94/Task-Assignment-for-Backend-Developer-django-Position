from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include


# Sample JWT toke configuration 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# # Sweagger Configuration
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

# drf-yasg - Yet another Swagger generator
schema_view = get_schema_view(
   openapi.Info(
      title="Care-box Blog Api",
      default_version='v1',
      description="Care Box api documentantion",
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


