from django.contrib import admin
from .models import Company, Billboard, Payment

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'reference_number')


@admin.register(Billboard)
class BillboardAdmin(admin.ModelAdmin):
    list_display = ('location', 'rented_by', 'is_paid')
    list_filter = ('is_paid',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('company', 'amount', 'date', 'transaction_id')
    list_filter = ('date',)
