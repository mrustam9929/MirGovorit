from django.contrib import admin
from django.urls import path, include

from api.docs import api_schema
from apps.products.views import RecipeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', api_schema.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('api.urls')),
    path('recipe-list/<int:pk>/', RecipeListView.as_view()),
]
