from django.db import models
from datetime import datetime
import os, random
from django.utils import timezone
from django.utils.html import mark_safe

# Create your models here. This is the database structure

now = timezone.now()

class Tbl_pasig_incidents(models.Model):
    City = models.CharField(max_length=200, verbose_name='City', blank=False)
    UnitStation= models.CharField(max_length=200, verbose_name='Unit/Station', blank=False)
    CrimeOffense = models.CharField(max_length=200, verbose_name='Crime/Offense',blank=False)
    Week = models.IntegerField(verbose_name='Week',blank=True)
    Date = models.DateField(max_length=200, verbose_name='Date',blank=True)
    Time = models.TimeField(verbose_name='Time', blank=True)
    Day = models.CharField(max_length=200, verbose_name='Time', blank=True)
    Incident_Type = models.CharField(max_length=200, verbose_name='Incident Type', blank=True)
    Number_of_Persons_Involved = models.IntegerField(max_length=200, verbose_name='# of Persons Involved',blank=True)
    Light = models.CharField(max_length=200, verbose_name='Light', blank=True)
    Weather = models.CharField(max_length=200, verbose_name='Weather', blank=True)
    Case_Status = models.CharField(max_length=200, verbose_name='Case Status', blank=True)
    District = models.CharField(max_length=200, verbose_name='District', blank=True)
    Barangay = models.CharField(max_length=200, verbose_name='Barangay', blank=True)
    Address = models.CharField(max_length=200, verbose_name='Address', blank=True)

    Along_Avenue = models.CharField(max_length=200, verbose_name='Along Avenue', blank=True)
    Corner_Avenue = models.CharField(max_length=200, verbose_name='Corner Avenue', blank=True)
    Along_Road = models.CharField(max_length=200, verbose_name='Along Road', blank=True)
    Corner_Road = models.CharField(max_length=200, verbose_name='Corner Road', blank=True)
    Along_Street = models.CharField(max_length=200, verbose_name='Along Street', blank=True)
    Corner_Street = models.CharField(max_length=200, verbose_name='Corner Street', blank=True)
    Bound = models.CharField(max_length=200, verbose_name='Bound', blank=True)
    Along_Highway = models.CharField(max_length=200, verbose_name='Along Highway', blank=True)
    Corner_Highway = models.CharField(max_length=200, verbose_name='Corner Highway', blank=True)
    Along_Boulevard = models.CharField(max_length=200, verbose_name='Along Boulevard', blank=True)
    Corner_Boulevard = models.CharField(max_length=200, verbose_name='Corner Boulevard', blank=True)
    Others = models.CharField(max_length=200, verbose_name='Others', blank=True)

    Surface_Condition = models.CharField(max_length=200, verbose_name='Surface Condition', blank=True)
    Surface_Type = models.CharField(max_length=200, verbose_name='Surface Type', blank=True)
    Road_Class = models.CharField(max_length=200, verbose_name='Road Class', blank=True)
    Road_Repair = models.CharField(max_length=200, verbose_name='Road Repair', blank=True)
    Hit_and_Run = models.CharField(max_length=200, verbose_name='Hit and Run', blank=True)
    Road_Character = models.CharField(max_length=200, verbose_name='Road Character', blank=True)
    
    Suspect_Name = models.CharField(max_length=200, verbose_name='Suspect Name', blank=True)
    Suspect_Severity = models.CharField(max_length=200, verbose_name='Suspect Severity', blank=True)
    Suspect_Age = models.IntegerField(verbose_name='Suspect Age', blank=True)
    Suspect_Sex = models.CharField(max_length=200, verbose_name='Suspect Sex', blank=True)
    Suspect_Civil_Status = models.CharField(max_length=200, verbose_name='Suspect Civil_Status', blank=True)
    Suspect_Address = models.CharField(max_length=200, verbose_name='Suspect Address', blank=True)
    Suspect_Vehicle = models.CharField(max_length=200, verbose_name='Suspect Vehicle', blank=True)
    Suspect_Vehicle_Body_Type = models.CharField(max_length=200, verbose_name='Suspect Vehicle_Body_Type', blank=True)
    Suspect_Plate_No = models.CharField(max_length=200, verbose_name='Suspect Plate_No', blank=True)
    Suspect_Reg_Owner = models.CharField(max_length=200, verbose_name='Suspect Reg_Owner', blank=True)
    Suspect_Drl_No = models.CharField(max_length=200, verbose_name='Suspect Drl_No', blank=True)
    Suspect_Vehicle_Year_Model = models.CharField(max_length=200, verbose_name='Suspect Vehicle_Year_Model', blank=True)   
    
    Victim_Type = models.CharField(max_length=200, verbose_name='Victim Type', blank=True)
    Victim_Name = models.CharField(max_length=200, verbose_name='Victim Name', blank=True)
    Victim_Severity = models.CharField(max_length=200, verbose_name='Victim Severity', blank=True)
    Victim_Age = models.IntegerField(verbose_name='Victim Age', blank=True)
    Victim_Sex = models.CharField(max_length=200, verbose_name='Victim Sex', blank=True)
    Victim_Civil_Status = models.CharField(max_length=200, verbose_name='Victim Civil_Status', blank=True)
    Victim_Address = models.CharField(max_length=200, verbose_name='Victim Address', blank=True)
    Victim_Vehicle = models.CharField(max_length=200, verbose_name='Victim Vehicle', blank=True)
    Victim_Vehicle_Body_Type = models.CharField(max_length=200, verbose_name='Victim Vehicle_Body_Type', blank=True)
    Victim_Plate_No = models.CharField(max_length=200, verbose_name='Victim Plate_No', blank=True)
    Victim_Reg_Owner = models.CharField(max_length=200, verbose_name='Victim Reg_Owner', blank=True)
    Victim_Drl_No = models.CharField(max_length=200, verbose_name='Victim Drl_No', blank=True)
    Victim_Vehicle_Year_Model = models.CharField(max_length=200, verbose_name='Victim Vehicle_Year_Model', blank=True)   
    
    Narrative = models.CharField(max_length=200, verbose_name='Narrative', blank=True)
    date_added = models.DateField(default=now, verbose_name='Date Added', blank=False)
    added_by = models.CharField(max_length=200, verbose_name='Added By', blank=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.City, self.Barangay, self.Date )

