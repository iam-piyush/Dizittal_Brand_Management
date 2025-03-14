# Generated by Django 5.1.6 on 2025-02-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_coupon_buy_x_coupon_get_y'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discount_value',
            new_name='flat_discount',
        ),
        migrations.AddField(
            model_name='coupon',
            name='percentage_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
