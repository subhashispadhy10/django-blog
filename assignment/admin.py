from django.contrib import admin

# Register your models here.
from . models import *

@admin.register(About)
class about_Admin(admin.ModelAdmin):
    list_display=['about_title','about_description']

    def has_add_permission(self, request):
        c=About.objects.all().count()
        if c==0:
            return True
        return False

@admin.register(Social)
class Social_Admin(admin.ModelAdmin):
    list_display=['name']