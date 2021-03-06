# Generated by Django 3.2 on 2021-10-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0013_auto_20211025_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Assigned_Investigator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roadcast.tbl_add_members'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Brgy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roadcast.tbl_barangay'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Substation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Substation_id', to='roadcast.tbl_substation'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='User_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roadcast.tbl_genpub_users'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Report_id', to='roadcast.tbl_public_report'),
        ),
    ]
