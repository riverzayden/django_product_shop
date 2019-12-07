from django import forms
from .models import Shop, Product


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
