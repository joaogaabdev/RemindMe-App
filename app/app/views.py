from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def how_it_works(request):
    return render(request, 'howItWorks.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def pricing(request):
    return render(request, 'pricing.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def my_reminders(request):
    return render(request, 'my_reminders.html')

def settings(request):
    return render(request, 'settings.html')

def new_reminder(request):
    return render(request, 'new_reminder.html')