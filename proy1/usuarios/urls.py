from django.urls import path
from usuarios import views

urlpatterns = [
    path('homeUsuarios/', views.homeUsuarios, name='homeUsuarios'),
]