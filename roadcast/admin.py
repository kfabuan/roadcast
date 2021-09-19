from django.contrib import admin
from .models import Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report #Class in models.py
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

admin.site.site_header = "Roadcast Admin"
admin.site.site_title = "Roadcast Admin Area"
admin.site.index_title = "Welcome to the Roadcast Admin Area"


class PasigIncidents(admin.ModelAdmin):
    list_display = ['City','UnitStation', 'CrimeOffense', 'Week', 'Date', 'Time', 'Day', 'District', 'Barangay_id','Address']
    # search_fields =['user_fname', 'user_lname', 'user_email', 'user_position']

class PasigDistrict(admin.ModelAdmin):
    list_display = ['District',]

class PasigBrgy(admin.ModelAdmin):
    list_display = ['id','Barangay', 'District_id']

class PasigReportedIncidents(admin.ModelAdmin):
    list_display = ['image_tag','id','User_ID', 'Reported_City', 'Reported_Brgy','Report_Status', 'Reported_Date', 'Reported_Time']
   
    
admin.site.register(Tbl_pasig_incidents, PasigIncidents) #2 parameters to lagi
admin.site.register(Tbl_district, PasigDistrict)
admin.site.register(Tbl_barangay, PasigBrgy)
admin.site.register(Tbl_public_report, PasigReportedIncidents)
