from django.urls import path
from . import views

app_name = 'autenticacao'
urlpattherns = [
    path('',views.login,name='login'),
]