# Generated by Django 4.2.7 on 2024-06-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ribble', '0006_details_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='terms',
            field=models.BooleanField(),
        ),
    ]
