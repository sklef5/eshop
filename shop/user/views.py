from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from shop.views import staff_user
from user.forms import  UpdateLogForm, SignUpForm
from user.models import UserModel
from django.views.generic import UpdateView, ListView, DetailView

'''реєстраціяб  вхід, вихід юзера'''


def createuser(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.create_user()
            return HttpResponseRedirect(reverse_lazy('homepage'))
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


class LoginUserView(LoginView):
    success_url = '/'
    template_name = 'user/signin.html'

    def get_success_url(self):
        return self.success_url


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = '/'

'''оновлення полів юзера'''
class UserFieldUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = 'user/change.html'
    fields = 'email', 'first_name', "last_name"
    success_url = "/"


class UserLogUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = UpdateLogForm
    template_name = 'user/change.html'
    success_url = "/"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = 'user/change.html'
    success_url = "/"
    fields = 'is_superuser', 'is_active', 'is_staff'


'''профіль юзера'''
class UserDetaelView(LoginRequiredMixin, DetailView):
    template_name = 'user/profile.html'
    model = UserModel

'''лист користувачів - для адміна'''
class UserlListView(LoginRequiredMixin, ListView):
    template_name = 'user/user_list.html'

    def get_queryset(self):
        return UserModel.objects.all()
