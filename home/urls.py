from django.conf.urls import url
from django.urls import path
from .views import home
from register.views import AdminLogin, register
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', home, name="home" ),
    url(r'^register/$', register, name='reg'),
    path('login/', AdminLogin.as_view(), name="login"),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path("create/", views.create),

]
