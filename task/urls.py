from django.urls import path
from rest_framework.routers import DefaultRouter
from task import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = router.urls
# [
#     path("categories/", views.CategoryListCreateView.as_view(), name="Get all"),
#     path("category/<int:id>/", views.CategoryDetailView.as_view(), name="Get by id"),
#     path("tasks/", views.ObavezaListCreateView.as_view(), name="Get all obaveze"),
#     path("task/<int:id>/", views.ObavezaDetailView.as_view(), name="Get obaveza by id"),
# ]