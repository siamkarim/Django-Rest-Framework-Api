from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.Api_list),
    path('detail/<int:pk>/', views.Api_detail),
]