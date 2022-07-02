from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
import celery_app

urlpatterns = [
    path('', views.test_func)
]
