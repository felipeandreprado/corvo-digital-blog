from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Meu blog está no ar no Render!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]