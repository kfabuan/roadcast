# Generated by Django 3.2 on 2021-11-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0039_alter_tbl_add_members_day_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Day_off',
            field=models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True, verbose_name='Day Off (Mon(0) - Sun(6)'),
        ),
    ]
