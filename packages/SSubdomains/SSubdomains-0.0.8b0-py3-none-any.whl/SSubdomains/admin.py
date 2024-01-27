from django.contrib import admin

from SSubdomains.models import (Subdomain, )


class SubdomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_domain', 'created_at', 'last_update')
    # list_filter = ( 'team', 'position', 'date_birth')
    search_fields = ('name', 'base_domain', 'created_at', 'last_update')
    fieldsets = (
        (None, {
            'fields': ('name','urlconf', 'subdomain', 'base_domain', 'created_at', 'last_update'),
        }),
        ('Access', {
            'fields': ('allow_none', 'is_active','default_access'),
        }),
        ('Configuration', {
            'fields': ('included_by_groups', 'included_by_users', 'included_by_role', 'included_by_ip_range',
                          'excluded_by_groups', 'excluded_by_users', 'excluded_by_role', 'excluded_by_ip_range'),
        }),
        ('Excluded', {
            'fields': ('excluded_groups', 'excluded_users', 'excluded_role', 'excluded_ip_range_from',
                       'excluded_ip_range_to'),
        }),
        ('Included', {
            'fields': ('included_groups', 'included_users', 'included_role', 'included_ip_range_from',

                       'included_ip_range_to'),
        }),
    )
    readonly_fields = ('created_at', 'last_update')
    # raw_id_fields = ["domain"]


admin.site.register(Subdomain, SubdomainAdmin)
# Register your models here.
