from django.contrib import admin

from .models import Car, ClientCard, Transaction


admin.site.register(Car)
admin.site.register(Transaction)
admin.site.register(ClientCard)
