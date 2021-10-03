# Generated by Django 3.2 on 2021-10-03 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import roadcast.models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0022_auto_20211003_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_audit',
            name='Genpub_id',
        ),
        migrations.RemoveField(
            model_name='tbl_audit',
            name='Members_id',
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Date_Edit',
            field=models.DateField(blank=True, null=True, verbose_name='Date Added'),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Edit_By',
            field=models.CharField(blank=True, default='Have not been editted yet', max_length=200, null=True, verbose_name='Edit By'),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Members_Username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='Read_Status',
            field=models.CharField(blank=True, max_length=200, verbose_name='Read'),
        ),
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='date_edit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='gen_profile',
            field=models.ImageField(blank=True, default='Public/default.jpg', null=True, upload_to=roadcast.models.image_path2),
        ),
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tbl_add_departments',
            name='Dept_Dept',
            field=models.CharField(blank=True, max_length=200, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_position',
            name='Position',
            field=models.CharField(blank=True, choices=[('NUP', 'NUP'), ('Pat', 'Pat'), ('PCpl', 'PCpl'), ('PSSg', 'PSSg'), ('PMGSg', 'PMGSg'), ('PSMSg', 'PSMSg'), ('PCMSg', 'PCMSg'), ('PEMSg', 'PEMSg'), ('PLT', 'PLT'), ('PCAP', 'PCAP'), ('PMAJ', 'PMAJ'), ('PLTCOL', 'PLTCOL'), ('PCOL', 'PCOL'), ('PBGEN', 'PBGEN'), ('PMGEN', 'PMGEN'), ('PLTGEN', 'PLTGEN'), ('PGEN', 'PGEN')], max_length=200, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), verbose_name='Time Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), null=True, verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Response_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 10, 3, 7, 35, 24, 731371, tzinfo=utc), null=True, verbose_name='Response Time'),
        ),
    ]