from django.db import models
from user.models import UserModel
from product.models import ProductModel


class CartModel(models.Model):
    basket = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'BasketModel'
        ordering = ['date_added']

    def __str__(self):
        return self.basket


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='Товар')
    basket = models.ForeignKey(CartModel, on_delete=models.CASCADE, verbose_name='Кошик')
    quantity = models.IntegerField(verbose_name='Кількість')
    active = models.BooleanField(default=True, verbose_name='Активна')


    class Meta:
        db_table = 'CartItemModel'
    #
    # def sub_total(self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.product


class OrderModel(models.Model):
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Клієнт')
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
        db_table = 'OrderModel'

    def __str__(self):
        return self.user


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, verbose_name='Замовлення')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.PositiveIntegerField(null=False, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(null=False, verbose_name='Кількість')

    class Meta:
        db_table = 'OrderItemModel'

    def __str__(self):
        return self.product

class OrderReturnModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, verbose_name='Замовлення')
    date_added = models.DateField(auto_now_add=True)
    date_up = models.DateField(auto_now=True)


    class Meta:
        db_table = 'OrderReturnModel'

    def __str__(self):
        return self.order

