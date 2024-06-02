from django.contrib import admin

from . models import Waste
# Register your models here.

@admin.register(Waste)
class AdminWaste(admin.ModelAdmin):
    list_display = [
        'waste_sources',
        'waste_collection',
        'transportation',
        'waste_separation',
        'waste_treatment',
        'waste_disposal'
    ]