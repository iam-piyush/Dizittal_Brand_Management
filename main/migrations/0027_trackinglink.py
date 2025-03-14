# Generated by Django 5.1.6 on 2025-02-15 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_delete_generatedpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=12)),
                ('tracking_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clicked', models.BooleanField(default=False)),
                ('clicked_at', models.DateTimeField(blank=True, null=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coupon')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subscriber')),
            ],
        ),
    ]
