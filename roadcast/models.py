from typing import ClassVar
from django.db import models 
from datetime import datetime
import os, random
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.utils import timezone
from django.utils.html import mark_safe
# from multiselectfield import MultiSelectField# Create your models here. This is the database structure

now = timezone.now()

def image_path_incident_report(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'incident_images/{year}-{month}-{imageid}={basename}-{randomstring}{ext}'.format(imageid = instance,basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime("%Y"), month=_now.strftime("%m"), day=_now.strftime("%d"))
#For PNP members
def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return '{year}-{month}-{basename}-{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime("%Y"), month=_now.strftime("%m"), day=_now.strftime("%d"))
    # return '{basename}-{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension)

#For general public
def image_path2(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'Public/{year}-{month}-{basename}-{randomstring}{ext}'.format(basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime("%Y"), month=_now.strftime("%m"), day=_now.strftime("%d"))

# Dane's codes
class Tbl_add_departments(models.Model):
    DEPARTMENTS = (
        ('Anti-Cybercrime Group', 'Anti-Cybercrime Group'),
        ('Anti-Kidnapping Group', 'Anti-Kidnapping Group'),
        ('Aviation Security Group', 'Aviation Security Group'),
        ('Civil Security Group', 'Civil Security Group'),
        ('Criminal Investigation and Detection Group', 'Criminal Investigation and Detection Group'),
        ('Drug Enforcement Group', 'Drug Enforcement Group'),
        ('Highway Patrol Group', 'Highway Patrol Group'),
        ('Integrity Monitoring and Enforcement Group', 'Integrity Monitoring and Enforcement Group'),
        ('Intelligence Group', 'Intelligence Group'),
        ('Maritime Group', 'Maritime Group'),
        ('Police Security and Protection Group', 'Police Security and Protection Group'),
        ('Special Action Force', 'Special Action Force')
    )
    Dept_Dept           =  models.CharField(max_length=200, verbose_name='Department', blank=True, choices=DEPARTMENTS)
    def __str__(self):
        return self.Dept_Dept 

class Tbl_substation(models.Model):
    SUBSTATION = (
        ('Pasig City Police Station', 'Pasig City Police Station'),
        ('Substation 1', 'Substation 1'),
        ('Substation 2', 'Substation 2'),
        ('Substation 3', 'Substation 3'),
        ('Substation 4', 'Substation 4'),
        ('Substation 5', 'Substation 5'),
        ('Substation 6', 'Substation 6'),
        ('Substation 7', 'Substation 7'),
        ('Substation 8', 'Substation 8')
    )
    Substation          = models.CharField(max_length=200, verbose_name='Substation', blank=True, choices=SUBSTATION)
    def __str__(self):
        return self.Substation

class Tbl_member_type(models.Model):
    MEMBERTYPE = (
        ('Admin', 'Admin'),
        ('Crime Statistician', 'Crime Statistician'),
        ('Sub-representative', 'Sub-representative'),
        ('Investigator', 'Investigator')
    )
    Member_Type         = models.CharField(max_length=200, verbose_name='MemberType', blank=True, choices=MEMBERTYPE)
    def __str__(self):
        return self.Member_Type 

class Tbl_position(models.Model):
    POSITION = (
        ('Police General (PGEN)', 'Police General (PGEN)'),
        ('Police Lieutenant General (PLTGEN)', 'Police Lieutenant General (PLTGEN)'),
        ('Police Major General (PMGEN)', 'Police Major General (PMGEN)'),
        ('Police Brigadier General (PBGEN)', 'Police Brigadier General (PBGEN)'),
        ('Police Colonel (PCOL)', 'Police Colonel (PCOL)'),
        ('Police Lieutenant Colonel (PLTCOL)', 'Police Lieutenant Colonel (PLTCOL)'),
        ('Police Major (PMAJ)', 'Police Major (PMAJ)'),
        ('Police Captain (PCPT)', 'Police Captain (PCPT)'),
        ('Police Lieutenant (PLT.)', 'Police Lieutenant (PLT.)'),
        ('Police Executive Master Sergeant (PEMS)', 'Police Executive Master Sergeant (PEMS)'),
        ('Police Chief Master Sergeant (PCMS)', 'Police Chief Master Sergeant (PCMS)'),
        ('Police Senior Master Sergeant (PSMS)', 'Police Senior Master Sergeant (PSMS)'),
        ('Police Master Sergeant (PMSg)', 'Police Master Sergeant (PMSg)'),
        ('Police Staff Sergeant (PSSg)', 'Police Staff Sergeant (PSSg)'),
        ('Police Corporal (PCpl)', 'Police Corporal (PCpl)'),
        ('Patrolman / Patrolwoman (Pat)', 'Patrolman / Patrolwoman (Pat)')
    )
    Position            = models.CharField(max_length=200, verbose_name='Position', blank=True, choices=POSITION)
    def __str__(self):
        return self.Position 

class Tbl_add_members(models.Model):
    #Foreign keys
    id                  = models.AutoField(primary_key=True)
    Members_Dept        = models.ForeignKey(Tbl_add_departments, null=True, on_delete=models.SET_NULL) 
    Members_User        = models.ForeignKey(Tbl_member_type, null=True, on_delete=models.SET_NULL) #Admin/ Crime/ Subrep / Investigator
    Members_Substation  = models.ForeignKey(Tbl_substation, null=True, on_delete=models.SET_NULL)
    Members_Position   = models.ForeignKey(Tbl_position, null=True, on_delete=models.SET_NULL) #Rank of police

    Members_District    = models.CharField(max_length=200, verbose_name='Members District', blank=True, null=True)
    Members_Fname       = models.CharField(max_length=200, verbose_name='First Name', blank=True, null=True)
    Members_Lname       = models.CharField(max_length=200, verbose_name='Last Name', blank=True, null=True)
    Members_Email       = models.EmailField(max_length=200, verbose_name='Email', blank=True, null=True)
    Members_Password    = models.CharField(max_length=200, verbose_name='Password', blank=True, null=True)
    Date_Added          = models.DateField(default=now, verbose_name='Date Added', blank=True, null=True) #binago hehe
    Added_By            = models.CharField(max_length=200, verbose_name='Added By', blank=True, null=True)
    Members_Pic         = models.ImageField(upload_to=image_path, default='Profile/default.jpg', blank=True, null=True)

    def image_tag(self):
            return mark_safe('<img src="/media/%s" width="50" height="50" />'%(self.Members_Pic))

    def __str__(self):
        return self.Members_Fname

class tbl_genpub_users(models.Model):
    gen_surname = models.CharField(max_length=50, blank=True, null=True)
    gen_fname = models.CharField(max_length=50, blank=True, null=True)
    gen_sex = models.CharField(max_length=50, blank=True,null=True)
    gen_bday = models.DateTimeField(max_length=50,blank=True,null=True)
    gen_region = models.CharField(max_length=50,blank=True, null=True)
    gen_province = models.CharField(max_length=50,blank=True, null=True)
    gen_city = models.CharField(max_length=50,blank=True, null=True)
    gen_barangay = models.CharField(max_length=50,blank=True, null=True)
    gen_contact_no = models.CharField(max_length=50,blank=True, null=True)
    gen_username = models.CharField(max_length=50,blank=True, null=True,)
    gen_pass = models.CharField(max_length=50, blank=True,null=True)
    # gen_cpass = models.CharField(max_length=50, blank=True,null=True)
    gen_valid_id = models.CharField(max_length=50,blank=True,null=True)
    gen_upload_id = models.ImageField(upload_to=image_path2, default='Public/default.jpg', blank=True, null=True)
    date_signed_up = models.DateTimeField(auto_now_add=True,blank=True, null=True)
 
    def image_tag(self):
            return mark_safe('<img src="media/%s" width="50" height="50" />'%(self.gen_upload_id))

    def __str__(self):
        return self.gen_surname

class tbl_audit(models.Model):
    Members_id = models.ForeignKey(Tbl_add_members, null=True, on_delete=models.SET_NULL) #foreign
    Genpub_id = models.ForeignKey(tbl_genpub_users, null=True, on_delete=models.SET_NULL) #foreign
    username =models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    date_logged_in = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    # date_logged_out = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.username


class Tbl_district(models.Model):
    DISTRICT = (
        ('District 1', 'District 1'),
        ('District 2', 'District 2'),
    )
    District = models.CharField(max_length=200, verbose_name='District', blank=True, choices=DISTRICT)
    def __str__(self):
        return self.District 
  

class Tbl_barangay(models.Model):
    Barangay    = models.CharField(max_length=200, verbose_name='Barangay', blank=True)
    District_id = models.ForeignKey(Tbl_district, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Barangay 



class Tbl_pasig_incidents(models.Model):
    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    OFFENSES = (
        ('Physical Injury', 'Physical Injury'),
        ('Self Accident', 'Self Accident'),
        ('Homicide', 'Homicide'),
        ('Damage to Property', 'Damage to Property'),
    )

    COLLISION_TYPES = (
        ('Angle Collision', 'Angle Collision'),
        ('Bumped From Behind', 'Bumped From Behind'),
        ('Clash', 'Clash'),
        ('Damage to Property', 'Damage to Property'),
        ('Head On', 'Head On'),
        ('Hit and Run', 'Hit and Run'),
        ('Hit Animals', 'Hit Animals'),
        ('Hit Object On Road', 'Hit Object On Road'),
        ('Hit Object Off Road', 'Hit Object Off Road'),
        ('Hit Parked Vehicle', 'Hit Parked Vehicle'),
        ('Hit Pedestrian', 'Hit Pedestrian'),
        ('Hit While Parked', 'Hit While Parked'),
        ('Multi Vehicle', 'Multi Vehicle'),
        ('Rear End', 'Rear End'),
        ('Self Accident', 'Self Accident'),
        ('Impact', 'Impact'),
        ('Sideswiped', 'Sideswiped'),
        ('Side Impact', 'Side Impact'),
        ('Right Angle', 'Right Angle'),
        ('Others', 'Others'),
    )

    LIGHT = (
        ('Daylight', 'Daylight'),
        ('Night', 'Night')
    )

    SURFACE_CONDITION = (
        ('Dry', 'Dry'),
        ('Wet', 'Wet'),
        ('Sand', 'Sand'),
    )

    SURFACE_TYPE = (
        ('Asphalt', 'Asphalt'),
        ('Concrete', 'Concrete'),
        ('Soil', 'Soil'),
    )

    CASE_STATUS = (
        ('Solved', 'Solved'),
        ('Unsolved', 'Unsolved'),
    )

    WEATHER = (
        ('Sun', 'Sun'),
        ('Fair', 'Fair'),
        ('Light Rain', 'Light Rain'),
        ('Rainy', 'Rainy'),
        ('Wind', 'Wind'),
    )

    ROAD_CHARACTER = (
        ('Straight Flat', 'Straight Flat'),
        ('Straight Incline', 'Straight Incline'),
        ('Curve', 'Curve'),
        ('Curve Incline', 'Curve Incline'),
        ('Upwards', 'Upwards'),
        ('Downwards', 'Downwards'),
    )
    
    PERSON_TYPE = (
        ('Driver', 'Driver'),
        ('Passenger', 'Passenger'),
        ('Pedestrian', 'Pedestrian')
    )

    SEVERITY = (
        ('Unharmed', 'Unharmed'),
        ('Harmed', 'Harmed'),
        ('Injured', 'Injured'),
        ('Self Accident', 'Self Accident'),
        ('Deceased', 'Deceased'),
        ('Not Interested to Report', 'Not Interested to Report'),
        ('Arrested', 'Arrested'),
        ('Escaped', 'Escaped'),
        ('Unidentified', 'Unidentified')
    )

    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    CIVIL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced')
    )

    VEHICLE_BODY_TYPE = (
        ('Armored Car', 'Armored Car'),
        ('Alto', 'Alto'),
        ('Bicycle', 'Bicycle'),
        ('Private Bus', 'Private Bus'),
        ('PUB - Public Utility Bus', 'PUB - Public Utility Bus'),
        ('Cab Chassis', 'Cab Chassis'),
        ('Coupe', 'Coupe'),
        ('Electric Bike', 'Electric Bike'),
        ('Jitney', 'Jitney'),
        ('Hatchback', 'Hatchback'),
        ('Motorcycle', 'Motorcycle'),
        ('MTC/MC', 'MTC/MC'),
        ('Object', 'Object'),
        ('Pedicab', 'Pedicab'),
        ('PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)', 'PUJ/PUB/PUV - (Public Utility Bus/Public Utility Jeep/Public Utility Vehicle)'),
        ('PUJ - Public Utility Jeep', 'PUJ - Public Utility Jeep'),
        ('PUV- Public Utility Vehicle', 'PUV- Public Utility Vehicle'),
        ('Sedan', 'Sedan'),
        ('S-CUV', 'S-CUV'),
        ('Shuttle', 'Shuttle'),
        ('SUV', 'SUV'),
        ('Tricycle', 'Tricycle'),
        ('Train', 'Train'),
        ('Truck', 'Truck'),
        ('Trailer', 'Trailer'),
        ('Unidentified', 'Unidentified'),
        ('Pick-Up', 'Pick-Up'),
        ('Minivan', 'Minivan'),
        ('Van', 'Van'),
        ('Wagon', 'Wagon'),
        ('Cart', 'Cart'),
        ('Modern Jeepney', 'Modern Jeepney'),
        ('Others', 'Others'),
    )


    City            = models.CharField(max_length=200, verbose_name='City', blank=True, null=True)
    UnitStation     = models.CharField(max_length=200, verbose_name='Unit/Station', blank=True, null=True)
    CrimeOffense    = models.CharField(max_length=200, verbose_name='Crime/Offense',blank=True, null=True, choices=OFFENSES)
    Week            = models.IntegerField(verbose_name='Week',blank=True,null=True)
    Date            = models.DateField(max_length=200, verbose_name='Date',blank=True, null=True)
    Time            = models.TimeField(verbose_name='Time', blank=True, null=True)
    Day             = models.CharField(max_length=200, verbose_name='Day', blank=True, null=True)
    Incident_Type   = models.CharField(max_length=200, verbose_name='Incident Type', blank=True, null=True, choices=COLLISION_TYPES)
    Number_of_Persons_Involved = models.IntegerField(verbose_name='# of Persons Involved',blank=True, null=True)
    Light           = models.CharField(max_length=200, verbose_name='Light', blank=True, null=True, choices=LIGHT)
    Weather         = models.CharField(max_length=200, verbose_name='Weather', blank=True, null=True, choices=WEATHER)
    Case_Status     = models.CharField(max_length=200, verbose_name='Case Status', blank=True, null=True, choices=CASE_STATUS)
    District        = models.ForeignKey(Tbl_district, null=True, on_delete=models.SET_NULL)
    Barangay_id     = models.ForeignKey(Tbl_barangay, null=True, on_delete=models.SET_NULL) #foreign
    Address         = models.CharField(max_length=200, verbose_name='Address', blank=True, null=True)
    Along           = models.CharField(max_length=200, verbose_name='Along', blank=True, null=True)
    Corner          = models.CharField(max_length=200, verbose_name='Corner', blank=True, null=True)
   
    Surface_Condition   = models.CharField(max_length=200, verbose_name='Surface Condition', blank=True, null=True, choices= SURFACE_CONDITION)
    Surface_Type        = models.CharField(max_length=200, verbose_name='Surface Type', blank=True, null=True, choices= SURFACE_TYPE)
    Road_Repair         = models.CharField(max_length=200, verbose_name='Road Repair', blank=True, null=True, choices=YES_NO)
    Hit_and_Run         = models.CharField(max_length=200, verbose_name='Hit and Run', blank=True, null=True, choices=YES_NO)
    Road_Character      = models.CharField(max_length=200, verbose_name='Road Character', blank=True, null=True, choices=ROAD_CHARACTER)
    
    Suspect_Type        = models.CharField(max_length=200, verbose_name='Suspect Type', blank=True, null=True, choices=PERSON_TYPE)
    Suspect_Fname        = models.CharField(max_length=200, verbose_name='Suspect First Name', blank=True, null=True)
    Suspect_Lname        = models.CharField(max_length=200, verbose_name='Suspect Last Name', blank=True, null=True)
    Suspect_Severity    = models.CharField(max_length=200, verbose_name='Suspect Severity', blank=True, null=True, choices=SEVERITY)
    Suspect_Age         = models.CharField(max_length=100, verbose_name='Suspect Age', blank=True, null=True)
    Suspect_Sex         = models.CharField(max_length=200, verbose_name='Suspect Sex', blank=True, null=True, choices=SEX)
    Suspect_Civil_Status = models.CharField(max_length=200, verbose_name='Suspect Civil_Status', blank=True, null=True, choices=CIVIL_STATUS)
    Suspect_Address      = models.CharField(max_length=200, verbose_name='Suspect Address', blank=True, null=True)
    Suspect_Vehicle             = models.CharField(max_length=200, verbose_name='Suspect Vehicle', blank=True, null=True)
    Suspect_Vehicle_Body_Type   = models.CharField(max_length=200, verbose_name='Suspect Vehicle_Body_Type', blank=True, null=True, choices=VEHICLE_BODY_TYPE)
    Suspect_Plate_No            = models.CharField(max_length=200, verbose_name='Suspect Plate_No', blank=True, null=True)
    Suspect_Reg_Owner           = models.CharField(max_length=200, verbose_name='Suspect Reg_Owner', blank=True, null=True)
    Suspect_Drl_No              = models.CharField(max_length=200, verbose_name='Suspect Drl_No', blank=True, null=True)
    Suspect_Drl_Exp             =  models.DateField(max_length=200, verbose_name='Suspect Drl Exp Date',blank=True, null=True)

    Victim_Type         = models.CharField(max_length=200, verbose_name='Victim Type', blank=True, null=True, choices=PERSON_TYPE)
    Victim_Fname        = models.CharField(max_length=200, verbose_name='Victim First Name', blank=True, null=True)
    Victim_Lname        = models.CharField(max_length=200, verbose_name='Victim Last Name', blank=True, null=True)    
    Victim_Severity     = models.CharField(max_length=200, verbose_name='Victim Severity', blank=True, null=True, choices=SEVERITY)
    Victim_Age          = models.CharField(max_length=100, verbose_name='Victim Age', blank=True, null=True)
    Victim_Sex          = models.CharField(max_length=200, verbose_name='Victim Sex', blank=True, null=True, choices=SEX)
    Victim_Civil_Status = models.CharField(max_length=200, verbose_name='Victim Civil_Status', blank=True, null=True, choices=CIVIL_STATUS)
    Victim_Address      = models.CharField(max_length=200, verbose_name='Victim Address', blank=True, null=True)
    Victim_Vehicle      = models.CharField(max_length=200, verbose_name='Victim Vehicle', blank=True, null=True)
    Victim_Vehicle_Body_Type   = models.CharField(max_length=200, verbose_name='Victim Vehicle_Body_Type', blank=True, null=True, choices=VEHICLE_BODY_TYPE)
    Victim_Plate_No            = models.CharField(max_length=200, verbose_name='Victim Plate_No', blank=True, null=True)
    Victim_Reg_Owner           = models.CharField(max_length=200, verbose_name='Victim Reg_Owner', blank=True, null=True)
    Victim_Drl_No              = models.CharField(max_length=200, verbose_name='Victim Drl_No', blank=True, null=True)
    Victim_Drl_Exp             =  models.DateField(max_length=200, verbose_name='Victim Drl Exp Date',blank=True, null=True)

    Narrative       = models.CharField(max_length=900, verbose_name='Narrative', blank=True, null=True)
    Investigator    = models.ForeignKey(Tbl_add_members, null=True, on_delete=models.SET_NULL) #foreign
    date_added      = models.DateField(default=now, verbose_name='Date Added', blank=True, null=True)
    added_by        = models.CharField(max_length=200, verbose_name='Added By', blank=True, null=True)
    archive         = models.CharField(max_length=200, verbose_name='Archive', blank=True, null=True, choices=YES_NO)


    def __str__(self):
        model = Tbl_barangay
        return '{}-{}-{}'.format(self.City, model.Barangay, self.Date)



class Tbl_public_report(models.Model):
    User_ID = models.CharField(max_length=200, verbose_name='User ID', blank=True)
    Reported_City        = models.CharField(max_length=200, verbose_name='City:', blank=True)
    Reported_Brgy        = models.ForeignKey(Tbl_barangay, null=True, on_delete=models.SET_NULL) #foreign
    Reported_District    = models.CharField(max_length=200, verbose_name='District', blank=True)
    Reported_Location    = models.CharField(max_length=200, verbose_name='Location', blank=True)
    Reported_Along       = models.CharField(max_length=200, verbose_name='Along', blank=True)
    Reported_Corner      = models.CharField(max_length=200, verbose_name='Corner', blank=True)
    Reported_Narrative   = models.CharField(max_length=800, verbose_name='Narrative', blank=True)
    Reported_Image_Proof = models.ImageField(upload_to=image_path_incident_report,verbose_name='Proof of Incident', blank=True)
    Reported_Date        = models.DateField(default=now, verbose_name='Date Reported', blank=True)
    Reported_Time        = models.TimeField(default=now, verbose_name='Time Reported', blank=True)

    Recipient               = models.CharField(max_length=200, verbose_name='Recipient', blank=True)
    Read_Status             = models.CharField(max_length=200, verbose_name='Read', blank=True)
    Report_Status           = models.CharField(max_length=200, verbose_name='Report Status', default="Unsolved", blank=True)
    Assigned_Investigator   = models.ForeignKey(Tbl_add_members, null=True, on_delete=models.SET_NULL) #foreign
    Substation              = models.ForeignKey(Tbl_substation, null=True, on_delete=models.SET_NULL, related_name='Substation_id') #foreign

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />'%(self.Reported_Image_Proof))

    def __str__(self):
        return '{}-{}-{}'.format(self.Reported_Date,self.Reported_Brgy,self.Reported_City)

#Admin Responses to General Public
class Tbl_public_report_response (models.Model):
    Response_id     = models.AutoField(primary_key=True)
    Report          = models.ForeignKey(Tbl_public_report,null=True, on_delete=models.SET_NULL, related_name='Report_id') #foreign
    Sender          = models.CharField(max_length=200, verbose_name ='Sender', blank=True)
    Receiver        = models.ForeignKey(Tbl_add_members, null=True, on_delete=models.SET_NULL, related_name='Receiver_id') #foreign
    Response        = models.CharField(max_length=200, verbose_name='Response', blank=True, null=True)
    Response_Date   = models.DateField(default=now, verbose_name='Response Date', blank=True, null=True)
    Response_Time   = models.TimeField(default=now, verbose_name='Response Time', blank=True, null=True)


    def __str__(self):
        return '{}-{}-{}'.format(self.Receiver,self.Response_id,self.Reported_City)

class Tbl_forecast(models.Model):
    Date = models.DateField(max_length=200, verbose_name='Dates', blank=True, primary_key=True)
    Incidents = models.PositiveIntegerField(verbose_name='Incidents', blank=True)
    Averages= models.FloatField(max_length=200, verbose_name='Averages', blank=True, null=True)

    def __str__(self):
            return self.Date 

            





