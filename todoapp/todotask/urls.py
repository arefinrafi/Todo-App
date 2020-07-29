from django.urls import path
from . import views


urlpatterns = [
    path('', views.task, name='task'),
    path('/update/<int:pk>/', views.update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]