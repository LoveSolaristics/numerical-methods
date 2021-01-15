from django.urls import path
import gradient_descent.views

urlpatterns = [
    path('', gradient_descent.views.index),
]
