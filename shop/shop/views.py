from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from shop.settings import  HOME_URL


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html')


def staff_user(
    view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=HOME_URL
):
    actual_decorator = user_passes_test(
        lambda u:  u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator