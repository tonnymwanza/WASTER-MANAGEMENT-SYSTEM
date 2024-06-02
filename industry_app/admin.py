from django.contrib import admin

from . models import Contact
from . models import Register
# Register your models here.

@admin.register(Register)
class AdminWaste(admin.ModelAdmin):
    list_display = [
        'name',
        'waste_sources',
        'waste_collection',
        'transportation',
        'waste_separation',
        'waste_treatment',
        'waste_disposal'
    ]

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message'
    ]