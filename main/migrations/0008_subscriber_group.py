# Generated by Django 5.1.6 on 2025-02-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_campaign_newsletter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='group',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True),
        ),
    ]
