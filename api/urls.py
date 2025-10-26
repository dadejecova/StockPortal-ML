from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename ='employee')

urlpatterns = [
    # Define your API endpoints here
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),
    path('', include(router.urls)),

    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]