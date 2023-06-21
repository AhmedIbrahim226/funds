from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAuth


@admin.register(UserAuth)
class MyUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = ('__str__', 'email', 'first_name', 'second_name', 'third_name', 'fourth_name', 'phone_number', 'is_active', 'is_superuser', 'is_staff')
    search_fields = ('email', 'phone_number',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_filter = ()

    fieldsets = (
        (None, {
            "fields": (
                'email', 'password', 'first_name', 'second_name', 'third_name', 'fourth_name', 'phone_number',)}),
        ('Permissions', {'fields': (
        'is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Personal', {'fields': ('date_joined', 'last_login')})
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'first_name', 'second_name', 'third_name', 'fourth_name', 'phone_number', 'is_active',
                    'is_superuser', 'is_staff')
            }
        ),
    )
