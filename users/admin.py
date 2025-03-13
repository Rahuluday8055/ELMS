from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'name', 'role')
    list_filter = ('role', 'is_active', 'is_staff')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'name', 'role', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups & Permissions', {'fields': ('groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
