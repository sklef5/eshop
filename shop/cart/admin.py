from django.contrib import admin
from cart.models import CartModel,  CartItemModel, OrderModel, OrderReturnModel, OrderItemModel

# Register your models here.
admin.site.register(CartModel)
admin.site.register(CartItemModel)
admin.site.register(OrderModel)
admin.site.register(OrderReturnModel)
admin.site.register(OrderItemModel)