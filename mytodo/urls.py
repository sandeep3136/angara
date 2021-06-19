from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("gettask", views.getTask, name="gettask"),
    path("delete<int:a>", views.deleteTask, name="del")
  
]