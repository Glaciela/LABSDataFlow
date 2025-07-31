from django.contrib import admin

from .models import Organization, Position, Sector, TypePosition, UserProfile


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organization_acronym', 'organization_code')
    search_fields = ('organization_name', 'organization_acronym')
    ordering = ('organization_name',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_name', 'sector_acronym', 'sector_code')
    search_fields = ('sector_name', 'sector_acronym')
    ordering = ('sector_name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'type_position')
    search_fields = ('position_name', 'type_position__type_name')
    ordering = ('position_name',)

@admin.register(TypePosition)
class TypePositionAdmin(admin.ModelAdmin):  
    list_display = ('type_name',)
    search_fields = ('type_name',)
    ordering = ('type_name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position')