from django.urls import path
from . import views

# This file defines the URL routing for the tracker app.
# Each URL pattern maps a specific route to a corresponding view function.

urlpatterns = [
    
    # Home page route
    # Displays the motivation entry form where users can submit their message
    path('', views.home, name="home"),
    
    # List page route
    # Displays all saved motivation entries from the database
    path('list/', views.list_entries, name="list"),
]