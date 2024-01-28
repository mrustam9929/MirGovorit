from django.urls import include, path

urlpatterns = [
    path('products/', include('api.products.urls')),
]
