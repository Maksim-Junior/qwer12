from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_index),
    path('show/', views.handle_view),
]