from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.admin import AdminSite

# Customize Admin Site
admin.site.site_header = "Ogani Administration"
admin.site.site_title = "Ogani Admin Portal"
admin.site.index_title = "Welcome to Ogani Admin"

# Register your models here.
admin.site.register(user)
admin.site.register(category)
admin.site.register(product)
admin.site.register(wishlist)
admin.site.register(Cart)
admin.site.register(Billing_Details)
admin.site.register(order)
admin.site.register(contact_us)
