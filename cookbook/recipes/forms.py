from django import forms
from .models import RecipeProduct


class RecipeProductForm(forms.ModelForm):
    class Meta:
        model = RecipeProduct
        fields = ['product', 'weight']
