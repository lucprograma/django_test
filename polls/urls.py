"""
This file contains the URLs that bellong to the polls app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_task, name="create_task"),
    path("index", views.list_tasks, name="list_tasks"),
    path("<int:id>/delete", views.delete_task, name="delete_tasks"),
    path("<int:id>/update", views.update_task, name="update_tasks"),
]
