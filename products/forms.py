from django.forms import ModelForm

from .models import Products

class ProductsForm(ModelForm):
    class Meta:
        model=Products
        fields=['Name','price','quantity']