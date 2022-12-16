from django.contrib import admin

from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass

@admin.register(SpandingCategories)
class SpandingCategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Spanding)
class SpandingAdmin(admin.ModelAdmin):
    pass

@admin.register(SpaceLogs)
class SpaceLogsAdmin(admin.ModelAdmin):
    pass

@admin.register(ReferalCode)
class ReferalCodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Shit)
class ShitAdmin(admin.ModelAdmin):
    pass