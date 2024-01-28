from django.db import models
from decimal import Decimal

from django.db.models import QuerySet, Q


class ProductManager(models.Manager):

    def cook_recipe(self, recipe: 'Recipe') -> None:
        products_ids = recipe.products.values_list('product_id', flat=True)
        self.filter(id__in=products_ids).update(use_count=models.F('use_count') + Decimal(1))


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    use_count = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Количество использований', default=0)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'products'

    def __str__(self) -> str:
        return f'{self.name}'


class RecipeManager(models.Manager):

    def show_recipes_without_product(self, product: 'Product') -> QuerySet['Recipe']:
        return self.filter(
            ~Q(products__product_id=product.pk) |
            Q(products__product_id=product.pk, products__weight__lt=Decimal(10))
        ).distinct()


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    objects = RecipeManager()

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        db_table = 'recipes'

    def __str__(self) -> str:
        return f'{self.name}'


class RecipeProductManager(models.Manager):

    def add_product_to_recipe(self, recipe, product, weight) -> 'RecipeProduct':
        instance, _ = self.update_or_create(
            recipe=recipe,
            product=product,
            defaults={'weight': weight}
        )
        return instance


class RecipeProduct(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name='Рецепт', related_name='products')
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, verbose_name='Продукт',
        related_name='recipes_products')
    weight = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Вес')

    objects = RecipeProductManager()

    class Meta:
        verbose_name = 'Продукт в рецепта'
        verbose_name_plural = 'Продукты в рецепте'
        db_table = 'recipe_products'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'product'],
                name='unique recipe product'
            )
        ]

    def __str__(self) -> str:
        return f'{self.product} - {self.weight} гр.'
