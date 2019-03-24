from django.contrib import admin


from .models import Product, Store


class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'photo', 'store',)


class StoreAdmin(admin.ModelAdmin):
    fields = ('title', 'address',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
