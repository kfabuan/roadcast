from django.db import models 
from datetime import datetime
import os, random
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.utils.html import mark_safe

# Create your models here. This is the database structure

now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'incident_images/{year}-{month}-{imageid}={basename}-{randomstring}{ext}'.format(imageid = instance,basename=basefilename, randomstring=randomstr, ext=file_extension, year=_now.strftime("%Y"), month=_now.strftime("%m"), day=_now.strftime("%d"))


class Tbl_district(models.Model):
    DISTRICT = (
        ('District 1', 'District 1'),
        ('District 2', 'District 2'),
    )
    District = models.CharField(max_length=200, verbose_name='District', blank=True, choices=DISTRICT)
    def __str__(self):
        return self.District 
  

class Tbl_barangay(models.Model):
    Barangay = models.CharField(max_length=200, verbose_name='Barangay', blank=True)
    District_id = models.ForeignKey(Tbl_district, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Barangay 

class Tbl_pasig_incidents(models.Model):
    # DISTRICT = (
    #     ('District 1', (
    #         ('Santa Lucia', 'Sta. Lucia'),
    #         ('Ugong', 'Ugong'),
    #         )
    #     ),
    #     ('District 2', (
    #             ('Brgy 2', 'Brgy 2'),
    #             ('Lela', 'lela'),
    #         )
    #     ),
    # )
    City = models.CharField(max_length=200, verbose_name='City', blank=True, null=True)
    UnitStation= models.CharField(max_length=200, verbose_name='Unit/Station', blank=True, null=True)
    CrimeOffense = models.CharField(max_length=200, verbose_name='Crime/Offense',blank=True, null=True)
    Week = models.IntegerField(verbose_name='Week',blank=True,null=True)
    Date = models.DateField(max_length=200, verbose_name='Date',blank=True, null=True)
    Time = models.TimeField(verbose_name='Time', blank=True, null=True)
    Day = models.CharField(max_length=200, verbose_name='Day', blank=True, null=True)
    Incident_Type = models.CharField(max_length=200, verbose_name='Incident Type', blank=True, null=True)
    Number_of_Persons_Involved = models.IntegerField(verbose_name='# of Persons Involved',blank=True, null=True)
    Light = models.CharField(max_length=200, verbose_name='Light', blank=True, null=True)
    Weather = models.CharField(max_length=200, verbose_name='Weather', blank=True, null=True)
    Case_Status = models.CharField(max_length=200, verbose_name='Case Status', blank=True, null=True)
    District = models.ForeignKey(Tbl_district, null=True, on_delete=models.SET_NULL)
    Barangay_id = models.ForeignKey(Tbl_barangay, null=True, on_delete=models.SET_NULL) #foreign
    Address = models.CharField(max_length=200, verbose_name='Address', blank=True, null=True)

    Along_Avenue = models.CharField(max_length=200, verbose_name='Along Avenue', blank=True, null=True)
    Corner_Avenue = models.CharField(max_length=200, verbose_name='Corner Avenue', blank=True, null=True)
    Along_Road = models.CharField(max_length=200, verbose_name='Along Road', blank=True, null=True)
    Corner_Road = models.CharField(max_length=200, verbose_name='Corner Road', blank=True, null=True)
    Along_Street = models.CharField(max_length=200, verbose_name='Along Street', blank=True, null=True)
    Corner_Street = models.CharField(max_length=200, verbose_name='Corner Street', blank=True, null=True)
    Bound = models.CharField(max_length=200, verbose_name='Bound', blank=True, null=True)
    Along_Highway = models.CharField(max_length=200, verbose_name='Along Highway', blank=True, null=True)
    Corner_Highway = models.CharField(max_length=200, verbose_name='Corner Highway', blank=True, null=True)
    Along_Boulevard = models.CharField(max_length=200, verbose_name='Along Boulevard', blank=True, null=True)
    Corner_Boulevard = models.CharField(max_length=200, verbose_name='Corner Boulevard', blank=True, null=True)
    Others = models.CharField(max_length=200, verbose_name='Others', blank=True, null=True)

    Surface_Condition = models.CharField(max_length=200, verbose_name='Surface Condition', blank=True, null=True)
    Surface_Type = models.CharField(max_length=200, verbose_name='Surface Type', blank=True, null=True)
    Road_Class = models.CharField(max_length=200, verbose_name='Road Class', blank=True, null=True)
    Road_Repair = models.CharField(max_length=200, verbose_name='Road Repair', blank=True, null=True)
    Hit_and_Run = models.CharField(max_length=200, verbose_name='Hit and Run', blank=True, null=True)
    Road_Character = models.CharField(max_length=200, verbose_name='Road Character', blank=True, null=True)
    
    Suspect_Name = models.CharField(max_length=200, verbose_name='Suspect Name', blank=True, null=True)
    Suspect_Severity = models.CharField(max_length=200, verbose_name='Suspect Severity', blank=True, null=True)
    Suspect_Age = models.CharField(max_length=100, verbose_name='Suspect Age', blank=True, null=True)
    Suspect_Sex = models.CharField(max_length=200, verbose_name='Suspect Sex', blank=True, null=True)
    Suspect_Civil_Status = models.CharField(max_length=200, verbose_name='Suspect Civil_Status', blank=True, null=True)
    Suspect_Address = models.CharField(max_length=200, verbose_name='Suspect Address', blank=True, null=True)
    Suspect_Vehicle = models.CharField(max_length=200, verbose_name='Suspect Vehicle', blank=True, null=True)
    Suspect_Vehicle_Body_Type = models.CharField(max_length=200, verbose_name='Suspect Vehicle_Body_Type', blank=True, null=True)
    Suspect_Plate_No = models.CharField(max_length=200, verbose_name='Suspect Plate_No', blank=True, null=True)
    Suspect_Reg_Owner = models.CharField(max_length=200, verbose_name='Suspect Reg_Owner', blank=True, null=True)
    Suspect_Drl_No = models.CharField(max_length=200, verbose_name='Suspect Drl_No', blank=True, null=True)
    Suspect_Vehicle_Year_Model = models.CharField(max_length=200, verbose_name='Suspect Vehicle_Year_Model', blank=True, null=True)   
    
    Victim_Type = models.CharField(max_length=200, verbose_name='Victim Type', blank=True, null=True)
    Victim_Name = models.CharField(max_length=200, verbose_name='Victim Name', blank=True, null=True)
    Victim_Severity = models.CharField(max_length=200, verbose_name='Victim Severity', blank=True, null=True)
    Victim_Age = models.CharField(max_length=100, verbose_name='Victim Age', blank=True, null=True)
    Victim_Sex = models.CharField(max_length=200, verbose_name='Victim Sex', blank=True, null=True)
    Victim_Civil_Status = models.CharField(max_length=200, verbose_name='Victim Civil_Status', blank=True, null=True)
    Victim_Address = models.CharField(max_length=200, verbose_name='Victim Address', blank=True, null=True)
    Victim_Vehicle = models.CharField(max_length=200, verbose_name='Victim Vehicle', blank=True, null=True)
    Victim_Vehicle_Body_Type = models.CharField(max_length=200, verbose_name='Victim Vehicle_Body_Type', blank=True, null=True)
    Victim_Plate_No = models.CharField(max_length=200, verbose_name='Victim Plate_No', blank=True, null=True)
    Victim_Reg_Owner = models.CharField(max_length=200, verbose_name='Victim Reg_Owner', blank=True, null=True)
    Victim_Drl_No = models.CharField(max_length=200, verbose_name='Victim Drl_No', blank=True, null=True)
    Victim_Vehicle_Year_Model = models.CharField(max_length=200, verbose_name='Victim Vehicle_Year_Model', blank=True, null=True)   
    
    Narrative = models.CharField(max_length=200, verbose_name='Narrative', blank=True, null=True)
    date_added = models.DateField(default=now, verbose_name='Date Added', blank=True, null=True)
    added_by = models.CharField(max_length=200, verbose_name='Added By', blank=True, null=True)

    def __str__(self):
        model = Tbl_barangay
        return '{}-{}-{}'.format(self.City, model.Barangay, self.Date)

class Tbl_public_report(models.Model):
    User_ID = models.CharField(max_length=200, verbose_name='User ID', blank=True)
    Reported_City = models.CharField(max_length=200, verbose_name='City:', blank=True)
    Reported_Brgy =  models.ForeignKey(Tbl_barangay, null=True, on_delete=models.SET_NULL) #foreign
    Reported_District = models.CharField(max_length=200, verbose_name='District', blank=True)
    Reported_Location = models.CharField(max_length=200, verbose_name='Location', blank=True)
    Reported_Along = models.CharField(max_length=200, verbose_name='Along', blank=True)
    Reported_Corner = models.CharField(max_length=200, verbose_name='Corner', blank=True)
    Reported_Narrative = models.CharField(max_length=800, verbose_name='Narrative', blank=True)
    Reported_Image_Proof = models.ImageField(upload_to=image_path,verbose_name='Proof of Incident', blank=True)
    Reported_Date = models.DateField(default=now, verbose_name='Date Reported', blank=True)
    Reported_Time = models.TimeField(default=now, verbose_name='Date Reported', blank=True)

    Recipient = models.CharField(max_length=200, verbose_name='Recipient', blank=True)
    Read_Status = models.CharField(max_length=200, verbose_name='Read', blank=True)
    Report_Status = models.CharField(max_length=200, verbose_name='Report Status', blank=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />'%(self.Reported_Image_Proof))

    def __str__(self):
        return '{}-{}-{}'.format(self.Reported_Date,self.Reported_Brgy,self.Reported_City)






