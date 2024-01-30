from django.contrib import admin
from .forms import RecipeProductForm
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    form = RecipeProductForm


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeProductInline,
    ]
    list_display = ('pk', 'name')


admin.site.register(Product)
admin.site.register(RecipeProduct)
