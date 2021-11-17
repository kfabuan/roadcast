# Generated by Django 3.2 on 2021-11-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0020_tbl_public_report_read_by_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_substation',
            name='Substation',
            field=models.CharField(blank=True, choices=[('PNP-Pasig', 'PNP-Pasig'), ('Substation 1 - San Antonio', 'Substation 1 - San Antonio'), ('Substation 2 - Caniogan', 'Substation 2 - Caniogan'), ('Substation 3 - Malinao', 'Substation 3 - Malinao'), ('Substation 4 - San Joaquin', 'Substation 4 - San Joaquin'), ('Substation 5 - Pinagbuhatan', 'Substation 5 - Pinagbuhatan'), ('Substation 6 - San Miguel', 'Substation 6 - San Miguel'), ('Substation 7 - Santa Lucia', 'Substation 7 - Santa Lucia'), ('Substation 8 - Manggahan', 'Substation 8 - Manggahan')], max_length=200, verbose_name='Substation'),
        ),
    ]