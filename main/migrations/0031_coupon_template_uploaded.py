# Generated by Django 5.1.6 on 2025-02-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_coupon_template_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='template_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
