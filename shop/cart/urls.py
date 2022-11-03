from django.urls import path

from shop.views import staff_user
from cart.views import cart_add, cart_view, orderitemview, orderlistview, allorderlistview, error, orderretunview, \
    orderstatusview, orderstatusagree, orderstatusrefus
from cart import views, apiview

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

    path('api/cart/', apiview.CartCreatetApiView.as_view(), name='api_cart'),
    path('api/cartlist/', apiview.CartListApiView.as_view(), name='api_cartlist'),
    path('api/cart/<int:pk>/', apiview.CartRUDApiView.as_view(), name='api_cart'),
    path('api/cartitem/', apiview.CartItemListApiView.as_view(), name='api_cartitem'),
    path('api/cartitem/<int:pk>/', apiview.CartItemRUDApiView.as_view(), name='api_cartitempk'),
    path('api/order/', apiview.OrderListApiView.as_view(), name='api_order'),
    path('api/order/<int:pk>', apiview.OrderItemRUDApiView.as_view(), name='api_orderpk'),
    path('api/orderitem/', apiview.OrdertItemListApiView.as_view(), name='api_orderitem'),
    path('api/orderitem/<int:pk>/', apiview.OrderItemRUDApiView.as_view(), name='api_orderitempk'),

       ]