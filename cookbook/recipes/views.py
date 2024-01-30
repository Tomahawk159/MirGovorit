from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db import transaction
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()

    return HttpResponse("Product added to recipe successfully")


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    with transaction.atomic():
        updated_products = []
        recipe_products = RecipeProduct.objects.filter(recipe=recipe)
        for recipe_product in recipe_products:
            product = recipe_product.product
            product.times_cooked += 1
            updated_products.append(product)

        Product.objects.bulk_update(updated_products, fields=('times_cooked',))
    return HttpResponse("Recipe cooked successfully")


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    recipes_without_product = Recipe.objects.filter((Q(recipeproduct__product=product) &
                                                    Q(recipeproduct__weight__lt=10))
                                                    | ~Q(recipeproduct__product=product)).distinct()
    context = {
        'recipes': recipes_without_product
    }

    return render(request, 'recipes.html', context)
