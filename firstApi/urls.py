from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_list),
    path('detail/<int:pk>/', views.contact_detail),
]