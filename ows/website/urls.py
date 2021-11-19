from django.urls import path
from website import views
from website import account_views, world_views

from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm

from . import views

urlpatterns = [
    path("", views.index,name="home"),
    path("login/", account_views.user_login,),
    path("passwordreset/", auth_views.PasswordResetView.as_view(
    template_name='website/account/password_reset1.html'),name='password_reset'),
    path("register/", account_views.register,), 
    path("read/", views.read,),
    path("read/news", views.readnews,),
    path('activate/<uidb64>/<token>/',
        account_views.activate, name='activate'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('worlds/create', world_views.create,),
]