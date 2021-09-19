# Generated by Django 3.2 on 2021-09-19 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0007_auto_20210919_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_public_report',
            name='Reported_Date_and_Time',
        ),
        migrations.AddField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 10, 0, 56, 240060, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 19, 10, 0, 56, 240060, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 19, 10, 0, 56, 240060, tzinfo=utc), verbose_name='Date Reported'),
        ),
    ]
