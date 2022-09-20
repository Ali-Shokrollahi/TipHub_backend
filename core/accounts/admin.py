from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    model = User

    list_display = ('email', 'is_active', 'role')
    list_filter = ('is_active', 'role', 'created')
    fieldsets = (
        ('Dates', {'fields': ('created', 'modified', 'last_login')}),
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'email_verified', 'role')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'image')}),
        ('Group and Permissions', {'fields': ('groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'role')}
         ),
    )
    search_fields = ('email',)
    ordering = ('-created',)
    readonly_fields = ('created', 'modified')


admin.site.register(User, UserAdmin)
