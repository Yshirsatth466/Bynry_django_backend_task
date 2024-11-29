from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # This includes URLs from the accounts app
    path('requests/', include('requests.urls')),  # This includes URLs from the requests app
    path('dashboard/', include('dashboard.urls')),  # This includes URLs from the dashboard app
]
