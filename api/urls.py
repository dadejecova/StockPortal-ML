from django.urls import path
from . import views

urlpatterns = [
    # Define your API endpoints here
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),
]