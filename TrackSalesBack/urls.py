
from django.contrib import admin
from django.urls import path, include


PREFIX = 'crm/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(PREFIX, include('crm.urls')),  # Include the user URLs under
]
