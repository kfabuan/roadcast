from django.contrib import admin
from .models import Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report, Tbl_add_members, Tbl_substation, Tbl_add_departments, tbl_audit, tbl_genpub_users, Tbl_member_type, Tbl_position #Class in models.py
from .models import refregion, refprovince, refcitymun
from .models import Tbl_public_report_response, Tbl_forecast
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

admin.site.site_header = "Roadcast Admin"
admin.site.site_title = "Roadcast Admin Area"
admin.site.index_title = "Welcome to the Roadcast Admin Area"

class Forecasting(admin.ModelAdmin):
    list_display = ['Date','Incidents', 'Averages']

class PasigIncidents(admin.ModelAdmin):
    list_display = ['City','UnitStation','Case_Status', 'CrimeOffense', 'Week', 'Date', 'Time', 'Day','Incident_Type', 'District', 'Barangay_id','Address','Latitude','Longitude','Suspect_Lname','Victim_Lname','Investigator','date_added','added_by','archive','read_status']

class PasigDistrict(admin.ModelAdmin):
    list_display = ['District',]

class PasigBrgy(admin.ModelAdmin):
    list_display = ['id','Barangay', 'District_id']

class PasigReportedIncidents(admin.ModelAdmin):
    list_display = ['image_tag','id','User_ID', 'Reported_City', 'Reported_Brgy','Report_Status', 'Reported_Date', 'Reported_Time', 'Assigned_Investigator']
   
class PasigReportResponses(admin.ModelAdmin):
    list_display = ['Response_id','Report','Sender_Type', 'Sender', 'Receiver','Response', 'Response_Date', 'Response_Time', 'Read_Status']
   
class PasigSubstation (admin.ModelAdmin):
    list_display = ['id', 'Substation']

class PasigBrgy(admin.ModelAdmin):
    list_display = ['id','Barangay', 'District_id']

class AddMembers(admin.ModelAdmin):
    list_display = ['image_tag', 'id','Members_Dept', 'Members_Substation', 'Members_District', 'Members_User', 'Members_Position', 'Members_Fname', 'Members_Lname', 'Members_Email', 'Members_Username', 'Members_Password', 'Members_Pic', 'Date_Added', 'Added_By', 'Edit_By', 'Date_Edit',]

class AddDept(admin.ModelAdmin):
    list_display = ['id', 'Dept_Dept',]

class MemberType(admin.ModelAdmin):
    list_display = ['id', 'Member_Type']

class Position(admin.ModelAdmin):
    list_display = ['id', 'Position']


class audit(admin.ModelAdmin):
    list_display = ['username','password','date_logged_in',]

class genpub_users(admin.ModelAdmin):
    list_display = ('image_tag', 'id', 'Read_Status','is_verified','is_email_verified', 'gen_surname', 'gen_fname','gen_sex','gen_bday', 'gen_city_id', 'gen_barangay','gen_contact_no','gen_username','gen_pass','gen_valid_id', 'gen_upload_id', 'gen_profile','date_signed_up', 'date_edit',)

class ref_region(admin.ModelAdmin):
    list_display = ('id', 'psgcCode','regDesc','regCode')

class ref_province(admin.ModelAdmin):
    list_display = ('id', 'psgcCode','provDesc','regCode','provCode')

class ref_citymun(admin.ModelAdmin):
    list_display = ('id', 'psgcCode','citymunDesc','regDesc','provCode','citymunCode')


admin.site.register(Tbl_pasig_incidents, PasigIncidents) #2 parameters to lagi
admin.site.register(Tbl_district, PasigDistrict)
admin.site.register(Tbl_barangay, PasigBrgy)
admin.site.register(Tbl_public_report, PasigReportedIncidents)
admin.site.register(Tbl_public_report_response, PasigReportResponses)
admin.site.register(Tbl_forecast, Forecasting)



#Dane
admin.site.register(Tbl_add_members, AddMembers)
admin.site.register(Tbl_add_departments, AddDept)
admin.site.register(Tbl_substation, PasigSubstation)
admin.site.register(Tbl_member_type, MemberType)
admin.site.register(Tbl_position, Position)

#Jew
admin.site.register(tbl_genpub_users, genpub_users)
admin.site.register(refregion, ref_region)
admin.site.register(refprovince, ref_province)
admin.site.register(refcitymun, ref_citymun)
admin.site.register(tbl_audit, audit)


