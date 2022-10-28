from django.urls import path

from shop.views import staff_user
from product import views, apiviews
from product.views import productdetailview, addprodimage, addcatimage, productlistview, categorylistview

urlpatterns = [
    path('category/<slug:slug>/', productlistview, name="product_list"),
    path('addproduct/', staff_user(views.CreateProdView.as_view()), name='product_add'),
    path('addprodimage/<int:pk>/', addprodimage, name='addprodimage'),
    path('product/<int:pk>/', productdetailview, name='product_detail'),
    path('category/', categorylistview, name='category_list'),
    path('addcatimage/<int:pk>/', addcatimage, name='addcatimage'),
    path('category_/add/', staff_user(views.CreateCatView.as_view()), name='category_add'),
    path('delete/<int:pk>/', staff_user(views.DeleteProdView.as_view()), name="product_del"),
    path('product_upp/<int:pk>/', staff_user(views.UpdateProdView.as_view()), name='product_update'),

    path('api/category/', apiviews.CategoryListApiView.as_view(), name='api_category'),
    path('api/category/<int:pk>/', apiviews.CategoryRUDApiView.as_view(), name='api_categorypk'),
    path('api/product/', apiviews.ProductListApiView.as_view(), name='api_product'),
    path('api/product/<int:pk>/', apiviews.ProductRUDApiView.as_view(), name='api_productpk'),
    path('api/productimg/', apiviews.ProductImgListAiView.as_view(), name='api_productimg'),
    path('api/productimg/<int:pk>/', apiviews.ProductImgRUDAiView.as_view(), name='api_productimgpk'),
    path('api/categoryimg/', apiviews.CategoryImgListAiView.as_view(), name='api_categoryimg'),
    path('api/categoryimg/<int:pk>/', apiviews.CategoryImgRUDAiView.as_view(), name='api_categoryimgpk'),

]
