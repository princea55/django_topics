from django.contrib import admin

from web.forms.models import Product, Contact, SaleOrder, Tag

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(SaleOrder)
admin.site.register(Tag)
# Register your models here.
