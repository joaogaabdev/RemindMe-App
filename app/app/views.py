from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def how_it_works(request):
    # O seu link HTML é para 'howItWorks.html'
    return render(request, 'howItWorks.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def pricing(request):
    return render(request, 'pricing.html')