from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseNotFound, Http404

from apps.products.models import Recipe, Product


class RecipeListView(ListView):
    template_name = 'recipes-list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.show_recipes_without_product(product=self.get_product())

    def get_product(self) -> Product:
        product = Product.objects.filter(pk=self.kwargs['pk']).first()
        if product is None:
            raise Http404('Product not found')
        return product
