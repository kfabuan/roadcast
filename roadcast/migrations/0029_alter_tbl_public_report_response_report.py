# Generated by Django 3.2 on 2021-11-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0028_tbl_public_report_admin_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_public_report_response',
            name='Report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Report_id', to='roadcast.tbl_public_report'),
        ),
    ]
