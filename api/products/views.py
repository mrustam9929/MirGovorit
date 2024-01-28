from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from api.products.serializers import AddRecipeProductSerializer
from apps.products.models import RecipeProduct, Recipe, Product


class AddRecipeProductAPIView(generics.GenericAPIView):
    pagination_class = None

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('recipe_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('product_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('weight', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
        ]
    )
    def get(self, request, *args, **kwargs):
        serializer = AddRecipeProductSerializer(data=request.query_params, context=self.get_serializer_context())
        if not serializer.is_valid(raise_exception=False):
            raise ValidationError(serializer.errors)
        RecipeProduct.objects.add_product_to_recipe(
            recipe=serializer.validated_data['recipe_id'],
            product=serializer.validated_data['product_id'],
            weight=serializer.validated_data['weight']
        )
        return Response(status=status.HTTP_200_OK)


class CookRecipeAPIView(generics.GenericAPIView):
    pagination_class = None

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('recipe_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, *args, **kwargs):
        recipe = self.get_recipe()
        Product.objects.cook_recipe(recipe=recipe)
        return Response(status=status.HTTP_200_OK)

    def get_recipe(self):
        recipe_id = self.request.query_params['recipe_id']
        recipe = Recipe.objects.filter(id=recipe_id).first()
        if recipe is None:
            raise ValidationError({'recipe_id': 'Рецепт не найден'})
        return recipe
