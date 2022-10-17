from django.urls import path

from shop.views import staff_user
from cart.views import cart_add, cart_view, orderitemview, orderlistview, allorderlistview, error, orderretunview, \
    orderstatusview, orderstatusagree, orderstatusrefus
from cart import views

urlpatterns = [
    path('cart/', cart_view , name='cart_view'),
    path('cart_add/<int:pk>/', cart_add, name='cart_add'),
    path('order_add/<int:pk>/', orderitemview, name='order_add'),
    path('orderuser_list/<int:pk>/', orderlistview, name='order_user'),
    path('order_list/', allorderlistview, name='order_all'),
    path("orderreturn/<int:id>/", orderretunview, name='orderreturn'),
    path('ord_returnlist/', staff_user(views.OrderReturnList.as_view()), name='returnorderlist'),
    path('orderstatus/<int:pk>/', orderstatusview, name='order_status'),
    path('returnagree/<int:pk>/', orderstatusagree, name='return_agreed'),
    path('returnrefus/<int:pk>/', orderstatusrefus, name='return_refusal'),
    path('error/', error, name='error'),







       ]