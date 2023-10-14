from django.contrib import admin

from CarManager.models import CarsReport


class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'damage_severity', )
    filter = ('damage_severity', )


admin.site.register(CarsReport, CarAdmin)
