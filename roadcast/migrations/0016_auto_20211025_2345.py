# Generated by Django 3.2 on 2021-10-25 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0015_auto_20211025_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Brgy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_barangay'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='User_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_genpub_users'),
        ),
    ]
