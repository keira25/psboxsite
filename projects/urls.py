from django.urls import path
from . import views

urlpatterns = [
  path('', views.projects_all, name="all"),
]