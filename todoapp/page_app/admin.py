from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","type")
    list_display =("id","type")

admin.site.register(Profile,ProfileAdmin)