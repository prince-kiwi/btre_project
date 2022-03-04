from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','zipcode', 'price','list_date', 'realtor') 
    list_display_links = ('id','title')
    list_filter = ('realtor', 'is_published',)
    list_editable = ('is_published',)
    list_per_page = 25
    search_fields = ('title', 'description', 'address', 'city', 'state','zipcode', 'price',)

admin.site.register(Listing, ListingAdmin)
