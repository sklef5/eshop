from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from shop.views import staff_user
from product.forms import CreateCatForm, AddCatImageForm, AddProdImageForm
from product.models import ProductModel, CategoryModel, ProductImagesModel, CategoryImagesModel



#створення категорій та переляд
class CreateCatView(LoginRequiredMixin, CreateView):
    model = CategoryModel
    form_class = CreateCatForm
    template_name = 'product/category_add.html'
    success_url = reverse_lazy('category_list')

@staff_user
def addcatimage(request:HttpRequest, pk) -> HttpResponse:
    try:
        category = CategoryModel.objects.get(pk=pk)
        if request.method == "POST":
            form = AddCatImageForm(request.POST, request.FILES)
            form_img = form.save(commit=False) # Сохранение с помощью commit = False предоставляет вам объект модели,
            # затем вы можете добавить свои дополнительные данные и сохранить его
            form_img.category_id = pk
            form_img.save()
            messages.info(request, 'Фото додане')
        else:
            form = AddCatImageForm()
    except:
        return render(request, 'main/message_list.html', {'form': 'Сталася помилка'})
    return render(request, 'product/image_add.html', {'form': form})


def categorylistview(request:HttpRequest) -> HttpResponse:
    categories = CategoryModel.objects.all()
    images = CategoryImagesModel.objects.all()
    return render(request, 'product/category_list.html', dict(categories=categories, images=images))


#створення товарів, апдейт, видилення, додавання фото
class CreateProdView(LoginRequiredMixin, CreateView):
    model = ProductModel
    fields = 'name', 'manufacturer', 'description', 'price', 'availability', 'category', 'currency'
    template_name = 'product/product_add.html'
    success_url = reverse_lazy('category_list')


class UpdateProdView(LoginRequiredMixin, UpdateView):
    model = ProductModel
    fields = 'name', 'manufacturer', 'description', 'price', 'availability', 'category', 'currency'
    template_name = 'product/product_update.html'
    success_url = reverse_lazy('category_list')


class DeleteProdView(LoginRequiredMixin, DeleteView):
    model = ProductModel
    template_name = 'product/product_delete.html'
    success_url = '/'

@staff_user
def addprodimage(request:HttpRequest, pk) -> HttpResponse:
    try:
        product = ProductModel.objects.get(pk=pk)
        if request.method == "POST":
            form = AddProdImageForm(request.POST, request.FILES)
            form_img = form.save(commit=False) # Сохранение с помощью commit = False предоставляет вам объект модели,
            # затем вы можете добавить свои дополнительные данные и сохранить его
            form_img.product_id = pk
            form_img.save()
            messages.info(request, 'Фото додане')
        else:
            form = AddProdImageForm()
    except:
        return render(request, 'main/message_list.html', {'form': 'Сталася помилка'})
    return render(request, 'product/image_add.html', {'form': form})


def productlistview(request:HttpRequest, slug) -> HttpResponse:
    category = CategoryModel.objects.get(slug=slug)
    products = ProductModel.objects.filter(category__slug=slug)
    images = ProductImagesModel.objects.filter(product__category__slug=slug)

    return render(request, 'product/product_list.html', dict(products=products, category=category, images=images))


def productdetailview(request:HttpRequest, pk) -> HttpResponse:
    try:
        product = ProductModel.objects.get(pk=pk)
        images = ProductImagesModel.objects.filter(product_id=pk)

        return render(request, 'product/product_detail.html', dict(product=product, images=images))
    except ProductModel.DoesNotExist:
        return render(request, 'main/message_list.html', {'form': 'Товару не існує'})

