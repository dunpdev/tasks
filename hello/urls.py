from django.urls import path

from hello import views

urlpatterns = [
    path("index/", views.get_all, name="index"),
]