# Generated by Django 3.2 on 2021-07-07 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0004_alter_tbl_pasig_incidents_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 5, 43, 11, 15641, tzinfo=utc), verbose_name='Date Added'),
        ),
    ]