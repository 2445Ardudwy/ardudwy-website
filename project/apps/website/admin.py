from django.contrib import admin
from .models import Contact, StaffMembers


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'purpose']
    search_fields = ['pk', 'first_name', 'last_name', 'email', 'telephone']
    readonly_fields = ['first_name', 'last_name', 'email', 'telephone', 'purpose', 'message']
    ordering = ['pk']
    fieldsets = (
        (None, {'fields': ['first_name', 'last_name']}),
        ('Contact Details', {'fields': ['email', 'telephone']}),
        ('Contact Reason', {'fields': ['purpose', 'message']})
    )


class StaffMembersAdmin(admin.ModelAdmin):
    list_display = ['rank', 'last_name', 'first_name', 'active']
    search_fields = ['rank', 'first_name', 'last_name', 'position']
    readonly_fields = []
    ordering = ['last_name', 'first_name', 'rank']
    fieldsets = (
        (None, {'fields': ['rank', 'first_name', 'last_name']}),
        ('Staff Details', {'fields': ['position', 'bio', 'image', 'email']}),
        ("Staff's Availability", {'fields': ['active']})
    )

admin.site.register(Contact, ContactUsAdmin)
admin.site.register(StaffMembers, StaffMembersAdmin)
