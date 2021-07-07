# Generated by Django 3.2 on 2021-07-07 05:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0002_alter_tbl_pasig_incidents_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Corner_Highway',
            field=models.CharField(blank=True, max_length=200, verbose_name='Corner Highway'),
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Day',
            field=models.CharField(blank=True, max_length=200, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Time',
            field=models.TimeField(blank=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 5, 41, 18, 480968, tzinfo=utc), verbose_name='Date Added'),
        ),
    ]
