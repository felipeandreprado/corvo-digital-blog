from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'home.html')  # temporário

def category_detail(request, slug):
    return render(request, 'home.html')  # temporário