from django.urls import path
from django.urls.conf import include
from firstApi import views
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
urlpatterns = [
    path('',include( router.urls))
]