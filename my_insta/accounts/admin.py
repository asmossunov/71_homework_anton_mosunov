from django.contrib import admin
from accounts.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'about_user', 'phone', 'gender')
    list_filter = ('email', 'avatar', 'about_user', 'phone', 'gender')
    search_fields = ('email', 'avatar', 'about_user', 'phone', 'gender')
    fields = ('email', 'avatar', 'about_user', 'phone', 'gender')
    readonly_fields = ['id']


admin.site.register(Account, AccountAdmin)
