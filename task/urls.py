from django.urls import path

from task import views

urlpatterns = [
    path("get_all_categories/", views.get_all_categories, name="Get all"),
    path("get/<int:id>/", views.get_category_by_id, name="Get by id"),
    #path("create/", views.save, name="Create new task"),
    #path("update/<int:id>/", views.update, name="Update existing task"),
    #path("delete/<int:id>/", views.delete, name="Delete existing task"),
]