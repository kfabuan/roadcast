# Generated by Django 3.2 on 2021-11-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0019_auto_20211026_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_public_report',
            name='Read_by_inv',
            field=models.CharField(blank=True, default='No', max_length=200, verbose_name='Read by Investigator'),
        ),
    ]
