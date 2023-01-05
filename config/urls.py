from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="pybo",  # 타이틀
        default_version='v1.0.0',   # 버전
        description="pybo",   # 설명
        terms_of_service="",
        contact=openapi.Contact(email="hjh4212@naver.com")
),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('pybo.urls')), 
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    
    # swagger
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]

handler404 = 'common.views.page_not_found'