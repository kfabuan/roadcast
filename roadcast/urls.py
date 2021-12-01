"""roadcast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

from.views import DashboardView, deletesession, notif_public_report_detail, user_profile


urlpatterns = [
  #  path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login/admin', views.admin_login, name='admin_login'),
    path('aboutus', views.about_us, name='about_us'),
    path('contactus', views.contact_us, name='contact_us'),
    path('contactno', views.contact_no, name='contact_no'),

    path('signup', views.sign_up, name='sign_up'),
    path('signup/validation', views.sign_up_validation, name='sign_up_validation'),
    path('update', views.duplicate_gen, name='duplicate_gen'), #sign up validation
    path('landing', views.logout, name='logout'),

    path('dashboard/', views.DashboardView, name='dashboard'),
    path('dashboard/data', views.get_data, name='data'),

    path('incidents/view', views.view_incidents, name='view_incidents'),
    path('incident/detail/<int:incident_id>/', views.encoder_view_incident_detail, name='incident_detail_view'),
    path('incident/detail/solved/<int:incident_id>/', views.view_solved_cases_detail, name='view_solved_cases_detail'),

    path('incident/public/<int:incident_id>/', views.public_view_incident_detail, name='pub_incident_detail_view'),
    path('incident/edit/<int:incident_id>', views.processEditIncident, name="process_edit_incident"),
    path('incident/create/<int:gen_pub_report_id>', views.create_incident_report, name="create_incident_report"),
    path('incident/create/<int:gen_pub_report_id>/process', views.processCreateIncidentReport, name="processCreateIncidentReport"),


    path('incidents/add', views.add_incident, name='add_incident'),
    path('incidents/processadd', views.processAddIncident, name='process_add_incident'),
    path('incidents/uploadcsv/import', views.processCSV, name="process_upload_csv"),
    path('incidents/uploadcsv', views.upload_csv, name="upload_csv"),

    path('incidents/view/archives', views.view_archive_incidents, name='view_archive_incidents'),
    path('incident/<int:incident_id>/archiving', views.archiving_solved_cases, name='archiving_solved_cases'),
    path('incident/<int:incident_id>/unarchiving', views.unarchiving_solved_cases, name='unarchiving_solved_cases'),
    path('incident/<int:incident_id>/delete', views.processDeleteIncident, name='processDeleteIncident'),

    path('submitreportpolicy', views.policy, name='policy'),
    path('report/submit', views.submit_report, name='submit_report'),
    path('report/submit/admin', views.submit_report_admin, name='submit_report_admin'),


    path('report/monthly', views.monthly_report, name='monthly_report'),
    path('report/monthly/data', views.get_monthly_data, name='monthly_data'),
    path('report/monthly/generate', views.get_monthly_generate, name='monthly_generate'),

    #admin/encoder notif & inbox
    path('notification', views.notification, name='notification'),
    path('notification/solved', views.notification_solved, name='notification_solved'), #filter 1
    path('notification/ongoing', views.notification_ongoing, name='notification_ongoing'), #filter 2
    path('notification/invalid', views.notification_invalid, name='notification_invalid'), #filter 3
    path('notification/unassigned', views.notification_unassigned, name='notification_unassigned'), #filter 4

    path('notification/replies/public', views.notif_replies_of_pub, name='notif_replies_of_pub'), #filter 4
    path('notification/replies/admin', views.notif_replies_of_admin, name='notif_replies_of_admin'), #filter 4

    path('notification/public/<int:gen_pub_report_id>', views.notif_public_report_detail , name='notif_public_report_detail'),
    path('notification/public/<int:report_id>/assign', views.processAssigning , name='process_assigning'),
    path('notification/public/<int:report_id>/reply', views.processAdmin_Reply , name='process_admin_reply'),
    path('notification/public/<int:report_id>/invalid', views.processMarkingInvalid , name='process_mark_invalid'),

    #public notif & inbox
    path('public/inbox', views.public_inbox, name='public_inbox'),
    path('public/inbox/<int:report_id>', views.public_inbox_detail, name='public_inbox_detail'),
    path('public/inbox/<int:report_id>/reply', views.processPublic_Reply , name='process_public_reply'),

    #sub-rep inbox
    path('substation/notification', views.sub_notification, name='sub_notification'),
    path('substation/notification/solved', views.sub_notification_solved, name='sub_notification_solved'),
    path('substation/notification/ongoing', views.sub_notification_ongoing, name='sub_notification_ongoing'),

    path('substation/notification/<int:report_id>', views.sub_notification_detail, name='sub_notification_detail'),

    #jew
    path('notification/verification/<int:signup_id>', views.notif_sign_up_validation, name='notif_sign_up_validation'),
    path('notification/verifed/<int:pk>', views.genpub_verified, name='genpub_verified'),
    path('notification/rejected/<int:pk>', views.genpub_rejected, name='genpub_rejected'),
    path('success', views.success, name='success'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    
    path('unsolvedcases/', views.unsolved_cases, name='unsolved_cases'),
    path('unsolvedcases/<int:incident_id>', views.archiving, name='archiving'),
    path('unsolvedcases/<int:incident_id>/unarchiving', views.unarchiving, name='unarchiving'),
    path('unsolvedcases/alert', views.notify_unsolved, name='notify_unsolved'), 

    # path('audit', views.admin_audit_trail, name='admin_audit_trail'),
    path('memberlist', views.admin_list_members, name='admin_list_members'),

    #Dane's
    path('members/add', views.add_members, name='add_members'),
    path('members/status', views.duplicate_members, name='duplicate_members'),
    path('members/view/<member_id>', views.view_members, name='view_members'),
    path('members/edit/<member_id>', views.edit_members, name='edit_members'),
    path('members/update/<member_id>', views.update_members, name='update_members'),
    path('members/delete/<member_id>', views.delete_member, name='delete_member'),
    path('members/archived', views.archived_members, name='archived_members'),    
    path('members/unarchive/<member_id>', views.unarchive_member, name='unarchive_member'),

    path('departments/add', views.add_dept, name='add_dept'),
    path('departments/status', views.duplicate, name='duplicate'),
    path('departmentlist', views.admin_list_departments, name='admin_list_departments'),
    path('departments/edit/<dept_id>', views.edit_dept, name='edit_dept'),
    path('departments/update/<dept_id>', views.update_dept, name='update_dept'),
    path('departments/delete/<dept_id>', views.delete_dept, name='delete_dept'),

    path('investigators/view/<member_id>', views.admin_view_investigators, name='admin_view_investigators'), #Binago lang yung name ng url hihi
    path('investigators', views.admin_investigators, name='admin_investigators'),

    #Audit Trail
    path('audit/genpub', views.admin_audit_genpub, name='admin_audit_genpub'),
    path('audit/members', views.admin_audit_members, name='admin_audit_members'),
    path('audit/members/view/<audit_id>', views.audit_members, name='audit_members'),
    path('audit/genpub/view/<audit_id>', views.audit_genpub, name='audit_genpub'),


    path('logout', views.deletesession, name='logout'),
    path('profile/user', views.user_profile, name="user_profile"),
    path('profile/edit/<prof_id>', views.edit_profile, name='edit_profile'), #edit profile for public
    path('profile/update/<prof_id>', views.update_profile, name='update_profile'), #save profile for public

    # path('public/notification', views.pub_notif_view, name='pub_notif_view'), #notification for public
    path('public/settings', views.pub_notif_inbox, name='pub_notif_inbox'), #settings
    path('public/settings/update/<prof_id>', views.change_account, name='change_account'), #save settings
    path('public/incident/detail/<str:incident_id>/', views.public_view_incident_detail, name='gen_incident_detail_view'),

    #alerts&notifs
    path('public/settings/account_activity_on', views.account_activity_on, name='account_activity_on'), 
    path('public/settings/account_activity_off', views.account_activity_off, name='account_activity_off'), 
    path('public/settings/new_incident_alert_on', views.new_incident_alert_on, name='new_incident_alert_on'), 
    path('public/settings/new_incident_alert_off', views.new_incident_alert_off, name='new_incident_alert_off'), 
    path('public/settings/custom_alert', views.custom_alert, name='custom_alert'), 


    path('error', views.error_page, name='error_page'), #error page for login required & permissions
    path('loginrequired', views.login_required, name='login_required'), #error page for login required

    path('forgot_pass', views.forgot_pass, name='forgot_pass'), #html ng forgot password
    path('validate', views.security_question, name='security_question'), #html for security question
    path('validating/<prof_id>', views.process_security, name='process_security'), #html for security question
    path('forgot_pass/reset/<prof_id>', views.genpub_reset_password, name='reset_pass'), #html ng forgot password
    path('forgot_pass/saving/<prof_id>', views.process_reset, name='process_reset'), #html ng forgot password
    path('termsofservice', views.terms, name='terms'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls),]
    
handler404 = "roadcast.views.no_page" #page not found
handler500 = 'roadcast.views.server_error' #server error