from django.contrib import admin
from trialshop.models import Product,Product_Cat

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_type","product_name","product_brand","pub_date","product_price","cart_value","product_pic"]
    search_fields = ["product_name"]
    fieldsets = [
        (None,               {'fields':["product_type","product_pic","product_name","product_brand","product_price","cart_value"]}),
        ('Date information', {'fields': ['pub_date'], }),
    ]
    list_filter = ["product_type"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Cat)
