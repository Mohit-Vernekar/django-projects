from django.urls import path
from project_app import views

urlpatterns = [
    path('', views.users, name='users'),
]
