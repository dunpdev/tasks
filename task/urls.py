from django.urls import path

from task import views

urlpatterns = [
    path("categories/", views.CategoryListCreateView.as_view(), name="Get all"),
    path("category/<int:id>/", views.CategoryDetailView.as_view(), name="Get by id"),
    path("tasks/", views.ObavezaListCreateView.as_view(), name="Get all obaveze"),
    path("task/<int:id>/", views.ObavezaDetailView.as_view(), name="Get obaveza by id"),
]