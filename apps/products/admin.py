from django.contrib import admin

from apps.products.models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.StackedInline):
    model = RecipeProduct
    extra = 0
    show_change_link = True
    fields = ('product', 'weight')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'use_count')
    list_display_links = ('id', 'name', 'use_count')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    inlines = (RecipeProductInline,)


