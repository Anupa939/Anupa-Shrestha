from django.contrib import admin
from .models import PaymentGateway


# Register your models here.

class PaymentGatewayAdmin(admin.ModelAdmin): 
 list_display = [ "balance","token", "expiry_date", "is_active",]

class Meta: 
 model = PaymentGateway 
admin.site.register(PaymentGateway, PaymentGatewayAdmin)
