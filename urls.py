from django.urls import path
from . import views

urlpatterns = [
    path('iniciar-sesion/', views.user_login, name = 'iniciosesion'),
]