from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =  format_suffix_patterns([

    path('snip/', views.Blog_List.as_view()),
    path('snips/<int:pk>/', views.Blog_Detail.as_view()),
    path('gapi/', views.gnaric_List.as_view(), name='contact-list'),
    path('gdapi/<int:pk>/', views.gnaric_Detail.as_view()),
    path('', views.api_root),
])