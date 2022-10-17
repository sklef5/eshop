from django.conf import settings
from search.views import search
from search import views
from django.urls import path


urlpatterns = [
    path('', search, name='search'),
    ]