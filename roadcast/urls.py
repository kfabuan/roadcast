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


    path('signup1', views.sign_up1, name='signup1'),
    path('signup2', views.sign_up2, name='signup2'),
    path('signup3', views.sign_up3, name='signup3'),
    path('signup/validation', views.sign_up_validation, name='sign_up_validation'),


    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('dashboard/data', views.get_data, name='data'),


    path('incidents/view', views.view_incidents, name='view_incidents'),
    path('incidents/add', views.add_incident, name='add_incident'),
    path('incidents/processadd', views.processAddIncident, name='process_add_incident'),

    path('report/submit', views.submit_report, name='submit_report'),

    path('report', views.report_summary, name='report_summary'),
    path('report/monthly', Report_monthly.as_view(), name='report_monthly'),
    path('report/monthly/data', views.get_monthly_data, name='monthly_data'),

    path('notification', views.notification, name='notification'),
    path('substation/notification', views.sub_notification, name='sub_notification'),

    

    path('unsolvedcases', views.unsolved_cases, name='unsolved_cases'),

    path('logout', views.logout, name='logout'),
    path('settings/notification', views.notif_setting, name='public_notif_setting')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)