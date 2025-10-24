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

# Em app/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # <-- GARANTA QUE VOCÊ ESTÁ IMPORTANDO O views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta você já tem e está funcionando:
    path('', views.home, name='home'), 
    
    # ADICIONE ESTAS LINHAS QUE ESTÃO FALTANDO:
    path('index.html', views.home, name='home-index'),
    path('features.html', views.features, name='features'),
    path('howItWorks.html', views.how_it_works, name='how-it-works'),
    path('signup.html', views.signup, name='signup'),
    path('login.html', views.login, name='login'),
    path('pricing.html', views.pricing, name='pricing'),
]
