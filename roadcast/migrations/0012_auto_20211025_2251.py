# Generated by Django 3.2 on 2021-10-25 14:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0011_auto_20211025_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 25, 14, 51, 35, 668986, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 25, 14, 51, 35, 668986, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 25, 14, 51, 35, 668986, tzinfo=utc), verbose_name='Time Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Time',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='Response Time'),
        ),
    ]
