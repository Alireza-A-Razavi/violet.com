from django.contrib import admin

from .models import Item, Order, OrderItem, Category, MainCategory, ContactTicket

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(ContactTicket)


