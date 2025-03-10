# Generated by Django 5.1.6 on 2025-02-24 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_newsletter_campaigns_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newsletters', to='main.campaign'),
        ),
    ]
