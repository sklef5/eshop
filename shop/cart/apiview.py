from cart.models import CartModel, CartItemModel, OrderModel, OrderItemModel, OrderReturnModel
from cart.serializer import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer, OrderReturnSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

class CartListApiView(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()

class CartRUDApiView(UpdateAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()

class CartItemListApiView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()

class CartItemRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()


class OrderListApiView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()

class OrderRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()

class OrdertItemListApiView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItemModel.objects.all()

class OrderItemRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItemModel.objects.all()


class OrderReturnListApiView(ListCreateAPIView):
    serializer_class = OrderReturnSerializer
    queryset = OrderReturnModel.objects.all()

class OrderReturnRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderReturnSerializer
    queryset = OrderReturnModel.objects.all()