from django.contrib import admin
from Product.models import *
# Register your models here.

admin.site.register(Itemlist)

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price' , 'category')
    
admin.site.register(About)
admin.site.register(Feedback)
