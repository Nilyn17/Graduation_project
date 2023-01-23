from django.contrib import admin

from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass

@admin.register(SpendingCategory)
class SpandingCategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Spending)
class SpandingAdmin(admin.ModelAdmin):
    pass

@admin.register(SpaceLog)
class SpaceLogsAdmin(admin.ModelAdmin):
    pass

@admin.register(ReferalCode)
class ReferalCodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Shit)
class ShitAdmin(admin.ModelAdmin):
    pass