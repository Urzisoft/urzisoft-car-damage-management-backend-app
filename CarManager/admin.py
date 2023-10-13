from django.contrib import admin

from CarManager.models import CarsReport


class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarsReport, CarAdmin)
