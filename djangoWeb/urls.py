
from django.contrib import admin
from django.urls import path, include
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('iniciar-sesion/', include('task.urls')),
]
