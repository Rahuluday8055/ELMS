from django.urls import path
from .views import admin_dashboard, add_student,admin_login

urlpatterns = [
    path("login/", admin_login, name="admin_login"),
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add-student/", add_student, name="add_student"),
]
    