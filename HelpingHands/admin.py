from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display=("id","user","contact","address","regdate")


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display=("id","user","contact","address","regdate")

@admin.register(DonationArea)
class DonationAreaAdmin(admin.ModelAdmin):
    list_display=("id","areaname","description","creationdate",)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display=("id","donor","volunteer","donationarea",)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=("id","donation","deliverypic","creationdate",)
