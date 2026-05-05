from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # 👈 chama seu template