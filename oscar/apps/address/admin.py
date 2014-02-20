from django.contrib import admin
from oscar.core.loading import get_model


class UserAddressAdmin(admin.ModelAdmin):
    search_fields = (
        'first_name', 'last_name', 'line4', 'postcode', 'phone_number',
        'user__email',
    )
    readonly_fields = ('num_orders',)


admin.site.register(get_model('address', 'useraddress'), UserAddressAdmin)
admin.site.register(get_model('address', 'country'))
