"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'), 
    
    path('index.html', views.home, name='home-index'),
    path('features.html', views.features, name='features'),
    path('howItWorks.html', views.how_it_works, name='how-it-works'),
    path('signup.html', views.signup, name='signup'),
    path('login.html', views.login, name='login'),
    path('pricing.html', views.pricing, name='pricing'),
    path('admin_dashboard.html', views.admin_dashboard, name='admin-dashboard'),
    path('my_reminders.html', views.my_reminders, name='my-reminders'),
    path('settings.html', views.settings, name='settings'),
    path('new_reminder.html', views.new_reminder, name='new-reminder'),
    path('my_profile.html', views.my_profile, name='my-profile'),
]
