# Generated by Django 5.1.6 on 2025-02-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_coupon_custom_coupon_type_alter_coupon_coupon_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='bill_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_days',
            field=models.CharField(default='All Days', max_length=100),
        ),
    ]
