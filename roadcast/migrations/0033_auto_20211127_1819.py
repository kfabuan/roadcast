# Generated by Django 3.2 on 2021-11-27 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0032_auto_20211127_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_add_members',
            name='Archived',
        ),
        migrations.RemoveField(
            model_name='tbl_add_members',
            name='Availability',
        ),
        migrations.RemoveField(
            model_name='tbl_add_members',
            name='Day_off',
        ),
    ]