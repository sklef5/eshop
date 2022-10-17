from django.contrib import admin
from product.models import ProductModel, CategoryModel, ProductImagesModel, CategoryImagesModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name",  "manufacturer", "price"]
admin.site.register(ProductModel, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [ "name", "class_category"]
admin.site.register(CategoryModel, CategoryAdmin)

admin.site.register(ProductImagesModel)

admin.site.register(CategoryImagesModel)