# Generated by Django 3.2 on 2021-09-25 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import roadcast.models


class Migration(migrations.Migration):

    dependencies = [
        ('roadcast', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_pasig_incidents',
            old_name='Along_Avenue',
            new_name='Along',
        ),
        migrations.RenameField(
            model_name='tbl_pasig_incidents',
            old_name='Corner_Avenue',
            new_name='Corner',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Along_Boulevard',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Along_Highway',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Along_Road',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Along_Street',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Bound',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Corner_Boulevard',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Corner_Highway',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Corner_Road',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Corner_Street',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Others',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Road_Class',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Vehicle_Year_Model',
        ),
        migrations.RemoveField(
            model_name='tbl_pasig_incidents',
            name='Victim_Vehicle_Year_Model',
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Drl_Exp',
            field=models.DateField(blank=True, max_length=200, null=True, verbose_name='Suspect Drl Exp Date'),
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Type',
            field=models.CharField(blank=True, choices=[('Driver', 'Driver'), ('Passenger', 'Passenger'), ('Pedestrian', 'Pedestrian')], max_length=200, null=True, verbose_name='Suspect Type'),
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='Victim_Drl_Exp',
            field=models.DateField(blank=True, max_length=200, null=True, verbose_name='Victim Drl Exp Date'),
        ),
        migrations.AddField(
            model_name='tbl_pasig_incidents',
            name='archive',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True, verbose_name='Archive'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Date_Added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 8, 24, 34, 5182, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_add_members',
            name='Members_Pic',
            field=models.ImageField(blank=True, default='Profile/default.jpg', null=True, upload_to=roadcast.models.image_path),
        ),
        migrations.AlterField(
            model_name='tbl_genpub_users',
            name='gen_upload_id',
            field=models.ImageField(blank=True, default='Public/default.jpg', null=True, upload_to=roadcast.models.image_path2),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Case_Status',
            field=models.CharField(blank=True, choices=[('Solved', 'Solved'), ('Unsolved', 'Unsolved')], max_length=200, null=True, verbose_name='Case Status'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='CrimeOffense',
            field=models.CharField(blank=True, choices=[('Physical Injury', 'Physical Injury'), ('Self Accident', 'Self Accident'), ('Homicide', 'Homicide'), ('Damage to Property', 'Damage to Property')], max_length=200, null=True, verbose_name='Crime/Offense'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Hit_and_Run',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True, verbose_name='Hit and Run'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Incident_Type',
            field=models.CharField(blank=True, choices=[('Angle Collision', 'Angle Collision'), ('Bumped From Behind', 'Bumped From Behind'), ('Clash', 'Clash'), ('Damage to Property', 'Damage to Property'), ('Head On', 'Head On'), ('Hit and Run', 'Hit and Run'), ('Hit Animals', 'Hit Animals'), ('Hit Object On Road', 'Hit Object On Road'), ('Hit Object Off Road', 'Hit Object Off Road'), ('Hit Parked Vehicle', 'Hit Parked Vehicle'), ('Hit Pedestrian', 'Hit Pedestrian'), ('Hit While Parked', 'Hit While Parked'), ('Multi Vehicle', 'Multi Vehicle'), ('Rear End', 'Rear End'), ('Self Accident', 'Self Accident'), ('Impact', 'Impact'), ('Sideswiped', 'Sideswiped'), ('Side Impact', 'Side Impact'), ('Right Angle', 'Right Angle'), ('Others', 'Others')], max_length=200, null=True, verbose_name='Incident Type'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Light',
            field=models.CharField(blank=True, choices=[('Daylight', 'Daylight'), ('Night', 'Night')], max_length=200, null=True, verbose_name='Light'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Road_Repair',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True, verbose_name='Road Repair'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Surface_Condition',
            field=models.CharField(blank=True, choices=[('Dry', 'Dry'), ('Wet', 'Wet'), ('Sand', 'Sand')], max_length=200, null=True, verbose_name='Surface Condition'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Surface_Type',
            field=models.CharField(blank=True, choices=[('Asphalt', 'Asphalt'), ('Concrete', 'Concrete'), ('Soil', 'Soil')], max_length=200, null=True, verbose_name='Surface Type'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Civil_Status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced')], max_length=200, null=True, verbose_name='Suspect Civil_Status'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Severity',
            field=models.CharField(blank=True, choices=[('Unharmed', 'Unharmed'), ('Harmed', 'Harmed'), ('Injured', 'Injured'), ('Self Accident', 'Self Accident'), ('Deceased', 'Deceased'), ('Not Interested to Report', 'Not Interested to Report'), ('Arrested', 'Arrested'), ('Escaped', 'Escaped'), ('Unidentified', 'Unidentified')], max_length=200, null=True, verbose_name='Suspect Severity'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True, verbose_name='Suspect Sex'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Suspect_Vehicle_Body_Type',
            field=models.CharField(blank=True, choices=[('Armored Car', 'Armored Car'), ('Alto', 'Alto'), ('Bicycle', 'Bicycle'), ('Private Bus', 'Private Bus'), ('PUB - Public Utility Bus', 'PUB - Public Utility Bus'), ('Cab Chassis', 'Cab Chassis'), ('Coupe', 'Coupe'), ('Electric Bike', 'Electric Bike'), ('Jitney', 'Jitney'), ('Hatchback', 'Hatchback'), ('Motorcycle', 'Motorcycle'), ('MTC/MC', 'MTC/MC'), ('Object', 'Object'), ('Pedicab', 'Pedicab'), ('PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)', 'PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)'), ('PUJ - Public Utility Jeep', 'PUJ - Public Utility Jeep'), ('PUV- Public Utility Vehicle', 'PUV- Public Utility Vehicle'), ('Sedan', 'Sedan'), ('S-CUV', 'S-CUV'), ('Shuttle', 'Shuttle'), ('SUV', 'SUV'), ('Tricycle', 'Tricycle'), ('Train', 'Train'), ('Truck', 'Truck'), ('Trailer', 'Trailer'), ('Unidentified', 'Unidentified'), ('Pick-Up', 'Pick-Up'), ('Minivan', 'Minivan'), ('Van', 'Van'), ('Wagon', 'Wagon'), ('Cart', 'Cart'), ('Modern Jeepney', 'Modern Jeepney'), ('Others', 'Others')], max_length=200, null=True, verbose_name='Suspect Vehicle_Body_Type'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Victim_Civil_Status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced')], max_length=200, null=True, verbose_name='Victim Civil_Status'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Victim_Severity',
            field=models.CharField(blank=True, choices=[('Unharmed', 'Unharmed'), ('Harmed', 'Harmed'), ('Injured', 'Injured'), ('Self Accident', 'Self Accident'), ('Deceased', 'Deceased'), ('Not Interested to Report', 'Not Interested to Report'), ('Arrested', 'Arrested'), ('Escaped', 'Escaped'), ('Unidentified', 'Unidentified')], max_length=200, null=True, verbose_name='Victim Severity'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Victim_Sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True, verbose_name='Victim Sex'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Victim_Type',
            field=models.CharField(blank=True, choices=[('Driver', 'Driver'), ('Passenger', 'Passenger'), ('Pedestrian', 'Pedestrian')], max_length=200, null=True, verbose_name='Victim Type'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Victim_Vehicle_Body_Type',
            field=models.CharField(blank=True, choices=[('Armored Car', 'Armored Car'), ('Alto', 'Alto'), ('Bicycle', 'Bicycle'), ('Private Bus', 'Private Bus'), ('PUB - Public Utility Bus', 'PUB - Public Utility Bus'), ('Cab Chassis', 'Cab Chassis'), ('Coupe', 'Coupe'), ('Electric Bike', 'Electric Bike'), ('Jitney', 'Jitney'), ('Hatchback', 'Hatchback'), ('Motorcycle', 'Motorcycle'), ('MTC/MC', 'MTC/MC'), ('Object', 'Object'), ('Pedicab', 'Pedicab'), ('PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)', 'PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)'), ('PUJ - Public Utility Jeep', 'PUJ - Public Utility Jeep'), ('PUV- Public Utility Vehicle', 'PUV- Public Utility Vehicle'), ('Sedan', 'Sedan'), ('S-CUV', 'S-CUV'), ('Shuttle', 'Shuttle'), ('SUV', 'SUV'), ('Tricycle', 'Tricycle'), ('Train', 'Train'), ('Truck', 'Truck'), ('Trailer', 'Trailer'), ('Unidentified', 'Unidentified'), ('Pick-Up', 'Pick-Up'), ('Minivan', 'Minivan'), ('Van', 'Van'), ('Wagon', 'Wagon'), ('Cart', 'Cart'), ('Modern Jeepney', 'Modern Jeepney'), ('Others', 'Others')], max_length=200, null=True, verbose_name='Victim Vehicle_Body_Type'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='Weather',
            field=models.CharField(blank=True, choices=[('Sun', 'Sun'), ('Fair', 'Fair'), ('Light Rain', 'Light Rain'), ('Rainy', 'Rainy'), ('Wind', 'Wind')], max_length=200, null=True, verbose_name='Weather'),
        ),
        migrations.AlterField(
            model_name='tbl_pasig_incidents',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 8, 24, 34, 5182, tzinfo=utc), null=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 25, 8, 24, 34, 5182, tzinfo=utc), verbose_name='Date Reported'),
        ),
        migrations.AlterField(
            model_name='tbl_public_report',
            name='Reported_Time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 9, 25, 8, 24, 34, 5182, tzinfo=utc), verbose_name='Date Reported'),
        ),
    ]
