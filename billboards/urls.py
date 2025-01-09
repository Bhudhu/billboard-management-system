from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-coordinates/<int:billboard_id>/', views.add_coordinates, name='add_coordinates'),
    path('payment/<int:company_id>/', views.payment_form, name='payment_form'),
    path('mark-paid/<int:billboard_id>/', views.mark_paid, name='mark_paid'),
]
