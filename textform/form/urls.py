# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info_view, name='user_form'),  # Use only one view
]
