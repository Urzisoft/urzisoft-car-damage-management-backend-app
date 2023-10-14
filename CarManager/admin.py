from django.contrib import admin

from CarManager.models import CarsReport


class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'damage_severity', 'car_entry_date', 'car_leave_date', 'done')
    filter = ('damage_severity', 'car_entry_date', 'car_leave_date', 'done')


admin.site.register(CarsReport, CarAdmin)
admin.site.site_header = 'CarManagement'
