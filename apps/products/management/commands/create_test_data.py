import pdb
from decimal import Decimal

from django.core.management import BaseCommand
from django.contrib.auth.models import User

from apps.products.models import Recipe, Product, RecipeProduct

RECIPES = [
    {
        "name": "Паста карбонара",
        "products": [
            {"name": "Спагетти", "weight": 200},
            {"name": "Бекон", "weight": 150},
            {"name": "Яйцо", "weight": 50},
            {"name": "Чеснок", "weight": 10},
            {"name": "Сливочное масло", "weight": 20}
        ]
    },
    {
        "name": "Салат Цезарь",
        "products": [
            {"name": "Куриное филе", "weight": 200},
            {"name": "Листья салата", "weight": 100},
            {"name": "Хлебные крутончики", "weight": 50},
            {"name": "Пармезан", "weight": 30},
            {"name": "Соус Цезарь", "weight": 40}
        ]
    },
    {
        "name": "Греческий салат",
        "products": [
            {"name": "Огурцы", "weight": 150},
            {"name": "Помидоры", "weight": 200},
            {"name": "Фета", "weight": 100},
            {"name": "Маслины", "weight": 50},
            {"name": "Лимонный сок", "weight": 20}
        ]
    },
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin')
        for d in RECIPES:
            recipe = Recipe.objects.create(name=d['name'])
            for pd in d['products']:
                product = Product.objects.create(name=pd['name'])
                RecipeProduct.objects.create(recipe=recipe, product=product, weight=Decimal(pd['weight']))
