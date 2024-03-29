# Generated by Django 5.0.1 on 2024-01-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dds_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_revenue', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('division', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('month', models.TextField()),
                ('total_revenue', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=25, null=True)),
                ('total_write_off', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=25, null=True)),
            ],
            options={
                'db_table': 'public.dds_report',
                'managed': False,
            },
        ),
    ]
