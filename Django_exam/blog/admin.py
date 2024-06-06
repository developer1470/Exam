from django.contrib.auth.models import Group, User
from django.contrib import admin
from blog.models import Product, Image, Attribute, Customers

# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'image')
admin.site.register(Customers, CustomersAdmin)


admin.site.unregister(Group)
admin.site.unregister(User)