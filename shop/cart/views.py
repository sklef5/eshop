from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from shop.views import staff_user
from product.models import ProductModel
from cart.models import CartModel, CartItemModel, OrderModel, OrderReturnModel, OrderItemModel
from user.models import UserModel

#створення кошика
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.session_key.create()
    return cart


def cart_add(request, pk):
    product = ProductModel.objects.get(pk=pk)
    client = request.user.id
    cash = UserModel.objects.get(id=client)
    if product.price < cash.cash:
        cart = CartModel.objects.get_or_create(client_id=client, cart=cart_id(request), defaults=None)
        try:
            cart_item = CartItemModel.objects.get(product_id=product, cart_id=cart[0].id)
            if cart_item.quantity < cart_item.product.availability:
                cart_item.quantity += 1
            cart_item.save()
        except CartItemModel.DoesNotExist:
            cart_item = CartItemModel.objects.create(
                        product=product,
                        quantity=1,
                        cart_id=cart[0].id,
                )
            cart_item.save()
        product.availability -= 1
        product.save()
        return redirect('category_list')
    else:
        return render(request, 'main/message_list.html',
                      {'form': "Вибачте, на Вашому рахунку не достатньо коштів для цього замовлення"})

#перегляд кошика
def cart_view(request: HttpRequest, total=0, counter= 0) -> HttpResponse:
    client = request.user.id
    bas_numb = CartModel.objects.filter(client_id=client)
    cartitems = CartItemModel.objects.filter(cart_id__client_id=client, active=True)
    for cartitem in cartitems:
        total += (cartitem.product.price * cartitem.quantity)
        counter += cartitem.quantity

    return render(request, "cart/cart.html", dict(form=cartitems, total=total, counter=counter, bas_numb=bas_numb))

#створення замовлення
def orderitemview(request: HttpRequest, pk):
    try:
        cart = CartModel.objects.get(id=pk)
    except CartModel.DoesNotExist:
        return render(request, 'main/message_list.html', {'form': "Кошик не існує"})

    cartitems = CartItemModel.objects.filter(cart=cart)
    user = request.user.id
    cash = UserModel.objects.get(id=user)
    order = OrderModel.objects.create(user_id=user)
    for cartitem in cartitems:
        try:
            cash.cash -= cartitem.product.price * cartitem.quantity
            cash.save()
        except:
            return render(request, 'main/message_list.html', {'form': "Недостатьо коштів на рахунку"})

        OrderItemModel.objects.create(
            order=order,
            product=cartitem.product,
            price=cartitem.product.price,
            quantity=cartitem.quantity,
        )
    cart.delete()
    return render(request, 'main/message_list.html', {'form': "Дякуємо за Ваше замовлення"})

#перегляд замовлень юзера
def orderlistview(request: HttpRequest, pk: int) -> HttpResponse:
    order = OrderModel.objects.filter(user_id=pk).order_by('user')
    item = OrderItemModel.objects.filter(order__user=pk)
    return render(request, 'cart/order_list.html', dict(order=order, item=item))

#перегляд всіх замовлень для адміна
@staff_user
def allorderlistview(request: HttpRequest) -> HttpResponse:
    order = OrderModel.objects.all()
    item = OrderItemModel.objects.all()
    return render(request, 'cart/order_list.html', dict(order=order, item=item))

#повернення замовлення
def orderretunview(request: HttpRequest, id) -> HttpResponse:
    try:
        orderreturn = OrderReturnModel.objects.get(order_id=id)
        return render(request, 'main/message_list.html', {'form': "Повернення вже зараєстровано"})
    except OrderReturnModel.DoesNotExist:

        order = OrderModel.objects.get(id=id)
        orderreturn = OrderReturnModel.objects.create(
            order_id=order.pk,
        )
        orderreturn.save()

        order.status = 'у обробці'
        order.save()
        return render(request, 'main/message_list.html', {'form': 'Замовлення прийняте на обробку'})

#список повернень
class OrderReturnList(LoginRequiredMixin, ListView):
    model = OrderReturnModel
    template_name = 'cart/orderreturnlist.html'

    def get_queryset(self):
        return OrderReturnModel.objects.all()

@staff_user
def orderstatusview(request:HttpRequest, pk) -> HttpResponse:
    order = OrderModel.objects.get(id=pk)
    orderitem =OrderItemModel.objects.filter(order_id=pk)

    return render(request, 'cart/order_update.html', dict(form=orderitem, number=order))

#повернення замовлення
@staff_user
def orderstatusagree(request: HttpRequest, pk) -> HttpResponse:
    order = OrderModel.objects.get(id=pk)
    orderitem = OrderItemModel.objects.filter(order_id=pk)
    user = UserModel.objects.get(id=order.user.id)
    for item in orderitem:
        user.cash += item.price * item.quantity
        product = ProductModel.objects.get(id=item.product.pk)
        product.availability += item.quantity
        item.quantity = 0
        item.price = 0
        order.status = 'скасовано'
        order.save()
        product.save()
        user.save()
        item.save()
    return render(request, 'main/message_list.html', {'form': 'Замовлення скасовано'})

#відмова у поверненні
@staff_user
def orderstatusrefus(request:HttpRequest, pk):
    order = OrderModel.objects.get(id=pk)
    order.status = 'оброблено'
    order.save()

    return render(request, 'main/message_list.html', {'form': 'У поверненні відмовлено'})


def error(request):
    return render(request, 'main/message_list.html')
