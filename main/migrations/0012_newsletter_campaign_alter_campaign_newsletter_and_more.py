# Generated by Django 5.1.6 on 2025-02-13 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_campaign_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newsletters', to='main.campaign'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='newsletter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newsletter_campaign', to='main.newsletter'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='newsletter_id',
            field=models.CharField(blank=True, editable=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='xml_template',
            field=models.FileField(blank=True, null=True, upload_to='xml_templates/%Y/%m/%d/'),
        ),
    ]
