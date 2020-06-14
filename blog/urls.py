from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_pass,name = 'blog-home'),
    
]
