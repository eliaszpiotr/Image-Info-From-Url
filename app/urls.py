from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('detail/<str:id>/', views.detail, name='detail'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('edit/<str:id>/', views.edit, name='edit'),
]