# Generated by Django 5.1.4 on 2024-12-31 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_products_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]