from django.urls import include, path
from api.products import views

urlpatterns = [
    path('add-recipe-product/', views.AddRecipeProductAPIView.as_view()),
    path('cook-recipe/', views.CookRecipeAPIView.as_view()),
]
