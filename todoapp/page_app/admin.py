from django.contrib import admin
from .models import Profile, Category, Task , Quotes

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","type")
    list_display =("id","type")

admin.site.register(Profile,ProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_filter =("id","name")
    list_display =("id","name")
admin.site.register(Category,CategoryAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_filter =("id","title")
    list_display =("id","title")
admin.site.register(Task,TaskAdmin)


class QuotesAdmin(admin.ModelAdmin):
    list_filter =("title","description")
    list_display =("title","description")
admin.site.register(Quotes,QuotesAdmin)