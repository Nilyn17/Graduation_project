from django.contrib import admin
from progect_app.models import Wallet, Transaction
# Register your models here.


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass
    # list_display = ('wallet_name', 'wallet_status', 'wallet_state')
    # list_filter = ('wallet_status', 'wallet_state',)
    # search_fields = ('wallet_name',)


@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    pass
    # list_display = ('transaction_name', 'transaction_state')
    # list_filter = ('transaction_state',)
    # search_fields = ('transaction_name',)