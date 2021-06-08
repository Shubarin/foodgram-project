from django.contrib import admin

from .models import Contact, User


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'created')
    list_filter = ('user_from', 'user_to', 'created',)
    search_fields = ('user_from', 'user_to')
    ordering = ('created', 'user_from')
    date_hierarchy = 'created'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'username', 'is_active',
                   'is_staff', 'is_superuser')
    search_fields = ('email', 'username',)
    ordering = ('pk',)
