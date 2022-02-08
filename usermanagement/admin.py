from django.contrib import admin

from usermanagement.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ['id','f_name','l_name','image']

admin.site.register(User,AdminUser)
