# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import User, Profile


class UserResource(resources.ModelResource):

    class Meta:
        model = User

@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):
    """Define admin model for custom User model with no email field."""
    resource_class = UserResource
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('date_joined',)
    # readonly_fields = ('-date_joined',)


class ProfileResource(resources.ModelResource):

    class Meta:
        model = Profile


class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'contact', 'college_name', 'year_of_study')
    search_fields = ('full_name', 'contact', )


admin.site.register(Profile, ProfileAdmin)