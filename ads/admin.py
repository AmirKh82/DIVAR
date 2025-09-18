from django.contrib import admin
from .models import Category , City , ads
# Register your models here.

class Category_Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


class City_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class ads_Admin(admin.ModelAdmin):
    list_display = ['city','category','name','price','status','amount','image']
    search_fields = ['city','category','name','price',]
    list_filter = ['city','category','name','price',]


admin.site.register(Category,Category_Admin)
admin.site.register(City,City_Admin)
admin.site.register(ads,ads_Admin)