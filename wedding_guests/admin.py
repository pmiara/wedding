from django.contrib import admin

from .models import Guest, Page


class GuestAdmin(admin.ModelAdmin):
    pass #exclude = ('gift',)


admin.site.register(Guest, GuestAdmin)
admin.site.register(Page)
