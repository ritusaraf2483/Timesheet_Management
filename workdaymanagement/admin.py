from django.contrib import admin
from workdaymanagement.models import Workday, Location


class AdminWorkday(admin.ModelAdmin):
    list_display = ['user','location','sector','work_date','time_in','time_out','hours_code','FBP_payroll','AMCO_payroll']

class AdminLocation(admin.ModelAdmin):
    list_display = ['location']

admin.site.register(Workday,AdminWorkday)
admin.site.register(Location,AdminLocation)