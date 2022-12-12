from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'is_staff'
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')}),
        ('Статус', {
            'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Остальные штуки', {'fields': ('last_login',)}),
    )
