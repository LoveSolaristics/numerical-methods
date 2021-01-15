from django.urls import path
import views

urlpatterns = [
    path('', views.index),
    # path('<int:number>/', views.index_task)
]
