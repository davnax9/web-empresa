# Generated by Django 2.2.1 on 2019-06-01 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 15, 24, 21, 280494, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
