# Generated by Django 3.2 on 2021-10-23 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0005_auto_20211022_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_public_report',
            name='Report_Created',
            field=models.CharField(blank=True, default='No', max_length=200, verbose_name='Report Created'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 23, 14, 45, 17, 167949, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 23, 14, 45, 17, 167949, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 23, 14, 45, 17, 167949, tzinfo=utc), verbose_name='Time Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 23, 14, 45, 17, 167949, tzinfo=utc), null=True, verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 23, 14, 45, 17, 167949, tzinfo=utc), null=True, verbose_name='Response Time'),
        ),
    ]