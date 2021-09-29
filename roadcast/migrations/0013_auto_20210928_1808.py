# Generated by Django 3.2.4 on 2021-09-28 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0012_auto_20210928_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Latitude',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Longitude',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 10, 8, 33, 602456, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 10, 8, 33, 602456, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 10, 8, 33, 602456, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 28, 10, 8, 33, 602456, tzinfo=utc), verbose_name='Date Reported'),
        ),
    ]
