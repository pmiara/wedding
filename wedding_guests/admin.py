from django.contrib import admin

from .models import Guest, Page


#class GuestAdmin(admin.ModelAdmin):
#    exclude = ('gift',)
#
#admin.site.register(Guest, GuestAdmin)

admin.site.register(Guest)
admin.site.register(Page)
