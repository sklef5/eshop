from django import forms
from django.forms import ModelForm
from product.models import ProductModel, CategoryModel, ProductImagesModel, CategoryImagesModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'manufacturer', 'description', 'price', 'availability', 'category', 'currency']


class CreateCatForm(ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name', 'class_category', 'description']

class AddProdImageForm(ModelForm):
    class Meta:
        model = ProductImagesModel
        fields = 'name', 'locate'

class AddCatImageForm(ModelForm):
    class Meta:
        model = CategoryImagesModel
        fields = 'name', 'locate'