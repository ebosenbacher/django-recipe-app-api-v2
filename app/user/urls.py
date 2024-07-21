"""
URL amppings for the user API.
"""
from django.urls import path

from user import views


# used for reverse mapping in the test
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]