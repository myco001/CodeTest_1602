# Generated by Django 3.0.3 on 2020-02-14 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publishedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
