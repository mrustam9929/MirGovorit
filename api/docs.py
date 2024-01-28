from django.urls import include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from api import urls

api_schema = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns=[
        re_path(r'api/', include(urls)),
    ],
)
