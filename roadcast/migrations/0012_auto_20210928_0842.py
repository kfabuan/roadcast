# Generated by Django 3.2.4 on 2021-09-28 00:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0011_auto_20210926_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 0, 42, 9, 919910, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 0, 42, 9, 919910, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 28, 0, 42, 9, 919910, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 28, 0, 42, 9, 919910, tzinfo=utc), verbose_name='Date Reported'),
        ),
    ]