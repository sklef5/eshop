from django.urls import path

from shop.views import staff_user
from product import views
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
    path('api/category/<slug:slug>/', views.CategoryListApiView.as_view(), name='api-category'),
    ]
