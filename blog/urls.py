from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),  # ✔ já resolvemos
    path('categoria/<slug:slug>/', views.category_detail, name='category-detail'),  # 👈 ADICIONA
]