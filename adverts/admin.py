from django.contrib import admin
from .models import Category, City, Advert


admin.site.register(Category)
admin.site.register(City)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'city__name', 'category__name']
    list_display = ['title', 'created', 'city', 'category', 'views']
    list_filter = ['created', 'city', 'category']
    readonly_fields = ['views']


