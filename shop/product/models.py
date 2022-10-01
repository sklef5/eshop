from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from django.db.models import Q


class CategoryManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__icontains=query) | Q(description__icontains=query))
            qs = qs.filter(or_lookup)

        return qs


class CategoryModel(models.Model):
    objects = CategoryManager()

    name = models.CharField(max_length=38, unique=True, verbose_name="Категорія")  # str
    slug = models.SlugField(max_length=38, editable=False)
    class_category = models.IntegerField(null=False, verbose_name='Клас')  # str
    created_at = models.DateField(auto_now_add=True)  # date
    update_at = models.DateField(auto_now=True)  # date
    description = models.TextField(null=True, blank=True, verbose_name='Опис')  # data

    class Meta:
        db_table = 'Category'
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_list', kwargs={'slug':self.slug})


class ProductManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__icontains=query) | Q(description__icontains=query))
            qs = qs.filter(or_lookup)

        return qs


class ProductModel(models.Model):
    objects = ProductManager()

    name = models.CharField(max_length=150, verbose_name='Назва товару')  # str
    slug = models.SlugField(max_length=150, editable=False)
    manufacturer = models.CharField(max_length=38, null=True, verbose_name='Виробник')  # str
    created_at = models.DateField(auto_now_add=True)  # date
    update_at = models.DateField(auto_now=True)  # date
    description = models.TextField(null=True, blank=True, verbose_name='Опис товару')  # data
    price = models.FloatField(null=True, verbose_name='Ціна')
    availability = models.PositiveIntegerField(null=True, default=0, verbose_name='Наявність')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='categories', verbose_name='Категорія')
    currency = models.CharField(max_length=4, default="UAH", verbose_name='Валюта')  # str

    class Meta:
        db_table = 'Product'
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk':self.pk})

class ProductImagesModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Фото")
    created_at = models.DateField(auto_now_add=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='prodimg', verbose_name='Товар')
    locate = models.ImageField(upload_to='images/product/')

    class Meta:
        db_table = 'ProductImages'

    def __str__(self):
        return f'{self.product}'


class CategoryImagesModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Фото")
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='catimg', verbose_name='Категорія')
    locate = models.ImageField(upload_to='images/category/')

    class Meta:
        db_table = 'CategoryImages'

    def __str__(self):
        return f'{self.category}'