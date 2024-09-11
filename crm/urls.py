from django.urls import path, include
from rest_framework import routers
from .views import UserView, CompanyView,TaskView

router = routers.DefaultRouter()
router.register(r'users', UserView)  # Register the UserView with the router.  # The API endpoint will be /users/
router.register(r'companies', CompanyView)  # Register the CompanyView
router.register(r'tasks', TaskView)  # Include the task URLs

urlpatterns = [
    path('', include(router.urls)),
]