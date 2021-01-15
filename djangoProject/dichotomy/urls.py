from django.urls import path
import dichotomy.views

urlpatterns = [
    path('', dichotomy.views.index),
]
