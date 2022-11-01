from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'avatar', 'about_user', 'phone', 'gender', 'created_at', 'changed_at', )
    list_filter = ('email', 'first_name', 'last_name', 'avatar', 'about_user', 'phone', 'gender', 'created_at', 'changed_at')
    search_fields = ('email', 'first_name', 'last_name', 'avatar', 'about_user', 'phone', 'gender', 'created_at', 'changed_at')
    fields = ('email', 'first_name', 'last_name', 'avatar', 'about_user', 'phone', 'gender', 'groups')
    readonly_fields = ['id']


admin.site.register(Account, AccountAdmin)
