# Generated by Django 3.2 on 2021-10-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0018_tbl_genpub_users_nf_brgy'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_add_members',
            name='nf_acc_activity',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='nf_brgy',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='nf_new_incident',
            field=models.BooleanField(default=True),
        ),
    ]
