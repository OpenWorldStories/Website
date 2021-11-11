from django.urls import path
from website import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
]
