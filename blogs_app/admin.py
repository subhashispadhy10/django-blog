from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(category)
class category_admin(admin.ModelAdmin):
    list_display=['id','category']

@admin.register(Blog)
class blog_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['id','title','author','category_blog','status']
    search_fields=['id','title','category_blog__category']
