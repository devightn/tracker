# Generated by Django 2.2.5 on 2019-09-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_attribute_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributetype',
            name='unit',
            field=models.CharField(max_length=12),
        ),
    ]
