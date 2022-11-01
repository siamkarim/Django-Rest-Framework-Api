from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.Api_list),
    path('detail/<int:pk>/', views.Api_detail),
    path('snip/', views.Api_List.as_view()),
    path('snips/<int:pk>/', views.Api_Detail.as_view()),
]