from django.contrib import admin
from django.urls import path
from blog import views  # 👈 conecta com seu app

urlpatterns = [
    path('', views.home, name='home'),  # 👈 agora renderiza HTML
    path('admin/', admin.site.urls),
]