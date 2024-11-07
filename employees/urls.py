# employees/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.employee_add, name='employee_add'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/update/<str:pk>/', views.department_update, name='department_update'),
    path('departments/delete/<str:pk>/', views.department_delete, name='department_delete'),
]
