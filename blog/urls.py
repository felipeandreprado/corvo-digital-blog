from django.urls import path
from . import views

app_name = 'blog'  # 👈 ISSO RESOLVE O ERRO

urlpatterns = [
    path('', views.home, name='home'),
]