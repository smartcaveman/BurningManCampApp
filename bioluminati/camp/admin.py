from django.contrib import admin

from .models import MealShifts, UserProfile, Bikes, Inventory, BicycleMutationInventory, BikeMutationSchedule

admin.site.register(MealShifts)
admin.site.register(UserProfile)
admin.site.register(Bikes) 
admin.site.register(Inventory)
admin.site.register(BicycleMutationInventory)
admin.site.register(BikeMutationSchedule)
