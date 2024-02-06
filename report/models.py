from django.db import models


class BankStatementsRes(models.Model):
    date = models.DateField(auto_now_add=False, blank=False, null=False)
    revenue = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True, default=None)
    write_off = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True, default=None)
    purpose_of_payment = models.CharField(max_length=500, blank=True, null=True, default=None)
    contractor = models.CharField(max_length=200, blank=True, null=True, default=None)
    doc_number = models.IntegerField(blank=False, null=False)
    transaction_type = models.CharField(max_length=100, blank=True, null=True, default=None)
    division = models.CharField(max_length=150, blank=True, null=True, default=None)
    article_revenue = models.CharField(max_length=250, blank=True, null=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return f'{self.article_revenue} - {self.date}'


class dds_report(models.Model):
    article_revenue = models.CharField(max_length=250, blank=True, null=True, default=None)
    division = models.CharField(max_length=150, blank=True, null=True, default=None)
    month = models.TextField()
    total_revenue = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True, default=None)
    total_write_off = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.article_revenue}-{self.division}-{self.total_revenue}-{self.total_write_off}'

    class Meta:
        managed = False  # Отключаем автогенерацию таблицы
        db_table = 'public.dds_report'
