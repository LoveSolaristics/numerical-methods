from django.urls import path
import jacobi_method.views

urlpatterns = [
    path('', jacobi_method.views.index),
    path('2/', jacobi_method.views.solve2),
    path('3/', jacobi_method.views.solve3),
    path('4/', jacobi_method.views.solve4)
]
