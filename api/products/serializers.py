from rest_framework import serializers

from apps.products.models import Recipe, Product


class AddRecipeProductSerializer(serializers.Serializer):
    recipe_id = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    weight = serializers.DecimalField(max_digits=10, decimal_places=0)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


