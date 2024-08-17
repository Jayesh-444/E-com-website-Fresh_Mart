from django.contrib import admin

# Register your models here.
from .models import*

class orderitemTabularInline(admin.TabularInline):
    model = orderitem
class orderAdmin(admin.ModelAdmin):
    inlines = [orderitemTabularInline]

admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(order,orderAdmin)
admin.site.register(orderitem)


