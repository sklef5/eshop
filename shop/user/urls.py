from django.urls import path
from django.conf import settings

from shop.views import staff_user
from user import views
from user.views import createuser

urlpatterns = [
    path('profile/<int:pk>/', views.UserDetaelView.as_view(),  name='profile_detail'),
    path(settings.LOGIN_URL, views.LoginUserView.as_view(), name="signin"),   # в settings ставим адрес по умолч
    path('signout/', views.LogoutUserView.as_view(), name='signout'),
    path('signup/', createuser, name="signup"),
    path('field/<slug:slug>/', views.UserFieldUpdateView.as_view(), name="update"),
    path('login/<slug:slug>/', views.UserLogUpdateView.as_view(), name="update_log"),
    path('user/all/', staff_user(views.UserlListView.as_view()), name='user_list'),
    path('user/<slug:slug>/', staff_user(views.UserUpdateView.as_view()), name='update_user_prof')
    ]