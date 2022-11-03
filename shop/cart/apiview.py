from cart.models import CartModel, CartItemModel, OrderModel, OrderItemModel, OrderReturnModel
from cart.serializer import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer, OrderReturnSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import permissions

class CartCreatetApiView(CreateAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class CartListApiView(ListAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()
    permission_classes = [permissions.IsAdminUser]

class CartRUDApiView(UpdateAPIView):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class CartItemListApiView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class CartItemRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItemModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrderListApiView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrderRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrdertItemListApiView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItemModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrderItemRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItemModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrderReturnListApiView(ListCreateAPIView):
    serializer_class = OrderReturnSerializer
    queryset = OrderReturnModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class OrderReturnRUDApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderReturnSerializer
    queryset = OrderReturnModel.objects.all()
    permission_classes = [permissions.IsAdminUser]