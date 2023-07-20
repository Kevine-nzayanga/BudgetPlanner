from django.contrib import admin
from.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name","address","phoneNumber","thumbnail",
                    "pictures","cuisine","menu","opening_hours","closing_hours")

admin.site.register(Restaurant,RestaurantAdmin)
# Register your models here.
