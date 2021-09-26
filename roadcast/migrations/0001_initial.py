# Generated by Django 3.2 on 2021-09-24 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import roadcast.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_add_departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_Dept', models.CharField(blank=True, choices=[('Anti-Cybercrime Group', 'Anti-Cybercrime Group'), ('Anti-Kidnapping Group', 'Anti-Kidnapping Group'), ('Aviation Security Group', 'Aviation Security Group'), ('Civil Security Group', 'Civil Security Group'), ('Criminal Investigation and Detection Group', 'Criminal Investigation and Detection Group'), ('Drug Enforcement Group', 'Drug Enforcement Group'), ('Highway Patrol Group', 'Highway Patrol Group'), ('Integrity Monitoring and Enforcement Group', 'Integrity Monitoring and Enforcement Group'), ('Intelligence Group', 'Intelligence Group'), ('Maritime Group', 'Maritime Group'), ('Police Security and Protection Group', 'Police Security and Protection Group'), ('Special Action Force', 'Special Action Force')], max_length=200, verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_add_members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Members_District', models.CharField(blank=True, max_length=200, null=True, verbose_name='Members District')),
                ('Members_Fname', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('Members_Lname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('Members_Email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('Members_Password', models.CharField(blank=True, max_length=200, null=True, verbose_name='Password')),
                ('Date_Added', models.DateField(blank=True, default=datetime.datetime(2021, 9, 24, 16, 34, 43, 99637, tzinfo=utc), null=True, verbose_name='Date Added')),
                ('Added_By', models.CharField(blank=True, max_length=200, null=True, verbose_name='Added By')),
                ('Members_Pic', models.ImageField(blank=True, default='profile/default.jpg', null=True, upload_to=roadcast.models.image_path)),
                ('Members_Dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_add_departments')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_barangay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Barangay', models.CharField(blank=True, max_length=200, verbose_name='Barangay')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(blank=True, choices=[('District 1', 'District 1'), ('District 2', 'District 2')], max_length=200, verbose_name='District')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_genpub_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_surname', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_fname', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_sex', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_bday', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('gen_region', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_province', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_city', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_barangay', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_contact_no', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_username', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_pass', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_valid_id', models.CharField(blank=True, max_length=50, null=True)),
                ('gen_upload_id', models.ImageField(blank=True, default='public/default.jpg', null=True, upload_to=roadcast.models.image_path2)),
                ('date_signed_up', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_member_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_Type', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Crime Statistician', 'Crime Statistician'), ('Sub-representative', 'Sub-representative'), ('Investigator', 'Investigator')], max_length=200, verbose_name='MemberType')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(blank=True, choices=[('Police General (PGEN)', 'Police General (PGEN)'), ('Police Lieutenant General (PLTGEN)', 'Police Lieutenant General (PLTGEN)'), ('Police Major General (PMGEN)', 'Police Major General (PMGEN)'), ('Police Brigadier General (PBGEN)', 'Police Brigadier General (PBGEN)'), ('Police Colonel (PCOL)', 'Police Colonel (PCOL)'), ('Police Lieutenant Colonel (PLTCOL)', 'Police Lieutenant Colonel (PLTCOL)'), ('Police Major (PMAJ)', 'Police Major (PMAJ)'), ('Police Captain (PCPT)', 'Police Captain (PCPT)'), ('Police Lieutenant (PLT.)', 'Police Lieutenant (PLT.)'), ('Police Executive Master Sergeant (PEMS)', 'Police Executive Master Sergeant (PEMS)'), ('Police Chief Master Sergeant (PCMS)', 'Police Chief Master Sergeant (PCMS)'), ('Police Senior Master Sergeant (PSMS)', 'Police Senior Master Sergeant (PSMS)'), ('Police Master Sergeant (PMSg)', 'Police Master Sergeant (PMSg)'), ('Police Staff Sergeant (PSSg)', 'Police Staff Sergeant (PSSg)'), ('Police Corporal (PCpl)', 'Police Corporal (PCpl)'), ('Patrolman / Patrolwoman (Pat)', 'Patrolman / Patrolwoman (Pat)')], max_length=200, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_substation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Substation', models.CharField(blank=True, choices=[('Substation 1', 'Substation 1'), ('Substation 2', 'Substation 2'), ('Substation 3', 'Substation 3'), ('Substation 4', 'Substation 4'), ('Substation 5', 'Substation 5'), ('Substation 6', 'Substation 6'), ('Substation 7', 'Substation 7'), ('Substation 8', 'Substation 8')], max_length=200, verbose_name='Substation')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_public_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.CharField(blank=True, max_length=200, verbose_name='User ID')),
                ('Reported_City', models.CharField(blank=True, max_length=200, verbose_name='City:')),
                ('Reported_District', models.CharField(blank=True, max_length=200, verbose_name='District')),
                ('Reported_Location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('Reported_Along', models.CharField(blank=True, max_length=200, verbose_name='Along')),
                ('Reported_Corner', models.CharField(blank=True, max_length=200, verbose_name='Corner')),
                ('Reported_Narrative', models.CharField(blank=True, max_length=800, verbose_name='Narrative')),
                ('Reported_Image_Proof', models.ImageField(blank=True, upload_to=roadcast.models.image_path, verbose_name='Proof of Incident')),
                ('Reported_Date', models.DateField(blank=True, default=datetime.datetime(2021, 9, 24, 16, 34, 43, 99637, tzinfo=utc), verbose_name='Date Reported')),
                ('Reported_Time', models.TimeField(blank=True, default=datetime.datetime(2021, 9, 24, 16, 34, 43, 99637, tzinfo=utc), verbose_name='Date Reported')),
                ('Recipient', models.CharField(blank=True, max_length=200, verbose_name='Recipient')),
                ('Read_Status', models.CharField(blank=True, max_length=200, verbose_name='Read')),
                ('Report_Status', models.CharField(blank=True, default='Unsolved', max_length=200, verbose_name='Report Status')),
                ('Assigned_Investigator', models.CharField(blank=True, max_length=200, verbose_name='Investigator')),
                ('Reported_Brgy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_barangay')),
                ('Substation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Substation_id', to='roadcast.tbl_substation')),
            ],
        ),
        migrations.CreateModel(
            name='Tbl_pasig_incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(blank=True, max_length=200, null=True, verbose_name='City')),
                ('UnitStation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Unit/Station')),
                ('CrimeOffense', models.CharField(blank=True, max_length=200, null=True, verbose_name='Crime/Offense')),
                ('Week', models.IntegerField(blank=True, null=True, verbose_name='Week')),
                ('Date', models.DateField(blank=True, max_length=200, null=True, verbose_name='Date')),
                ('Time', models.TimeField(blank=True, null=True, verbose_name='Time')),
                ('Day', models.CharField(blank=True, max_length=200, null=True, verbose_name='Day')),
                ('Incident_Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Incident Type')),
                ('Number_of_Persons_Involved', models.IntegerField(blank=True, null=True, verbose_name='# of Persons Involved')),
                ('Light', models.CharField(blank=True, max_length=200, null=True, verbose_name='Light')),
                ('Weather', models.CharField(blank=True, max_length=200, null=True, verbose_name='Weather')),
                ('Case_Status', models.CharField(blank=True, max_length=200, null=True, verbose_name='Case Status')),
                ('Address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('Along_Avenue', models.CharField(blank=True, max_length=200, null=True, verbose_name='Along Avenue')),
                ('Corner_Avenue', models.CharField(blank=True, max_length=200, null=True, verbose_name='Corner Avenue')),
                ('Along_Road', models.CharField(blank=True, max_length=200, null=True, verbose_name='Along Road')),
                ('Corner_Road', models.CharField(blank=True, max_length=200, null=True, verbose_name='Corner Road')),
                ('Along_Street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Along Street')),
                ('Corner_Street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Corner Street')),
                ('Bound', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bound')),
                ('Along_Highway', models.CharField(blank=True, max_length=200, null=True, verbose_name='Along Highway')),
                ('Corner_Highway', models.CharField(blank=True, max_length=200, null=True, verbose_name='Corner Highway')),
                ('Along_Boulevard', models.CharField(blank=True, max_length=200, null=True, verbose_name='Along Boulevard')),
                ('Corner_Boulevard', models.CharField(blank=True, max_length=200, null=True, verbose_name='Corner Boulevard')),
                ('Others', models.CharField(blank=True, max_length=200, null=True, verbose_name='Others')),
                ('Surface_Condition', models.CharField(blank=True, max_length=200, null=True, verbose_name='Surface Condition')),
                ('Surface_Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Surface Type')),
                ('Road_Class', models.CharField(blank=True, max_length=200, null=True, verbose_name='Road Class')),
                ('Road_Repair', models.CharField(blank=True, max_length=200, null=True, verbose_name='Road Repair')),
                ('Hit_and_Run', models.CharField(blank=True, max_length=200, null=True, verbose_name='Hit and Run')),
                ('Road_Character', models.CharField(blank=True, max_length=200, null=True, verbose_name='Road Character')),
                ('Suspect_Name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Name')),
                ('Suspect_Severity', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Severity')),
                ('Suspect_Age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Suspect Age')),
                ('Suspect_Sex', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Sex')),
                ('Suspect_Civil_Status', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Civil_Status')),
                ('Suspect_Address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Address')),
                ('Suspect_Vehicle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Vehicle')),
                ('Suspect_Vehicle_Body_Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Vehicle_Body_Type')),
                ('Suspect_Plate_No', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Plate_No')),
                ('Suspect_Reg_Owner', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Reg_Owner')),
                ('Suspect_Drl_No', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Drl_No')),
                ('Suspect_Vehicle_Year_Model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Suspect Vehicle_Year_Model')),
                ('Victim_Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Type')),
                ('Victim_Name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Name')),
                ('Victim_Severity', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Severity')),
                ('Victim_Age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Victim Age')),
                ('Victim_Sex', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Sex')),
                ('Victim_Civil_Status', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Civil_Status')),
                ('Victim_Address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Address')),
                ('Victim_Vehicle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Vehicle')),
                ('Victim_Vehicle_Body_Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Vehicle_Body_Type')),
                ('Victim_Plate_No', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Plate_No')),
                ('Victim_Reg_Owner', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Reg_Owner')),
                ('Victim_Drl_No', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Drl_No')),
                ('Victim_Vehicle_Year_Model', models.CharField(blank=True, max_length=200, null=True, verbose_name='Victim Vehicle_Year_Model')),
                ('Narrative', models.CharField(blank=True, max_length=200, null=True, verbose_name='Narrative')),
                ('date_added', models.DateField(blank=True, default=datetime.datetime(2021, 9, 24, 16, 34, 43, 99637, tzinfo=utc), null=True, verbose_name='Date Added')),
                ('added_by', models.CharField(blank=True, max_length=200, null=True, verbose_name='Added By')),
                ('Barangay_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_barangay')),
                ('District', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_district')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_barangay',
            name='District_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_district'),
        ),
        migrations.CreateModel(
            name='tbl_audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('date_logged_in', models.DateTimeField(auto_now_add=True, null=True)),
                ('Genpub_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_genpub_users')),
                ('Members_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_add_members')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Members_Position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_position'),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Members_Substation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_substation'),
        ),
        migrations.AddField(
            model_name='tbl_add_members',
            name='Members_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadcast.tbl_member_type'),
        ),
    ]
