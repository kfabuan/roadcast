# Generated by Django 3.2 on 2021-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0031_auto_20211127_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_add_members',
            name='Archived',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=200, null=True, verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Availability',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200, null=True, verbose_name='Availability'),
        ),
    ]
