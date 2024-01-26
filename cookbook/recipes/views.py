from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()

    return JsonResponse({'message': 'Product added to recipe successfully'})
