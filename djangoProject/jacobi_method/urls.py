from django.urls import path
import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.solve)
]
