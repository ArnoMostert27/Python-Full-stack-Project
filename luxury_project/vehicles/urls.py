from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_vehicles, name='vehicles'),
    path('create/', views.create_vehicle, name='create_vehicle'),
    path('edit/<int:id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),
]