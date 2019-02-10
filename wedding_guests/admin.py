from django.contrib import admin

from .models import Guest, Gift


class GuestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'attending', 'attending_afters', 'wants_bus', 'is_vegetarian', 'comments')
    list_filter = ('attending', 'wants_bus', 'is_vegetarian', 'attending_afters', 'eligible_for_afters')


admin.site.register(Guest, GuestAdmin)
admin.site.register(Gift)
