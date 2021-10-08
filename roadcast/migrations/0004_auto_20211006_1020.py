# Generated by Django 3.2 on 2021-10-06 02:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0003_auto_20211006_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_public_report_response',
            name='Sender',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sender'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), verbose_name='Time Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), null=True, verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 6, 2, 20, 22, 58281, tzinfo=utc), null=True, verbose_name='Response Time'),
        ),
    ]