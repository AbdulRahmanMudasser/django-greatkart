# Generated by Django 5.1.4 on 2025-01-30 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_discount_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_amount',
            new_name='discounted_price',
        ),
    ]
