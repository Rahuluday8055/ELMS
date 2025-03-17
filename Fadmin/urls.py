from django.urls import path
from .views import admin_dashboard, add_student

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add-student1/", add_student, name="add_student"),
]
    