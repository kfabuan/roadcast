# Generated by Django 3.2 on 2021-09-27 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0012_auto_20210927_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 27, 14, 56, 36, 776663, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 27, 14, 56, 36, 776663, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 27, 14, 56, 36, 776663, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 27, 14, 56, 36, 776663, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.CreateModel(
            name='Tbl_public_report_response',
            fields=[
                ('Response_id', models.AutoField(primary_key=True, serialize=False)),
                ('Sender', models.CharField(blank=True, max_length=200, verbose_name='Sender')),
                ('Response', models.CharField(blank=True, max_length=200, verbose_name='Response')),
                ('Response_Date', models.DateField(blank=True, default=datetime.datetime(2021, 9, 27, 14, 56, 36, 776663, tzinfo=utc), null=True, verbose_name='Response_Date')),
                ('Receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Receiver_id', to='roadcast.tbl_add_members')),
                ('Report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Report_id', to='roadcast.tbl_public_report')),
            ],
        ),
    ]
