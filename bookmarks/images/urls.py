from django.urls import path
from images import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
]