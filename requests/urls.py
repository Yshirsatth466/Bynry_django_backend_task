from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('<int:pk>/', views.request_detail, name='request_detail'),
    path('new/', views.submit_request, name='submit_request'),
]
