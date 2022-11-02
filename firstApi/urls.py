from django.urls import path
from . import views

urlpatterns = [

    path('snip/', views.Blog_List.as_view()),
    path('snips/<int:pk>/', views.Blog_Detail.as_view()),
    path('gapi/', views.gnaric_List.as_view()),
    path('gdapi/<int:pk>/', views.gnaric_Detail.as_view()),
] 