# Generated by Django 3.2 on 2021-09-26 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import roadcast.models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0010_auto_20210926_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 26, 9, 17, 48, 389647, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Members_Pic',
            field=models.ImageField(blank=True, default='Profile/default.jpg', null=True, upload_to=roadcast.models.image_path),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 26, 9, 17, 48, 389647, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 26, 9, 17, 48, 389647, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Image_Proof',
            field=models.ImageField(blank=True, upload_to=roadcast.models.image_path_incident_report, verbose_name='Proof of Incident'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 26, 9, 17, 48, 389647, tzinfo=utc), verbose_name='Date Reported'),
        ),
    ]