from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.prueba),
    path('', views.Buscarusuario.as_view(), name='inicio')
]