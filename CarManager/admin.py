from django.contrib import admin

from CarManager.models import Car


class CarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
