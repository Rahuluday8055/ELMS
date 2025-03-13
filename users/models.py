from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

# User roles
USER_ROLES = [
    ('superuser', 'Superuser'),
    ('admin', 'Admin'),
    ('trainer', 'Trainer'),
    ('student', 'Student'),
]

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, role, password=None):
        if not email:
            raise ValueError("Email is required")
        if role not in dict(USER_ROLES):
            raise ValueError("Invalid role")
        if not password:
            raise ValueError("Password is required")  # Ensure password is mandatory

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, role='superuser', password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return f"{self.name} ({self.role})"
