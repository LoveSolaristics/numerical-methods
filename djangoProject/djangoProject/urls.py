"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from homepage import views as homepage
from gradient_descent import views as gradient_descent
from dichotomy import views as dichotomy
from chord_method import views as chord_method
from jacobi_method import views as jacobi_method

urlpatterns = [
    path('', homepage.index),
    path('gradient_descent/', gradient_descent.index),
    path('dichotomy/', dichotomy.index),
    path('chord_method/', chord_method.index),
    path('jacobi_method/', jacobi_method.index),
]
