# Generated by Django 2.2.3 on 2019-07-28 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tracker.Event'),
            preserve_default=False,
        ),
    ]
