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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

from.views import DashboardView, Report_monthly

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    
    path('login', views.login, name='login'),
    path('aboutus', views.about_us, name='about_us'),
    path('contactus', views.contact_us, name='contact_us'),
    path('contactno', views.contact_no, name='contact_no'),

    path('signup', views.sign_up, name='sign_up'),
    path('signup/validation', views.sign_up_validation, name='sign_up_validation'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dashboard/data', views.get_data, name='data'),

    path('incidents/view', views.view_incidents, name='view_incidents'),
    path('incidents/add', views.add_incident, name='add_incident'),
    path('incidents/processadd', views.processAddIncident, name='process_add_incident'),
    path('incidents/uploadcsv', views.processCSV, name="process_upload_csv"),

    path('incident/detail/<int:incident_id>/', views.encoder_view_incident_detail, name='incident_detail_view'),
    path('incident/edit/<int:incident_id>', views.processEditIncident, name="process_edit_incident"),


    path('report/submit', views.submit_report, name='submit_report'),
    path('report', views.report_summary, name='report_summary'),
    path('report/monthly', Report_monthly.as_view(), name='report_monthly'),
    path('report/monthly/data', views.get_monthly_data, name='monthly_data'),

    path('notification', views.notification, name='notification'),
    path('public/notification', views.public_notification, name='public_notification'),

    path('substation/notification', views.sub_notification, name='sub_notification'),
    
    path('unsolvedcases', views.unsolved_cases, name='unsolved_cases'),

    path('audit', views.admin_audit_trail, name='admin_audit_trail'),
    path('memberlist', views.admin_list_members, name='admin_list_members'),
    path('departments', views.admin_departments, name='admin_departments'),
    path('investigators', views.admin_investigators, name='admin_investigators'),
    path('investigator/view', views.admin_view_investigators, name='admin_view_investigators'),
    path('public/incident/detail/<int:incident_id>/', views.pub_incident_detail_view, name='gen_incident_detail_view'),

    # path('gen_report', views.gen_report, name='gen_report'),
    # path('rep_notif', views.rep_notif, name='rep_notif'),
    # path('<int:incident_id>/public_incident_detail/', views.public_incident_detail, name='public_incident_detail'),

    #path('<int:incident_id>/admin_incident_detail/', views.admin_incident_detail, name='admin_incident_detail'),

    
    path('logout', views.login, name='logout'),
    path('public/notification', views.pub_notif_inbox, name='pub_notif_inbox'),
    path('public/notification/view', views.pub_notif_inbox, name='pub_notif_view'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)