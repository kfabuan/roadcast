# Generated by Django 3.2 on 2021-10-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0017_auto_20211026_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_genpub_users',
            name='nf_brgy',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
