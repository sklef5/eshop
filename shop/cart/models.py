from django.db import models
from user.models import UserModel
from product.models import ProductModel


class CartModel(models.Model):
    cart = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    client = models.ForeignKey(UserModel, related_name= 'clients', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='products', on_delete=models.CASCADE, verbose_name='Товар')
    cart = models.ForeignKey(CartModel, related_name='carts', on_delete=models.CASCADE, verbose_name='Кошик')
    quantity = models.IntegerField(verbose_name='Кількість')
    active = models.BooleanField(default=True, verbose_name='Активна')


    class Meta:
        db_table = 'CartItem'
    #
    # def sub_total(self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.product


class OrderModel(models.Model):
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserModel, related_name='users', on_delete=models.CASCADE, verbose_name='Клієнт')
    PROCESSING = 'в обр'
    CANCELLED = 'скас'
    APPROVED = 'оброб'
    CREATE = 'нове'
    STATUS = [
        (CREATE, 'новий'),
        (PROCESSING, 'у обробці'),
        (CANCELLED, 'скасовано'),
        (APPROVED, 'оброблено')
    ]
    status = models.CharField(
        max_length=6,
        choices=STATUS,
        default=CREATE,
        verbose_name='Статус заказу'
    )

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return self.user


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, related_name='orders', on_delete=models.CASCADE, verbose_name='Замовлення')
    product = models.ForeignKey(ProductModel, related_name='productsord',  on_delete=models.CASCADE, verbose_name='Товар')
    price = models.PositiveIntegerField(null=False, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(null=False, verbose_name='Кількість')

    class Meta:
        db_table = 'OrderItem'

    def __str__(self):
        return self.product

class OrderReturnModel(models.Model):
    order = models.ForeignKey(OrderModel, related_name='ordersret', on_delete=models.CASCADE, verbose_name='Замовлення')
    date_added = models.DateField(auto_now_add=True)
    date_up = models.DateField(auto_now=True)


    class Meta:
        db_table = 'OrderReturn'

    def __str__(self):
        return self.order

