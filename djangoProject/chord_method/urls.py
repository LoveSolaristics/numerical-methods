from django.urls import path
import chord_method.views

urlpatterns = [
    path('', chord_method.views.index),
]
