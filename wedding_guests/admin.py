from django.contrib import admin

from .models import Guest


#class GuestAdmin(admin.ModelAdmin):
#    exclude = ('gift',)
#
#admin.site.register(Guest, GuestAdmin)

admin.site.register(Guest)
