from django.contrib import admin
from .models import Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report, Tbl_add_members, Tbl_substation, Tbl_add_departments, tbl_audit, tbl_genpub_users, Tbl_member_type, Tbl_position #Class in models.py
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
    list_display = ['image_tag','id','User_ID', 'Reported_City', 'Reported_Brgy','Report_Status', 'Reported_Date', 'Reported_Time', 'Assigned_Investigator']
   
class PasigUsers(admin.ModelAdmin):
    list_display = ['image_tag','Members_id','Members_Fname','Members_Lname','Members_Dept','Members_Position', 'Members_User','Members_Email','Members_Password','Members_Substation','Members_District',]

class PasigSubstation (admin.ModelAdmin):
    list_display = ['id', 'Substation']

class PasigBrgy(admin.ModelAdmin):
    list_display = ['id','Barangay', 'District_id']

class AddMembers(admin.ModelAdmin):
    list_display = ['id','Members_Dept', 'Members_Substation', 'Members_District', 'Members_User', 'Members_Position', 'Members_Fname', 'Members_Lname', 'Members_Email', 'Members_Username', 'Members_Password', 'Members_Pic', 'Date_Added', 'Added_By', 'Edit_By', 'Date_Edit', 'image_tag']

class AddDept(admin.ModelAdmin):
    list_display = ['id', 'Dept_Dept',]

class MemberType(admin.ModelAdmin):
    list_display = ['id', 'Member_Type']

class Position(admin.ModelAdmin):
    list_display = ['id', 'Position']

#Jewe's codes
# class genpub_users(admin.ModelAdmin):
#     list_display = ['gen_surname', 'gen_fname','gen_sex','gen_bday', 'gen_region','gen_province','gen_city', 'gen_barangay','gen_contact_no','gen_username','gen_pass','gen_valid_id', 'gen_upload_id','date_signed_up']

class audit(admin.ModelAdmin):
    list_display = ['Members_id','Genpub_id','username', 'password','date_logged_in']

class genpub_users(admin.ModelAdmin):
    list_display = ('id', 'Read_Status','is_verified','is_email_verified', 'gen_surname', 'gen_fname','gen_sex','gen_bday', 'gen_region','gen_province','gen_city', 'gen_barangay','gen_contact_no','gen_username','gen_pass','gen_valid_id', 'gen_upload_id', 'gen_profile','date_signed_up', 'date_edit', 'image_tag')

admin.site.register(Tbl_pasig_incidents, PasigIncidents) #2 parameters to lagi
admin.site.register(Tbl_district, PasigDistrict)
admin.site.register(Tbl_barangay, PasigBrgy)
admin.site.register(Tbl_public_report, PasigReportedIncidents)
# admin.site.register(Tbl_add_members, PasigUsers)
# admin.site.register(Tbl_substation, PasigSubstation)

#Dane
admin.site.register(Tbl_add_members, AddMembers)
admin.site.register(Tbl_add_departments, AddDept)
admin.site.register(Tbl_substation, PasigSubstation)
admin.site.register(Tbl_member_type, MemberType)
admin.site.register(Tbl_position, Position)

#Jew
admin.site.register(tbl_genpub_users, genpub_users)
# admin.site.register(tbl_audit, audit)


