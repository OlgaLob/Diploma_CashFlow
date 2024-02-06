from django.contrib import admin

from .models import BankStatementsRes


@admin.register(BankStatementsRes)
class BankStatementsResAdmin(admin.ModelAdmin):
    list_display = ['article_revenue', 'date', 'revenue', 'write_off',
                    'purpose_of_payment', 'contractor',
                    'transaction_type', 'division']
    list_filter = ('date', 'division', 'article_revenue')
    date_hierarchy = 'date'
    search_fields = ['article_revenue', 'division']


