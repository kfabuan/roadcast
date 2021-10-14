import json
import urllib
from django.core.checks.messages import INFO
from django.shortcuts import render, get_object_or_404, reverse #get_object_or_404 & reverse for processEdit
from .models import Tbl_add_members, Tbl_member_type, Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report, Tbl_substation, tbl_audit, tbl_genpub_users, Tbl_forecast, Tbl_public_report_response, Tbl_add_departments, Tbl_position
from requests.api import request
# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.views.generic import View #for charts
from django.http import JsonResponse
from django.db.models import Q
from collections import Counter
from itertools import chain
from django.db import connection
from django.core.cache import cache
# from PIL import Image
from django.contrib import messages #for csv upload
import csv, io
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, timedelta, date
# from django.utils import timezone, simplejson

from django.db.models import Avg
import datetime
from urllib.parse import urlencode
import requests
from django.core.paginator import Paginator 
from django.http.response import HttpResponse

from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token , send_html_mail
from django.core.mail import EmailMessage
from django.core.mail import send_mail

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Get date today
today = date.today()

#Sessions
authorized = Tbl_add_members.objects.all()
pub            = tbl_genpub_users.objects.all()

#notifications count
unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

def index(request): #landing/home
    return render (request, 'landing.html')

#Jew
def login(request):
    if request.method == 'POST':
        # try:
        username = request.POST['username']
        password = request.POST['password']
        a = False
        b = False
        
        try:
            members = Tbl_add_members.objects.get(Members_Email = username)
            a = True
        except:
            a = False
            print('none')
        try:
            public = tbl_genpub_users.objects.get(gen_username = username)
            b= True
        except:
            b = False
            print('none')
        
        if a:
            if (members.Members_Email == username) and (members.Members_Password == password):

                submit = tbl_audit( username = username, password = password)
                submit.save()

                authorized_session = Tbl_add_members.objects.get(Members_Email=username, Members_Password = password)

                request.session['authorized_id'] = authorized_session.id

                return HttpResponseRedirect(reverse('dashboard')) 
            else: 
                messages.success(request, ("Oops! Please check your email or password."))
                return render(request, 'login.html')
        if b:
            if (public.gen_username == username) and (public.gen_pass == password):
                if public.is_email_verified:    
                    if public.is_verified:
                        submit = tbl_audit(username = username, password = password)
                        submit.save()

                        public_session = tbl_genpub_users.objects.get(gen_username=username, gen_pass= password)
                        request.session['public_id'] = public_session.id
                        return HttpResponseRedirect(reverse('dashboard'))
                    
                    elif not public.is_verified:
                        messages.success(request, ("Oops! Please wait for the admin to approve your account."))
                        return render(request, 'login.html')
                elif not public.is_email_verified:
                        messages.success(request, ("Oops! Please check your email to verify your account."))
                        return render(request, 'login.html')
            else: 
               messages.success(request, ("Oops! Please check your email or password."))
               return render(request, 'login.html')
    return render (request, 'login.html') 

def deletesession(request):
    try:
        if request.session['public_id']:
            del request.session['public_id']
    except:
        pass
    try:
        if request.session['authorized_id']:
            del request.session['authorized_id']
    except:
        pass
    return HttpResponseRedirect('/login')

def about_us(request):
    if request.method == "POST":
        myname        = request.POST['myname'].title()
        myemail       = request.POST['myemail']
        mysubject     = request.POST['mysubject'].title()
        mymessage     = request.POST['mymessage']

    #send an email
        send_mail (
            'Roadcast: ' + mysubject , #subject
            'A user named ' + myname + ' with an email of ' + myemail + ' has send a message of:  ' + mymessage, #message
            myemail, #from email
            ['danenapigkit@gmail.com'], # to email change to naviliansquads@gmail.com pagsesend na 
        )

        context = {
            'myname': myname
        }
        messages.success(request, ("We've received your email and will respond shortly."))
        return HttpResponseRedirect('/aboutus#contactus')
    else:
        return render (request, 'about_us.html') 

def contact_us(request):
    return render (request, 'contact_us.html') 

def contact_no(request):
    return render (request, 'contact_no.html') 

def success(request):
    return render(request, 'submit_success.html')

def sign_up (request):
    return render (request, 'sign_up.html')
    
def duplicate_gen (request): #Jew
    if request.method   =="POST": #save data when button is clicked
        gen_surname     = request.POST["gen_surname"].title()
        gen_fname       = request.POST["gen_fname"].title()
        gen_sex         = request.POST["gen_sex"]
        gen_bday        = request.POST["gen_bday"]
        gen_region      = request.POST["gen_region"].title()
        gen_province    = request.POST["gen_province"].title()
        gen_city        = request.POST["gen_city"].title()
        gen_barangay    = request.POST["gen_barangay"].title()
        gen_contact_no  = request.POST["gen_contact_no"]
        gen_username    = request.POST["gen_username"]
        gen_pass        = request.POST["gen_pass"]
        gen_valid_id    = request.POST["gen_valid_id"]
        gen_upload_id   = request.POST["gen_valid_id"]
        gen_profile     = 'media/Public/default.jpg'

        #save image to database 
        if request.FILES.get("gen_upload_id"):
            gen_upload_id   = request.FILES.get('gen_upload_id')
        else:
            gen_upload_id   = 'media/Public/default.jpg'

        if tbl_genpub_users.objects.filter(gen_username = gen_username):
            messages.success(request, ("Oops! That email address is already taken. Please use a different one."))
            return render(request, 'sign_up.html')  

        if Tbl_add_members.objects.filter(Members_Email=gen_username):
            messages.success(request, ("Oops! That email address is already taken. Please use a different one."))
            return HttpResponseRedirect('signup')

        #Recaptcha validation
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': "6LezEbYcAAAAAPs9xoE2PnJsb18ljq1oi1aWZ0Gp",
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        if result['success'] == False:
            messages.error(request, ('Oops! Invalid reCAPTCHA. Please try again.'))
            return HttpResponseRedirect('signup')
            
        submit = tbl_genpub_users.objects.create(gen_surname = gen_surname,gen_fname = gen_fname, gen_sex = gen_sex, gen_bday=gen_bday, gen_region = gen_region, gen_province = gen_province, gen_city = gen_city,
        gen_barangay = gen_barangay, gen_contact_no = gen_contact_no, gen_username = gen_username, gen_pass = gen_pass, gen_valid_id = gen_valid_id,gen_upload_id=gen_upload_id, gen_profile = gen_profile )#,gen_upload_id=gen_upload_id
        submit.save()

        send_action_email(submit,request)
        messages.success(request, ("We've already sent you an email. Please check your email to verify your account."))
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'sign_up.html')

#Email verification - Jew
def send_action_email(public, request):
    current_site = get_current_site(request)
    email_subject = ' Activate your Account'
    email_body = render_to_string('email verification.html',{
        'public': public,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(public.pk)),
        'token': generate_token.make_token(public)
    })

    send_html_mail('Roadcast: Verify your Email Address', email_body,{public.gen_username},settings.EMAIL_HOST_USER)

    email = EmailMessage(subject=email_subject, body=email_body,
        from_email=settings.EMAIL_FROM_PUBLIC,
        to={public.gen_username}
    )
    # email.send()

def activate_user(request,uidb64,token): #Jew
    try:
        uid =force_text(urlsafe_base64_decode(uidb64))
        public= tbl_genpub_users.objects.get(pk=uid)

    except Exception as e:
        public = None

    if public and generate_token.check_token(public,token): #if this is true valid siya
        public.is_email_verified = True
        public.save()

        messages.success(request, ("Your email is now verified. Please wait for the admin's approval of your registration."))
        return HttpResponseRedirect(reverse('login'))
    return render (request,'activation_twice.html', {'public':public})


def sign_up_validation (request): #Jew
    list = tbl_genpub_users.objects.all()
    context={'list':list}
    return render (request, 'sign_up_validation.html',context)

# def admin_audit_trail(request):
#     return render (request, 'admin_audit_trail.html')  

# def admin_list_members(request):
#     return render (request, 'admin_list_members.html') 

# def admin_departments(request):
#     return render (request, 'admin_list_members.html')   

# def admin_investigators(request):
#     return render (request, 'admin_investigators.html')  

# def admin_view_investigators(request):
#     return render (request, 'admin_view_investigators.html')  

def is_valid(param):
    return param != "" and param is not None
def is_not_valid(param):
    return param == "" and param is None

#Jew - Sign up Validation / makikita na dito yung details
def notif_sign_up_validation (request, signup_id):
    unread_sign_up_validation = tbl_genpub_users.objects.get(id=signup_id) #kukunin id ng mga nag signup
    unread_sign_up_validation.Read_Status = "Yes" 
    unread_sign_up_validation.save()
    
    #for gen pub reports inbox
    sign_up_validation = tbl_genpub_users.objects.all().order_by('-id')
    unread_notif_count_signup = tbl_genpub_users.objects.filter(Read_Status="No").count()

    data = {
        'detail': unread_sign_up_validation,
        'unread_notif_count_signup': unread_notif_count_signup,
        'sign_up_validation':sign_up_validation,
        "all": authorized,
        "pub": pub,

    }
    return render (request, 'notif_sign_up_validation.html', data)

#Jew
def genpub_verified(request, pk=None):
    if pk !=None:
        genpub = tbl_genpub_users.objects.get(id=pk)
        genpub.is_verified = True
        genpub.save()
    unread_sign_up_validation = tbl_genpub_users.objects.get(id=pk) #kukunin id ng mga nag signup
    sign_up_validation = tbl_genpub_users.objects.all().order_by('-id')
    unread_notif_count_signup = tbl_genpub_users.objects.filter(Read_Status="No").count()

    data = {
        'detail': unread_sign_up_validation,
        'unread_notif_count_signup': unread_notif_count_signup,
        'sign_up_validation':sign_up_validation,
        "all": authorized, 
        "pub": pub,
    }
    messages.success(request, " is verified")
    return render (request, 'notif_sign_up_validation.html', data)

#Jew
def genpub_rejected(request,pk):
    unread_sign_up_validation = tbl_genpub_users.objects.get(id=pk) #kukunin id ng mga nag signup

    if pk !=None:
        genpub = tbl_genpub_users.objects.get(id=pk)
        genpub.is_verified = False
        genpub.save()
        messages.success(request, " is rejected")

        
    unread_sign_up_validation = tbl_genpub_users.objects.get(id=pk) #kukunin id ng mga nag signup
    sign_up_validation = tbl_genpub_users.objects.all().order_by('-id')
    unread_notif_count_signup = tbl_genpub_users.objects.filter(Read_Status="No").count()

    data = {
        'detail': unread_sign_up_validation,
        'unread_notif_count_signup': unread_notif_count_signup,
        'sign_up_validation':sign_up_validation,
        "all": authorized, 
        "pub": pub,
    }
    return render (request, 'notif_sign_up_validation.html', data)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def extract_lat_lng(address_postal):
    #FOR GOOGLE MAPS
    
    API_KEY='AIzaSyACS7G3CoYRTEAOy4vAUdPq1H08ueUoDXI'
    endpoint=f'https://maps.googleapis.com/maps/api/geocode/json?'
                    
    params={
        'key':API_KEY,
        'address':address_postal
    }
    urlparams= urlencode(params)
    url=f"{endpoint}{urlparams}"
        
    r= requests.get(url)
    if r.status_code not in range(200,299):
        return {}
    latlng={}
    try:
        latlng= r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get('lat'),latlng.get('lng')      
    #END FOR GOOGLE MAPS


def DashboardView (request):
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except:
        pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass


    #FOR CHARTS FORECASTING
    datelist= Tbl_forecast.objects.all().order_by("-Date")[:14]
    datelist_values= Tbl_forecast.objects.all().order_by("-Date")[:14][6:]
    datelist_values_forecast= Tbl_forecast.objects.all().order_by("-Date")[:7]
    reversed_datelist=reversed(datelist)
    reversed_datelist_values=reversed(datelist_values)
    reversed_datelist_values_forecast=reversed(datelist_values_forecast)

    #END OF FOR CHARTS FORECASTING

    # FOR FORECASTING
    # today = date.today() 

    earliest_day= Tbl_pasig_incidents.objects.exclude(Q(Date__isnull=True)).order_by("Date")[0].Date
    
    a_week= date(2019,1,1)
    test=date.today() + timedelta(7)

    end_date=date(2019,2,28)+ timedelta(7)
    limit = Tbl_forecast.objects.all().count()
    start_i=0
    end_i=7
    i_day=6
    count=0
    for insert_date in daterange(earliest_day,test):

        date_exist=Tbl_forecast.objects.filter(Date=insert_date,).exists()


        if not date_exist:
            incident_count=Tbl_pasig_incidents.objects.filter(Date=insert_date).count()
            create= Tbl_forecast.objects.create(Date=insert_date.strftime("%Y-%m-%d"), Incidents=incident_count, Averages=0)
        else:
            incident_count=Tbl_pasig_incidents.objects.filter(Date=insert_date).count()
            create= Tbl_forecast.objects.filter(Date=insert_date.strftime("%Y-%m-%d")).update(Incidents=incident_count)

            while i_day < limit:
                count_avg=Tbl_forecast.objects.all().order_by('Date')[start_i:end_i].aggregate(Avg('Incidents'))
                nth=Tbl_forecast.objects.all().order_by('Date')[i_day]
                insert=Tbl_forecast.objects.filter(Date=nth.Date).update(Averages=count_avg['Incidents__avg'])
                start_i += 1
                end_i += 1
                i_day += 1 #may mali dito di gumagana yung iteration
    # END OF FORECASTING

    all_total = Tbl_pasig_incidents.objects.count()

    
    yesterday = today - timedelta(days=1)
    year, week_num, day_of_week =  date.today().isocalendar()

    this_week = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year, Date__year__lte=today.year, Date__week=week_num,).count()
    yesterday_total = Tbl_pasig_incidents.objects.filter(Date__gte = yesterday, Date__lt = today).count()
    this_day = Tbl_pasig_incidents.objects.filter(Date__gte = today, Date__lte = today, Date__year__gte=today.year, Date__year__lte=today.year).count()

    # FOR MULTIPLE MARKERS IN DASHBOARD
    markers= Tbl_pasig_incidents.objects.exclude(Q(Latitude__isnull=True) | Q(Longitude__isnull=True) | Q(Longitude ="None") | Q(Latitude ="None"))

    #Sessions
    authorized = Tbl_add_members.objects.all()
    pub            = tbl_genpub_users.objects.all()

    

    data = {
        "all_total": all_total,
        "this_week": this_week,
        "week_num": week_num,
        "yesterday_total":yesterday_total,
        "this_day": this_day,
        "this_year": today.year,
        
        "all": authorized,
        "pub": pub,
        'unread_notif_count': unread_notif_count,

        'datelist':reversed_datelist,
        'markers_json':markers,
        "reversed_datelist_values":reversed_datelist_values,
        "reversed_datelist_values_forecast":reversed_datelist_values_forecast     
    }
    return render (request, 'dashboard.html', data)

def get_data(request, *args, **kwargs):
    #District 1
    d1_brgys = []
    d1_brgys_count = []
    d1_brgys_list = Tbl_barangay.objects.filter(District_id = '1').values_list('Barangay', flat=True)
    
    for brgy in d1_brgys_list:
        d1_brgys.append(brgy)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=today.year,
                                    Date__year__lte=today.year,
                                    # Date__month__gte=today.month,
                                    # Date__month__lte=today.month,
                                    Barangay_id__Barangay = brgy).count()        
        d1_brgys_count.append(x)

    #District 2
    d2_brgys = []
    d2_brgys_count = []
    d2_brgys_list = Tbl_barangay.objects.filter(District_id = '2').values_list('Barangay', flat=True)
    
    for brgy in d2_brgys_list:
        d2_brgys.append(brgy)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=today.year,
                                    Date__year__lte=today.year,
                                    # Date__month__gte=today.month,
                                    # Date__month__lte=today.month,
                                    Barangay_id__Barangay = brgy).count()                          
        d2_brgys_count.append(x)


    #CRIME/OFFENSE
    offense = []
    offenses = Tbl_pasig_incidents.objects.exclude(Q(CrimeOffense__isnull=True) | Q(CrimeOffense__exact='') ).values_list('CrimeOffense', flat=True)

    str = ",".join(offenses)
    offense = str.split(",")

    offenses_distict = set(offense)
    offense_labels = []
    offense_count = []

    for off in offenses_distict:
        if off == '':
            off = 'none'
        offense_labels.append(off)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=today.year,
                                    Date__year__lte=today.year,
                                    # Date__month__gte=today.month,
                                    # Date__month__lte=today.month,
                                    CrimeOffense = off).exclude(CrimeOffense__isnull=True).count()   
        offense_count.append(x)

    #Sex 
    suspect_sex = []
    victim_sex = []

    suspect_sex = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year, Date__year__lte=today.year,).values_list('Suspect_Sex', flat=True)
    victim_sex = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year, Date__year__lte=today.year,).values_list('Victim_Sex', flat=True)

    sex_combined = list(chain(suspect_sex, victim_sex))
    sex_distinct = set(sex_combined)
    sex_labels = []
    sex_count = []

    for sex in sex_distinct:
        if sex == '':
            sex = 'blank'
            sex_labels.append(sex)
            x = sex_combined.count('')
            sex_count.append(x)

        else:
            sex_labels.append(sex)
            x = sex_combined.count(sex)
            sex_count.append(x)
    
    #Time Plot
    # time(hour = 0, minute = 0, second = 0)
    am12 = datetime.time(0, 0, 0)
    am2  = datetime.time(2, 0, 0)
    am4  = datetime.time(4, 0, 0)
    am6  = datetime.time(6, 0, 0)
    am8  = datetime.time(8, 0, 0)
    am10 = datetime.time(10, 0, 0)
    pm12 = datetime.time(12, 0, 0)
    pm2 = datetime.time(14, 0, 0)
    pm4 = datetime.time(16, 0, 0)
    pm6 = datetime.time(18, 0, 0)
    pm8 = datetime.time(20, 0, 0)
    pm10 = datetime.time(22, 0, 0)

    
    am12_am2 = Tbl_pasig_incidents.objects.filter(Time__gte = am12, Time__lt = am2, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    am2_am4 = Tbl_pasig_incidents.objects.filter(Time__gte = am2, Time__lt = am4, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    am4_am6 = Tbl_pasig_incidents.objects.filter(Time__gte = am4, Time__lt = am6, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    am8_am10 = Tbl_pasig_incidents.objects.filter(Time__gte = am8, Time__lt = am10, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    am10_pm12 = Tbl_pasig_incidents.objects.filter(Time__gte = am10, Time__lt = pm12, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm12_pm2 = Tbl_pasig_incidents.objects.filter(Time__gte = pm12, Time__lt = pm2, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm2_pm4 = Tbl_pasig_incidents.objects.filter(Time__gte = pm2, Time__lt = pm4, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm4_pm6 = Tbl_pasig_incidents.objects.filter(Time__gte = pm4, Time__lt = pm6, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm6_pm8 = Tbl_pasig_incidents.objects.filter(Time__gte = pm6, Time__lt = pm8, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm8_pm10 = Tbl_pasig_incidents.objects.filter(Time__gte = pm8, Time__lt = pm10, Date__year__gte = today.year, Date__year__lte = today.year,).count()
    pm10_am12 = Tbl_pasig_incidents.objects.filter(Time__gte = pm10, Time__lt = am12, Date__year__gte = today.year, Date__year__lte = today.year,).count()

    time_count = [am12_am2, am2_am4,am4_am6, am8_am10, am10_pm12, pm12_pm2, pm2_pm4, pm4_pm6, pm6_pm8, pm8_pm10, pm10_am12]

    #SEVERITY 
    suspect_severity = []
    victim_severity = []

    suspect_severity = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year,Date__year__lte=today.year,).values_list('Suspect_Severity', flat=True)
    victim_severity = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year,Date__year__lte=today.year, ).values_list('Victim_Severity', flat=True)

    severity_combined = list(chain(suspect_severity, victim_severity))
    distinct_severity = list(set(severity_combined))
    severity_count = []
    severity_total = 0

    for severity in distinct_severity:
        x = severity_combined.count(severity)
        severity_count.append(x)
        severity_total += x

    #Day of the week 
    day_labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_count = []
    
    for day in day_labels:
        x = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year, Date__year__lte=today.year, Day = day).count()                          
        day_count.append(x)


    data = {
            "district2_labels": d2_brgys,
            "district2_count": d2_brgys_count,

            "district1_labels": d1_brgys,
            "district1_count": d1_brgys_count,

            "offense_labels":offense_labels,
            "offense_count": offense_count,

            "sex_labels": sex_labels,
            "sex_count": sex_count,

            "time_count":time_count,

            "severity_labels":distinct_severity,
            "severity_count":severity_count,
            
            "day_labels": day_labels,
            "day_count": day_count,
    }
    return JsonResponse(data) #http response

def archiving_solved_cases (request, incident_id):
    try:
        incident_detail=Tbl_pasig_incidents.objects.get(id=incident_id)
        incident_detail.archive="Yes"
        incident_detail.save()
        messages.success(request, ("Incident Successfully Archived!"))
        return HttpResponseRedirect('/incidents/view')
    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")

def unarchiving_solved_cases (request, incident_id):
    try:
        incident_detail=Tbl_pasig_incidents.objects.get(id=incident_id)
        incident_detail.archive="No"
        incident_detail.save()
        messages.success(request, ("Incident Successfully Unarchived!"))
        return HttpResponseRedirect('/incidents/view')
    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")  

def view_archive_incidents (request):

   if request.method=="GET":
        incident_type = request.GET.get('coltype') 
        barang= request.GET.get('barangay')
        from_date =  request.GET.get('from_date')
        to_date =   request.GET.get('to_date')
        unread_count = Tbl_pasig_incidents.objects.filter(Q(read_status = "No") & Q(Case_Status = "Solved") &~Q(archive= "No")).exclude(Q(archive__isnull=True) | Q(archive__exact='')).count()

    
        if is_valid(from_date) & is_valid(to_date):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" and Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'archive_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
                
        elif is_valid(from_date) & is_valid(to_date) & is_not_valid(incident_type) & is_not_valid(barang):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'"AND Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'archive_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub, "unread_count": unread_count})
   
        if bool(incident_type) & bool(barang) :
            if incident_type=="Collision":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" and Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'archive_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
            elif barang=="0":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" order by id DESC')
                return render(request, 'archive_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
            
            else:
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'archive_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
        else:
            incident_model=Tbl_pasig_incidents.objects.raw('select * from roadcast_tbl_pasig_incidents WHERE archive = "Yes" and Case_Status = "Solved" order by id DESC')
            
            paginator = Paginator(incident_model, 10)
            page_number = request.GET.get('page')
            incident_model = paginator.get_page(page_number) 

            context = {
                "all": authorized,
                "pub": pub,
                "pasig_incident_list":incident_model,
                "unread_count": unread_count
            }
        
            return render (request, 'archive_incidents.html',context)

def view_incidents (request):
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except:
        pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass

    incident_model=Tbl_pasig_incidents.objects.raw('select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" order by id DESC')
            
    paginator = Paginator(incident_model, 10) #ano at ilan ang ipapakita per page
    page_number = request.GET.get('page') #ganto talaga
    incident_model = paginator.get_page(page_number) #ito ren, except sa var name

    unread_count = Tbl_pasig_incidents.objects.filter(Q(read_status = "No") & Q(Case_Status = "Solved") &~Q(archive= "Yes")).count()
    
    if request.method=="GET":
        incident_type = request.GET.get('coltype') 
        barang= request.GET.get('barangay')
        from_date =  request.GET.get('from_date')
        to_date =   request.GET.get('to_date')
        
        if is_valid(from_date) & is_valid(to_date):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" and Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
                
        elif is_valid(from_date) & is_valid(to_date) & is_not_valid(incident_type) & is_not_valid(barang):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'"AND Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub, "unread_count": unread_count})
   
        if bool(incident_type) & bool(barang) :
            if incident_type=="Collision":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" and Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
            elif barang=="0":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
            
            else:
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE archive = "No" and Case_Status = "Solved" and Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search, "all": authorized, "pub": pub,  "unread_count": unread_count})
        else:
            

            context = {
                'unread_notif_count': unread_notif_count,
                "all": authorized,
                "pub": pub,
                "pasig_incident_list":incident_model,
                "unread_count": unread_count
            }
           
            return render (request, 'encoder_view_incidents.html',context)

    else:
        try:
            if request.session['public_id']:
                searched = request.POST['searched']

                incident_model     = Tbl_pasig_incidents.objects.filter(Q(Barangay_id_id__Barangay__icontains = searched)|Q(Incident_Type__icontains = searched)|Q(Case_Status__icontains = searched)).order_by('-id')

                context = {
                    'searched': searched,
                    'unread_notif_count': unread_notif_count,
                    "all": authorized,
                    "pub": pub,
                    "pasig_incident_list":incident_model,
                    "unread_count": unread_count
                }
            return render (request, 'encoder_view_incidents.html',context)

        except:
            searched = request.POST['searched']
            incident_model     = Tbl_pasig_incidents.objects.filter(Q(Barangay_id_id__Barangay__icontains = searched)|Q(Incident_Type__icontains = searched)|Q(Case_Status__icontains = searched)|Q(Suspect_Fname__icontains = searched)|Q(Suspect_Lname__icontains = searched)|Q(Victim_Fname__icontains = searched)|Q(Victim_Lname__icontains = searched)).order_by('-id')

            context = {
                'searched': searched,
                'unread_notif_count': unread_notif_count,
                "all": authorized,
                "pub": pub,
                "pasig_incident_list":incident_model,
                "unread_count": unread_count
            }
        
            return render (request, 'encoder_view_incidents.html',context)



def add_incident (request): #add using CSV
    try:
        #Landing page ng add incident page / wala pang process
        if request.method == "GET":
            member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
            investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
            brgy_list = Tbl_barangay.objects.all()

            context = {
                'brgy_list': brgy_list, 
                'investigators_list': investigators_list,
                "all": authorized,
                "pub": pub,
                'unread_notif_count': unread_notif_count,
            }
            return render(request, 'add_incident.html', context)

        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('ISO-8859-1')
      
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter='|'):
            _, created = Tbl_pasig_incidents.objects.get_or_create(
                
                City=column[0],
                UnitStation=column[1],
                CrimeOffense=column[2],
                Week=column[3],
                Date= column[4][6:] + "-" + column[4][3:5] + "-" + column[4][:2],
                Time=column[5],
                Day=column[6],
                Incident_Type=column[7],
                Number_of_Persons_Involved=column[8],
                Light=column[9],
                Weather=column[10],
                Case_Status=column[11],
                
                Address=column[12],
                Along_Avenue=column[13],
                Corner_Avenue=column[14],
                Along_Road=column[15],
                Corner_Road=column[16],
                Along_Street=column[17],
                Corner_Street=column[18],
                Bound=column[19],
                Along_Highway=column[20],
                Corner_Highway=column[21],
                Along_Boulevard=column[22],
                Corner_Boulevard=column[23],
                Others=column[24],

                Surface_Condition=column[25],
                Surface_Type=column[26], 
                Road_Class=column[27], 
                Road_Repair = column[28], 
                Hit_and_Run = column[29], 
                Road_Character=column[30], 
        
                Suspect_Name=column[31], 
                Suspect_Severity=column[32],
                Suspect_Age=column[33], 
                Suspect_Sex=column[34], 
                Suspect_Civil_Status = column[35], 
                Suspect_Address=column[36],  
                Suspect_Vehicle=column[37], 
                Suspect_Vehicle_Body_Type=column[38], 
                Suspect_Plate_No=column[39],
                Suspect_Reg_Owner=column[40], 
                Suspect_Drl_No=column[41], Suspect_Vehicle_Year_Model=column[42], 
                
                Victim_Type=column[43],
                Victim_Name=column[44], Victim_Severity=column[45],Victim_Age=column[46], 
                Victim_Sex=column[47], Victim_Civil_Status = column[48], Victim_Address=column[49], 
                Victim_Vehicle=column[50], Victim_Vehicle_Body_Type=column[51], 
                Victim_Plate_No=column[52],Victim_Reg_Owner=column[53], 
                Victim_Drl_No=column[54], Victim_Vehicle_Year_Model=column[55],

                Narrative=column[56], 
                # date_added=column[57][6:] + "-" + column[57][3:5] + "-" + column[57][:2],
                # added_by=column[58],

                District_id=column[59],
                Barangay_id_id=column[60]
               
            )

            brgy_list = Tbl_barangay.objects.all()
            
            context = {
                'brgy_list': brgy_list, 
                'success_message':"Successfully Added!",
                'url':'url',
                "all": authorized,
                "pub": pub,
            }
            return render (request, 'add_incident.html', context)
    except:
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.png'):
            messages.error(request, 'Error: This is not a CSV file.')

        context = {
            'error_message': "Error uploading file. Please check file format.",
            "all": authorized,
            "pub": pub,
        }
        return render (request, 'add_incident.html', context)

def processAddIncident(request): #Add using forms
    city = "Pasig"
    unit_station = "Pasig City Police Station"
    crime_offense = request.POST.get('display_offense')
    week = request.POST.get('week') 
    date_committed = request.POST.get('DateCommitted') #name attribute of textbox
    current_time = request.POST.get('currentTime')
    day = request.POST.get('day_of_the_week')
    col_type = request.POST.get('collision_type')
    no_of_person_involved = "1"
    light = "Day"
    weather = request.POST.get('weather')
    case_status = request.POST.get('case_status')
    district = request.POST.get('district')
    barangay = request.POST.get('barangay')
    address = request.POST.get('place_committed')
    along = request.POST.get('along')
    corner = request.POST.get('corner')
    latitude = request.POST.get('lat')
    longitude = request.POST.get('long')
   
    surface_cond = request.POST.get('surface_condition')
    surface_type = request.POST.get('surface_type')
    road_repair = request.POST.get('road-repair')
    hit_and_run = request.POST.get('hit-and-run')
    road_char = request.POST.get('road_character')

    sus_type = request.POST.get('sus_type')
    sus_fname = request.POST.get('sus_fname')
    sus_lname = request.POST.get('sus_lname')
    sus_severity = request.POST.get('sus_severity')
    sus_age = request.POST.get('sus_age')
    if sus_age:
        sus_age = request.POST.get('sus_age')
    else:
        sus_age = None

    sus_sex = request.POST.get('s_sex')
    sus_civil_status = request.POST.get('sus_civil_status')
    sus_add = request.POST.get('sus_add')
    sus_vehicle = request.POST.get('sus_vehicle') #brand/model
    sus_vehicle_body_type = request.POST.get('sus_vehicle_body_type')
    sus_plate_no = request.POST.get('sus_plate_no')
    sus_reg_owner = request.POST.get('sus_reg_owner')
    sus_drl = request.POST.get('sus_drl')
    sus_drl_exp = request.POST.get('sus_drl_exp')
    if sus_drl_exp:
        sus_drl_exp = request.POST.get('sus_drl_exp')
    else:
        sus_drl_exp = None

    vic_type = request.POST.get('vic_type')
    vic_fname = request.POST.get('vic_fname')
    vic_lname = request.POST.get('vic_lname')
    vic_severity = request.POST.get('vic_severity')
    vic_age = request.POST.get('vic_age')
    if vic_age:
        vic_age = request.POST.get('vic_age')
    else:
        vic_age = None
        
    vic_sex = request.POST.get('v_sex')
    vic_civil_status = request.POST.get('vic_civil_status')
    vic_add = request.POST.get('vic_add')
    vic_vehicle = request.POST.get('vic_vehicle')
    vic_vehicle_body_type = request.POST.get('vic_vehicle_body_type')
    vic_plate_no = request.POST.get('vic_plate_no')
    vic_reg_owner = request.POST.get('vic_reg_owner')
    vic_drl = request.POST.get('vic_drl')
    vic_drl_exp = request.POST.get('vic_drl_exp')
    if vic_drl_exp:
        vic_drl_exp = request.POST.get('sus_drl_exp')
    else:
        vic_drl_exp = None

   
    narrative = request.POST.get('narrative')
    added_by = "For now encoder"
    inv_name = request.POST.get('inv_name')
    
    incident_record = Tbl_pasig_incidents.objects.create(
                    City        = city, 
                    UnitStation = unit_station,               
                    CrimeOffense= crime_offense, 
                    Week        = week,          
                    Date        = date_committed,               
                    Time        = current_time, 
                    Day         = day, 
                    Incident_Type   = col_type, 
                    Number_of_Persons_Involved  = no_of_person_involved, 
                    Light       = light, 
                    Weather     = weather, 
                    Case_Status = case_status, 
                    District_id = district, 
                    Barangay_id_id = barangay, 
                    Address        = address,
                    Along          = along,
                    Corner         = corner,
                    Latitude       = latitude,
                    Longitude     = longitude,

                    Surface_Condition   = surface_cond, 
                    Surface_Type        = surface_type, 
                    Road_Repair         = road_repair, 
                    Hit_and_Run         = hit_and_run,
                    Road_Character      = road_char, 
    
                    Suspect_Type        = sus_type,
                    Suspect_Fname       = sus_fname, 
                    Suspect_Lname       = sus_lname, 
                    Suspect_Severity    = sus_severity,
                    Suspect_Age         = sus_age, 
                    Suspect_Sex         = sus_sex, 
                    Suspect_Civil_Status = sus_civil_status, 
                    Suspect_Address     = sus_add,  
                    Suspect_Vehicle     = sus_vehicle, 
                    Suspect_Vehicle_Body_Type   = sus_vehicle_body_type, 
                    Suspect_Plate_No    = sus_plate_no,
                    Suspect_Reg_Owner   = sus_reg_owner, 
                    Suspect_Drl_No      = sus_drl, 
                    Suspect_Drl_Exp     = sus_drl_exp, 

                    Victim_Type         = vic_type,
                    Victim_Fname        = vic_fname, 
                    Victim_Lname        = vic_lname, 
                    Victim_Severity     = vic_severity,
                    Victim_Age          = vic_age, 
                    Victim_Sex          = vic_sex, 
                    Victim_Civil_Status = vic_civil_status, 
                    Victim_Address      = vic_add, 
                    Victim_Vehicle      = vic_vehicle, 
                    Victim_Vehicle_Body_Type = vic_vehicle_body_type, 
                    Victim_Plate_No          = vic_plate_no,
                    Victim_Reg_Owner         = vic_reg_owner, 
                    Victim_Drl_No            = vic_drl, 
                    Victim_Drl_Exp           = vic_drl_exp, 

                    Narrative    = narrative, 
                    Investigator_id = inv_name,
                    added_by     = added_by,
                    archive      = "No" )
                    
    incident_record.save()
    messages.success(request, ("Incident details successfully added!"))
    return HttpResponseRedirect('/incidents/view')

def processCSV (request):
    data = Tbl_pasig_incidents.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {'order': 'Order of the CSV should be name, email, address, phone, profile',
             'incident_csv': data }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, 'add_incident.html', prompt)
    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Tbl_barangay.objects.get_or_create(
            Barangay=column[0],
            District_id_id=column[1]
        )
    context = {}
    return render(request, 'add_incident.html', context)

def processDeleteIncident (request, incident_id):
    Tbl_pasig_incidents.objects.filter(id=incident_id).delete()
    messages.success(request, ("Successfully Deleted!"))
    return HttpResponseRedirect('/incidents/view/archives')

#encoder and admin view incidents
def encoder_view_incident_detail(request, incident_id): #pag view lang ng edit page, pas sinubmit form, YUNG def processEdit mag hahandle
    try:
        member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
        investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
        substation_list = Tbl_substation.objects.all()
        brgy_list = Tbl_barangay.objects.all()
        all_incidents = Tbl_pasig_incidents.objects.all()
        pasig_incident_detail = Tbl_pasig_incidents.objects.get(id=incident_id)
        pasig_incident_detail.read_status = "Yes"
        pasig_incident_detail.save()


    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")

    return render(request, 'encoder_view_incident_detail.html', 
        {'pasig_incident_detail': pasig_incident_detail,
         'all_incidents': all_incidents,
         'investigators_list': investigators_list,
         'substation_list': substation_list,
         'brgy_list':brgy_list,
         "all": authorized,
         "pub": pub,
         'unread_notif_count': unread_notif_count,})

def processEditIncident(request, incident_id):
    incident_detail =  Tbl_pasig_incidents.objects.get(id=incident_id)

    try:
        crime_offense = request.POST.get('display_offense') 
        date_committed = request.POST.get('DateCommitted') #name attribute of textbox
        incident_time = request.POST.get('incidentTime')
        day = request.POST.get('day_of_the_week')
        col_type = request.POST.get('collision_type')
        #no_of_person_involved = "1"
        #light = "Day"
        weather = request.POST.get('weather')
        case_status = request.POST.get('case_status')
        district = request.POST.get('district')
        barangay = request.POST.get('barangay')
        address = request.POST.get('place_committed')
        along = request.POST.get('along')
        corner = request.POST.get('corner')
        latitude = request.POST.get('lat')
        longitude = request.POST.get('lon')
   
        surface_cond = request.POST.get('surface_condition')
        surface_type = request.POST.get('surface_type')
        road_repair = request.POST.get('road-repair')
        hit_and_run = request.POST.get('hit-and-run')
        road_char = request.POST.get('road_character')

        sus_type = request.POST.get('sus_type')
        sus_fname = request.POST.get('sus_fname')
        sus_lname = request.POST.get('sus_lname')
        sus_severity = request.POST.get('sus_severity')
        sus_age = request.POST.get('sus_age')
        sus_sex = request.POST.get('s_sex')
        sus_civil_status = request.POST.get('sus_civil_status')
        sus_add = request.POST.get('sus_add')
        sus_vehicle = request.POST.get('sus_vehicle')
        sus_vehicle_body_type = request.POST.get('sus_vehicle_body_type')
        sus_plate_no = request.POST.get('sus_plate_no')
        sus_reg_owner = request.POST.get('sus_reg_owner')
        sus_drl = request.POST.get('sus_drl')
        sus_drl_exp = request.POST.get('sus_drl_exp')
        if sus_drl_exp:
            sus_drl_exp = request.POST.get('sus_drl_exp')
        else:
            sus_drl_exp = None

        vic_type = request.POST.get('vic_type')
        vic_fname = request.POST.get('vic_fname')
        vic_lname = request.POST.get('vic_lname')
        vic_severity = request.POST.get('vic_severity')
        vic_age = request.POST.get('vic_age')
        vic_sex = request.POST.get('v_sex')
        vic_civil_status = request.POST.get('vic_civil_status')
        vic_add = request.POST.get('vic_add')
        vic_vehicle = request.POST.get('vic_vehicle')
        vic_vehicle_body_type = request.POST.get('vic_vehicle_body_type')
        vic_plate_no = request.POST.get('vic_plate_no')
        vic_reg_owner = request.POST.get('vic_reg_owner')
        vic_drl = request.POST.get('vic_drl')
        vic_drl_exp = request.POST.get('vic_drl_exp')
        if vic_drl_exp:
            vic_drl_exp = request.POST.get('sus_drl_exp')
        else:
            vic_drl_exp = None
    
        narrative = request.POST.get('narrative')
        # added_by = "Encoder"
        inv_name = request.POST.get('inv_name')
      
    except (KeyError, Tbl_pasig_incidents.DoesNotExist): #KeyError is partner nung get_object_or_404
        return render(request, 'encoder_view_incident_detail.html', {
            'detail':incident_detail,
            'error_message': "Problem Updating Record.",
            'unread_notif_count': unread_notif_count,
        })
    else:
        incident = Tbl_pasig_incidents.objects.get(id=incident_id) #kukunin yung row sa database na kapareha ng incident_id
        incident.CrimeOffense=crime_offense         
        incident.Date=date_committed             
        incident.Time=incident_time
        incident.Day = day 
        incident.Incident_Type=col_type
        # incident.Number_of_Persons_Involved=no_of_person_involve
        # incident.Light=light 
        incident.Weather=weather 
        incident.Case_Status=case_status 
        incident.District_id = district 
        incident.Barangay_id_id = barangay 
        incident.Address = address 
        incident.Along_Avenue = along 
        incident.Corner_Avenue = corner
        incident.Latitude       = latitude
        incident.Longitude     = longitude

        incident.Surface_Condition=surface_cond 
        incident.Surface_Type=surface_type
        incident.Road_Repair = road_repair 
        incident.Hit_and_Run = hit_and_run
        incident.Road_Character=road_char

        incident.Suspect_Type = sus_type
        incident.Suspect_Fname=sus_fname
        incident.Suspect_Lname=sus_lname
        incident.Suspect_Severity=sus_severity
        incident.Suspect_Age=sus_age 
        incident.Suspect_Sex=sus_sex 
        incident.Suspect_Civil_Status = sus_civil_status 
        incident.Suspect_Address=sus_add  
        incident.Suspect_Vehicle=sus_vehicle 
        incident.Suspect_Vehicle_Body_Type=sus_vehicle_body_type 
        incident.Suspect_Plate_No=sus_plate_no
        incident.Suspect_Reg_Owner=sus_reg_owner 
        incident.Suspect_Drl_No=sus_drl 
        incident.Suspect_Drl_Exp=sus_drl_exp
        
        incident.Victim_Type = vic_type
        incident.Victim_Fname=vic_fname
        incident.Victim_Lname=vic_lname  
        incident.Victim_Severity=vic_severity
        incident.Victim_Age=vic_age 
        incident.Victim_Sex=vic_sex 
        incident.Victim_Civil_Status = vic_civil_status 
        incident.Victim_Address=vic_add 
        incident.Victim_Vehicle=vic_vehicle 
        incident.Victim_Vehicle_Body_Type=vic_vehicle_body_type 
        incident.Victim_Plate_No=vic_plate_no
        incident.Victim_Reg_Owner=vic_reg_owner 
        incident.Victim_Drl_No=vic_drl 
        incident.Victim_Drl_Exp=vic_drl_exp


        incident.Narrative=narrative
        incident.Investigator_id=inv_name
        # incident.added_by=added_by

        incident.save()  #may changes or wala sa profile pic, save parin
        messages.success(request, "Your data has been saved!")
        return HttpResponseRedirect(reverse('incident_detail_view', args=(incident_id, )))

#public and subrep view incidents
def public_view_incident_detail(request, incident_id): #pag view lang ng edit page, pas sinubmit form, YUNG def processEdit mag hahandle
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    
    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()

    except: pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass

    try:
        member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
        investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
        substation_list = Tbl_substation.objects.all()
        brgy_list = Tbl_barangay.objects.all()
        all_incidents = Tbl_pasig_incidents.objects.all()
        pasig_incident_detail = Tbl_pasig_incidents.objects.get(id=incident_id)
        pasig_incident_detail.read_status = "Yes"
        pasig_incident_detail.save()

    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")

    return render(request, 'gen_incident_detail_view.html', 
        {'pasig_incident_detail': pasig_incident_detail,
         'all_incidents': all_incidents,
         'investigators_list': investigators_list,
         'substation_list': substation_list,
         'brgy_list':brgy_list,
         "all": authorized,
         "pub": pub,
         'unread_notif_count': unread_notif_count,})

def report_summary (request):
    context    = {
        "all": authorized,
        "pub": pub,
    }
    return render (request, 'report_summary.html', context)

class JSONResponseMixin:
  """
  A mixin that can be used to render a JSON response.
  """
  def render_to_json_response(self, context, **response_kwargs):

    return JsonResponse(self.get_data(context), **response_kwargs)

  def get_data(self, context):

    return context

# def report_monthly (request):
def monthly_report (request):
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except:
        pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if request.method == 'POST':
        select_year = request.POST.get('select_year') 
        select_month = int(request.POST.get('select_month'))

        month = select_month
        year = select_year

        month_label = months[select_month-1]
        year_label = select_year
        
    else:
        month = today.month
        year = today.year
        month_label = months[today.month-1]
        year_label = today.year

    #District 1
    d1_brgys = []
    d1_brgys_count = []
    d1_brgys_total = 0
    d1_brgys_list = Tbl_barangay.objects.filter(District_id = '1').values_list('Barangay', flat=True)

    for brgy in d1_brgys_list:
        d1_brgys.append(brgy)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,
                                    Date__year__lte=year,
                                    Date__month__gte=month,
                                    Date__month__lte=month,
                                    Barangay_id__Barangay = brgy).count()        
        d1_brgys_count.append(x)
        d1_brgys_total += x

    #District 2
    d2_brgys = []
    d2_brgys_count = []
    d2_brgys_total = 0
    d2_brgys_list = Tbl_barangay.objects.filter(District_id = '2').values_list('Barangay', flat=True)
    
    for brgy in d2_brgys_list:
        d2_brgys.append(brgy)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,
                                    Date__year__lte=year,
                                    Date__month__gte=month,
                                    Date__month__lte=month,
                                    Barangay_id__Barangay = brgy).count()                          
        d2_brgys_count.append(x)
        d2_brgys_total += x

    #CRIME/OFFENSE
    offense = []
    offenses = Tbl_pasig_incidents.objects.exclude(Q(CrimeOffense__isnull=True) | Q(CrimeOffense__exact='')).values_list('CrimeOffense', flat=True)

    str = ",".join(offenses)
    offense = str.split(",")

    offenses_distict = set(offense)
    offense_labels = []
    offense_count = []
    offense_total = 0

    for off in offenses_distict:
        if off == '':
            off = 'none'
        offense_labels.append(off)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,
                                    Date__year__lte=year,
                                    Date__month__gte=month,
                                    Date__month__lte=month,
                                    CrimeOffense = off).exclude(CrimeOffense__isnull=True).count()   
        offense_count.append(x)
        offense_total += x

    #Sex 
    suspect_sex = []
    victim_sex = []

    suspect_sex = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Suspect_Sex', flat=True)

    victim_sex = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Victim_Sex', flat=True)

    sex_combined = list(chain(suspect_sex, victim_sex))
    sex_distinct = set(sex_combined)
    sex_labels = []
    sex_count = []

    for sex in sex_distinct:
        if sex == '':
            sex = 'blank'
            sex_labels.append(sex)
            x = sex_combined.count('')
            sex_count.append(x)

        else:
            sex_labels.append(sex)
            x = sex_combined.count(sex)
            sex_count.append(x)
    
    #Time Plot
    # time(hour = 0, minute = 0, second = 0)
    am12 = datetime.time(0, 0, 0)
    am2  = datetime.time(2, 0, 0)
    am4  = datetime.time(4, 0, 0)
    am6  = datetime.time(6, 0, 0)
    am8  = datetime.time(8, 0, 0)
    am10 = datetime.time(10, 0, 0)
    pm12 = datetime.time(12, 0, 0)
    pm2 = datetime.time(14, 0, 0)
    pm4 = datetime.time(16, 0, 0)
    pm6 = datetime.time(18, 0, 0)
    pm8 = datetime.time(20, 0, 0)
    pm10 = datetime.time(22, 0, 0)

    
    am12_am2 = Tbl_pasig_incidents.objects.filter(Time__gte = am12, Time__lt = am2, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    am2_am4 = Tbl_pasig_incidents.objects.filter(Time__gte = am2, Time__lt = am4, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    am4_am6 = Tbl_pasig_incidents.objects.filter(Time__gte = am4, Time__lt = am6, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    am8_am10 = Tbl_pasig_incidents.objects.filter(Time__gte = am8, Time__lt = am10, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    am10_pm12 = Tbl_pasig_incidents.objects.filter(Time__gte = am10, Time__lt = pm12, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm12_pm2 = Tbl_pasig_incidents.objects.filter(Time__gte = pm12, Time__lt = pm2, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm2_pm4 = Tbl_pasig_incidents.objects.filter(Time__gte = pm2, Time__lt = pm4, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm4_pm6 = Tbl_pasig_incidents.objects.filter(Time__gte = pm4, Time__lt = pm6, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm6_pm8 = Tbl_pasig_incidents.objects.filter(Time__gte = pm6, Time__lt = pm8, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm8_pm10 = Tbl_pasig_incidents.objects.filter(Time__gte = pm8, Time__lt = pm10, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()
    pm10_am12 = Tbl_pasig_incidents.objects.filter(Time__gte = pm10, Time__lt = am12, Date__year__gte = year, Date__year__lte = year, Date__month__gte=month,Date__month__lte=month,).count()

    time_count = [am12_am2, am2_am4,am4_am6, am8_am10, am10_pm12, pm12_pm2, pm2_pm4, pm4_pm6, pm6_pm8, pm8_pm10, pm10_am12]

    # VEHICLE STATS - monthly
    suspect_vehicles = []
    victim_vehicles = []

    suspect_vehicles = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Suspect_Vehicle_Body_Type', flat=True)
    victim_vehicles = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Victim_Vehicle_Body_Type', flat=True)

    vehicles_combined = list(chain(suspect_vehicles, victim_vehicles))
    distinct_vehicles = set(vehicles_combined)
    vehicle_count = []
    vehicle_total = 0

    for vehicle in distinct_vehicles:
        x = vehicles_combined.count(vehicle)
        vehicle_count.append(x)
        vehicle_total = vehicle_total + int(x)

    # AGE STATS - MALE - monthly
    suspect_age_m = []
    victim_age_m = []

    suspect_age_m = Tbl_pasig_incidents.objects.filter(Q(Suspect_Sex='Male') & Q(Suspect_Age__isnull=False), 
                                Date__year__gte=year,Date__year__lte=year,
                                Date__month__gte=month,Date__month__lte=month,).values_list('Suspect_Age', flat=True)

    victim_age_m = Tbl_pasig_incidents.objects.filter(Q(Victim_Sex='Male')& Q(Victim_Age__isnull=False),
                                Date__year__gte=year,Date__year__lte=year,
                                Date__month__gte=month,Date__month__lte=month,).values_list('Victim_Age', flat=True)

    age_combined_m = list(chain(suspect_age_m, victim_age_m))
    if not age_combined_m:
        age_combined_m.append(-1)

    age_total_m = child_m = adolescent_m = adult_m = geriatric_m = 0


    for child in range(0, 13):
        x = age_combined_m.count(child)
        child_m = child_m + x

    for adolescent in range(13, 20):
        x = age_combined_m.count(adolescent)
        adolescent_m = adolescent_m + x

    for adult in range(20, 60):
        x = age_combined_m.count(adult)
        adult_m = adult_m + x
    
    for geriatric in range(60, max(age_combined_m)+1):
        x = age_combined_m.count(geriatric)
        geriatric_m = geriatric_m + x

    age_total_m = child_m + adolescent_m + adult_m + geriatric_m 

    #AGE STATS - FEMALE - monthly
    suspect_age_f = []
    victim_age_f = []

    suspect_age_f = Tbl_pasig_incidents.objects.filter(Q(Suspect_Sex='Female') & Q(Suspect_Age__isnull=False), 
                                Date__year__gte=year,Date__year__lte=year,
                                Date__month__gte=month,Date__month__lte=month).values_list('Suspect_Age', flat=True)
    victim_age_f = Tbl_pasig_incidents.objects.filter(Q(Victim_Sex='Female') & Q(Victim_Age__isnull=False), 
                                Date__year__gte=year,Date__year__lte=year,
                                Date__month__gte=month,Date__month__lte=month).values_list('Victim_Age', flat=True)

    age_combined_f = list(chain(suspect_age_f, victim_age_f))
    if not age_combined_f:
        age_combined_f.append(-1)

    age_total_f = child_f = adolescent_f = adult_f = geriatric_f = 0


    for child in range(0, 13):
        x = age_combined_f.count(child)
        child_f += x

    for adolescent in range(13, 20):
        x = age_combined_f.count(adolescent)
        adolescent_f = adolescent_f + x

    for adult in range(20, 60):
        x = age_combined_f.count(adult)
        adult_f = adult_f + x
    
    for geriatric in range(60, max(age_combined_f)+1):
        x = age_combined_f.count(geriatric)
        geriatric_f = geriatric_f + x

    age_total_f = child_f + adolescent_f + adult_f + geriatric_f 
    
    #SEVERITY 
    suspect_severity = []
    victim_severity = []

    suspect_severity = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Suspect_Severity', flat=True)
    victim_severity = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,Date__year__lte=year,
                                    Date__month__gte=month,Date__month__lte=month,).values_list('Victim_Severity', flat=True)

    severity_combined = list(chain(suspect_severity, victim_severity))
    distinct_severity = set(severity_combined)
    severity_count = []
    severity_total = 0

    for severity in distinct_severity:
        x = severity_combined.count(severity)
        severity_count.append(x)
        severity_total += x

    #Day of the week 
    day_labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_count = []
    day_total = 0
    # day_list = Tbl_pasig_incidents.objects.all().values_list('Day', flat=True)
    
    
    for day in day_labels:
        # day_labels.append(day)
        x = Tbl_pasig_incidents.objects.filter(
                                    Date__year__gte=year,
                                    Date__year__lte=year,
                                    Date__month__gte=month,
                                    Date__month__lte=month,
                                    Day = day).count()                          
        day_count.append(x)
        day_total += x

    data = {
            'unread_notif_count': unread_notif_count,
            "month": month_label, "year":year_label,

            "district1_data": zip(d1_brgys, d1_brgys_count),
            "district1_labels": d1_brgys,
            "district1_count": d1_brgys_count,
            "d1_brgys_total":d1_brgys_total,

            "district2_data": zip(d1_brgys, d2_brgys_count),
            "district2_labels": d2_brgys,
            "district2_count": d2_brgys_count,
            "d2_brgys_total":d2_brgys_total,

            "offense_data": zip(offense_labels, offense_count),
            "offense_labels":offense_labels,
            "offense_count": offense_count,
            "offense_total": offense_total,

            "sex_labels": sex_labels,
            "sex_count": sex_count, 

            "time_count":time_count,
            
            "vehicle_data": zip(distinct_vehicles, vehicle_count),
            "vehicle_total": vehicle_total,

            "age_combined_m": age_combined_m,
            "age_total_m": age_total_m,
            "child_m": child_m,
            "adolescent_m": adolescent_m,
            "adult_m": adult_m,
            "geriatric_m": geriatric_m,

            "age_combined_f": age_combined_f,
            "age_total_f": age_total_f,
            "child_f": child_f,
            "adolescent_f": adolescent_f,
            "adult_f": adult_f,
            "geriatric_f": geriatric_f,
            "all": authorized, 
            "pub": pub,

            "severity_labels":distinct_severity,
            "severity_count":severity_count,
            "severity_data": zip(distinct_severity, severity_count),
            "severity_total": severity_total,

            "day_data": zip(day_labels, day_count),
            "day_labels": day_labels,
            "day_count": day_count,
            "day_total":day_total,
    }
    return render (request, 'monthly_summary/2018/january.html', data)


def get_monthly_generate(request, *args, **kwargs):
        select_month = request.POST.get('select_month')
        select_year = request.POST.get('select_year')

        #District 1
        d1_brgys = []
        d1_brgys_count = []
        d1_brgys_list = Tbl_barangay.objects.filter(District_id = '1').values_list('Barangay', flat=True)
        
        for brgy in d1_brgys_list:
            d1_brgys.append(brgy)
            x = Tbl_pasig_incidents.objects.filter(
                                        Date__year__gte=select_year,
                                        Date__year__lte=select_year,
                                        Date__month__gte=select_month,
                                        Date__month__lte=select_month,
                                        Barangay_id__Barangay = brgy).count()        
            d1_brgys_count.append(x)
        
        report_data = {
                "district1_labels": d1_brgys,
                "district1_count": d1_brgys_count,
            }
        return JsonResponse(report_data) 


def get_monthly_data(request, *args, **kwargs):

    if request.method == "GET":

        #District 1
        d1_brgys = []
        d1_brgys_count = []
        d1_brgys_list = Tbl_barangay.objects.filter(District_id = '1').values_list('Barangay', flat=True)
        
        for brgy in d1_brgys_list:
            d1_brgys.append(brgy)
            x = Tbl_pasig_incidents.objects.filter(
                                        Date__year__gte=today.year,
                                        Date__year__lte=today.year,
                                        Date__month__gte=today.month,
                                        Date__month__lte=today.month,
                                        Barangay_id__Barangay = brgy).count()        
            d1_brgys_count.append(x)

        monthly_data = {
                "district1_labels": d1_brgys,
                "district1_count": d1_brgys_count,
            }
        return JsonResponse(monthly_data) #http response

    if request.method == 'POST':
        select_month = request.POST.get('select_month')
        select_year = request.POST.get('select_year')

        #District 1
        d1_brgys = []
        d1_brgys_count = []
        d1_brgys_list = Tbl_barangay.objects.filter(District_id = '1').values_list('Barangay', flat=True)
        
        for brgy in d1_brgys_list:
            d1_brgys.append(brgy)
            x = Tbl_pasig_incidents.objects.filter(
                                        Date__year__gte=select_year,
                                        Date__year__lte=select_year,
                                        Date__month__gte=select_month,
                                        Date__month__lte=select_month,
                                        Barangay_id__Barangay = brgy).count()        
            d1_brgys_count.append(x)
        
        report_data = {
                "district1_labels": d1_brgys,
                "district1_count": d1_brgys_count,
            }

        serialized_data = json.dumps(report_data)
        # return HttpResponse(serialized_data)
        return render (request, 'monthly_summary/2018/january.html', {"serialized_data": serialized_data, "all": authorized, "pub": pub,})


def notification (request): 
   
    authorized = Tbl_add_members.objects.all()
    pub        = tbl_genpub_users.objects.all()

    cursor=connection.cursor()
    cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id")
    pasig_incident_list = cursor.fetchall()

    #for signup validation
    sign_up_validation = tbl_genpub_users.objects.all().order_by('-id')
    unread_notif_count_signup = tbl_genpub_users.objects.filter(Read_Status="No").count()

    
    if request.method   == "POST":
        searched        = request.POST['searched']
        pasig_public_reports     = Tbl_public_report.objects.filter(Q(User_ID__gen_fname__icontains = searched)|Q(User_ID__gen_surname__icontains = searched)|Q(Reported_Brgy__Barangay__icontains = searched)|Q(Reported_Narrative__icontains = searched)|Q(Reported_Location__icontains = searched)|Q(Report_Status__icontains = searched)).order_by('-id') 

        data = {
            'searched': searched,
            'pasig_incident_list': pasig_incident_list, 
            'public_reports_list': pasig_public_reports,
            'unread_notif_count': unread_notif_count,
            "all": authorized, 
            "pub": pub,
            'sign_up_validation': sign_up_validation,
            'unread_notif_count_signup':unread_notif_count_signup
        }

    else:
        pasig_public_reports = Tbl_public_report.objects.all().order_by('-id')
       
        data = {
            'pasig_incident_list': pasig_incident_list, 
            'public_reports_list': pasig_public_reports,
            'unread_notif_count': unread_notif_count,
            "all": authorized, 
            "pub": pub,
            'sign_up_validation': sign_up_validation,
            'unread_notif_count_signup':unread_notif_count_signup
        }
    return render (request, 'notification.html', data)


def notif_public_report_detail (request, gen_pub_report_id):
    
    member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
    investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
    substation_list = Tbl_substation.objects.all()

    unread_public_report = Tbl_public_report.objects.get(id=gen_pub_report_id)
    unread_public_report.Read_Status = "Yes"
    unread_public_report.save()
    
    #for gen pub reports inbox
    pasig_public_reports = Tbl_public_report.objects.all().order_by('-id')
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_info = Tbl_add_members.objects.get(id=auth_id)
            replies = Tbl_public_report_response.objects.filter(Q(Report_id=gen_pub_report_id)).filter(Q(Sender=auth_id)|Q(Receiver=auth_id)).order_by('Response_id') 
            pub_info = tbl_genpub_users.objects.all()
    except:
        pass

    

    data = {
        'public_reports_list': pasig_public_reports,
        'detail': unread_public_report,
        'unread_notif_count': unread_notif_count,
        'investigators_list': investigators_list,
        'substation_list': substation_list,

        'auth_info':auth_info,
        'pub_info':pub_info,
        'replies':replies,
        'admin_responses': replies,


        "all": authorized, 
        "pub": pub,
    }
    return render (request, 'notif_public_report_detail.html', data)

def processAssigning (request, report_id):
    investigator = request.POST.get('select-investigator')
    substation = request.POST.get('select-substation')
    public_report = Tbl_public_report.objects.get(id=report_id)

    public_report.Assigned_Investigator_id = investigator
    public_report.Substation_id = substation
    public_report.save()
    messages.success(request, "Your data has been saved!")
    return HttpResponseRedirect(reverse('notif_public_report_detail', args=(report_id,)))

def processAdmin_Reply (request, report_id):
    admin_reply = request.POST.get('admin_reply')
    sender = request.POST.get('sender_id')
    receiver = request.POST.get('receiver_id')


    admin_responses = Tbl_public_report_response.objects.create(
                    Sender_Type = 'Admin',
                    Sender    = sender,
                    Receiver = receiver,
                    Response  = admin_reply,
                    Report_id = report_id, )

    admin_responses.save()
    return HttpResponseRedirect(reverse('notif_public_report_detail', args=(report_id,)))


def sub_notification (request):
    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            subrep_row = Tbl_add_members.objects.get(id=auth_id)

            fwd_reports = Tbl_public_report.objects.filter(Substation_id = subrep_row.Members_Substation_id)    
            unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = subrep_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()
            
    except:
        pass

    context    = {
        "unread_notif_count":unread_notif_count,
        "fwd_reports": fwd_reports,
        "all": authorized,
        "pub": pub,
    }
    return render (request, 'sub_notification.html', context)

def sub_notification_detail (request, report_id):
    try:
        if request.session['authorized_id']:
            detail = Tbl_public_report.objects.get(id=report_id)
            detail.Read_by_subrep = 'Yes'
            detail.save()

            auth_id = request.session['authorized_id']
            subrep_row = Tbl_add_members.objects.get(id=auth_id)
            fwd_reports = Tbl_public_report.objects.filter(Substation_id = subrep_row.Members_Substation_id)
            unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = subrep_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

    except:
        pass

    context    = {
        "unread_notif_count":unread_notif_count,
        "fwd_reports": fwd_reports,
        "detail": detail,
        "all": authorized,
        "pub": pub,
    }
    return render (request, 'sub_notification_detail.html', context)

#subrep to admin messages    
def processSubrep_Reply (request, report_id):
    public_reply = request.POST.get('public_reply')
    sender = request.POST.get('sender_id')
    receiver = request.POST.get('receiver_id')

    public_responses = Tbl_public_report_response.objects.create(
                    Sender_Type = 'Public',
                    Sender    = sender,
                    Receiver = receiver,
                    Response  = public_reply,
                    Report_id = report_id, )

    public_responses.save()
    messages.success(request, ("Message Successfully Sent!"))
    return HttpResponseRedirect(reverse('public_inbox_detail', args=(report_id,)))

#inbox
def public_inbox (request):
    
    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            pub_inbox = Tbl_public_report.objects.filter(User_ID=pub_id) #list ng reports nya
            pub_info = tbl_genpub_users.objects.get(id=pub_id)

            admin_replies = Tbl_public_report_response.objects.filter(Receiver=pub_id).order_by('-Response_id') 
            admin_info = Tbl_add_members.objects.all()
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except:
        pass

    context    = {
        "all": authorized,
        "pub": pub,
        "unread_notif_count":unread_notif_count,

        "pub_inbox":pub_inbox,
        "pub_info":pub_info,
        "admin_replies":admin_replies,
        "admin_info":admin_info,

    }
    return render (request, 'gen_inbox.html', context)

#inbox
def public_inbox_detail (request, report_id):
    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except: pass

    admin_info = Tbl_add_members.objects.all()

    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            pub_inbox = Tbl_public_report.objects.filter(User_ID=pub_id) #list ng reports nya
            pub_info = tbl_genpub_users.objects.get(id=pub_id)
            prev_report = Tbl_public_report.objects.get(id=report_id)

            replies = Tbl_public_report_response.objects.filter(Q(Report_id=report_id)).filter(Q(Sender=pub_id)|Q(Receiver=pub_id)).order_by('Response_id') 
            replies.update(Read_Status = "Yes")

    except:
        pass

    context    = {
        "all": authorized,
        "pub": pub,
        "unread_notif_count": unread_notif_count,

        "pub_inbox":pub_inbox,
        "pub_info":pub_info,
        "prev_report": prev_report,
        "replies":replies,
        "admin_info":admin_info,

    }
    return render (request, 'gen_inbox_detail.html', context)

#public to admin messages    
def processPublic_Reply (request, report_id):
    public_reply = request.POST.get('public_reply')
    sender = request.POST.get('sender_id')
    receiver = request.POST.get('receiver_id')

    public_responses = Tbl_public_report_response.objects.create(
                    Sender_Type = 'Public',
                    Sender    = sender,
                    Receiver = receiver,
                    Response  = public_reply,
                    Report_id = report_id, )

    public_responses.save()
    messages.success(request, ("Message Successfully Sent!"))
    return HttpResponseRedirect(reverse('public_inbox_detail', args=(report_id,)))


def archiving (request, incident_id):
    try:
        incident_detail=Tbl_pasig_incidents.objects.get(id=incident_id)
        incident_detail.archive="Yes"
        incident_detail.save()
        messages.success(request, ("Incident Successfully Archived!"))

        return HttpResponseRedirect('/unsolvedcases')
    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")

def unarchiving (request, incident_id):
    try:
        incident_detail=Tbl_pasig_incidents.objects.get(id=incident_id)
        incident_detail.archive="No"
        incident_detail.save()
        messages.success(request, ("Incident Successfully Unarchived!"))

        return HttpResponseRedirect('/unsolvedcases')
    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")   


def unsolved_cases (request):
    member_type=Tbl_member_type.objects.get(Member_Type="Investigator")
    investigator_list=Tbl_add_members.objects.filter(Members_User_id=member_type.id)
    level1_range=date.today()-timedelta(31)
    level2_range_gte=date.today()-timedelta(186)
    level2_range_lte=date.today()-timedelta(31)
    
    level3_range_lte=date.today()-timedelta(186)
    level3_range_gte=date.today()-timedelta(372)

    archive_range=date.today()-timedelta(372)
    unsolveds_cases_list=Tbl_pasig_incidents.objects.filter(Case_Status="Unsolved")
    level1=Tbl_pasig_incidents.objects.filter(Q(Date__gte=level1_range),Q(archive="No")|Q(archive__isnull=True),Case_Status="Unsolved")
    level2=Tbl_pasig_incidents.objects.filter(Q(Date__gte=level2_range_gte)&Q(Date__lte=level2_range_lte),Q(archive="No")|Q(archive__isnull=True),Case_Status="Unsolved")
    level3=Tbl_pasig_incidents.objects.filter(Q(Date__gte=level3_range_gte)&Q(Date__lte=level3_range_lte),Q(archive="No")|Q(archive__isnull=True),Case_Status="Unsolved")
    level4=Tbl_pasig_incidents.objects.filter(Q(Date__lt=archive_range),Q(archive="No")|Q(archive__isnull=True),Case_Status="Unsolved",)
    archive=Tbl_pasig_incidents.objects.filter(Q(Case_Status="Unsolved") & Q(archive="Yes"))
    data = {
        "investigator_list":investigator_list,
        "unsolveds_cases_list":unsolveds_cases_list,
        "level1":level1,
        "level2":level2,
        "level3":level3,
        "level4":level4,
        "archive":archive,
        "all": authorized,
        "pub": pub,
        'unread_notif_count': unread_notif_count,
    }
    return render (request, 'unsolved_cases.html', data)

def processDeleteUnsolved (request, incident_id):
    Tbl_pasig_incidents.objects.filter(id=incident_id)
    messages.success(request, ("Successfully Deleted!"))
    return HttpResponseRedirect('/incidents/view')

def logout (request):
    return render (request, 'logout.html')

#PUBLIC
def submit_report (request):
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    
    try:
        if request.method == "GET":
            if request.session['public_id']:
                pub_id = request.session['public_id']
                unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()

            context    = {
                "all": authorized,
                "pub": pub,
                "unread_notif_count":unread_notif_count
            }
            return render (request, 'submit_report.html', context) #Load view

        user_id = request.POST.get('user_id')
        city = request.POST.get('city')
        barangay = request.POST.get('Barangay')
        district = request.POST.get('district')
        address = request.POST.get('address')
        along = request.POST.get('along')
        corner = request.POST.get('corner')
        latitude = request.POST.get('lat')
        longitude = request.POST.get('lon')
        narrative = request.POST.get('narrative')
        recipient = "Admin"

        if request.FILES.get('image'):
            image_proof = request.FILES.get('image')

        incident_report = Tbl_public_report.objects.create(
                        User_ID_id = user_id,
                        Reported_City=city, 
                        Reported_Brgy_id=barangay,               
                        Reported_District=district,   
                        Reported_Location=address,               
                        Reported_Along=along,
                        Reported_Corner=corner, 
                        Reported_Latitude = latitude,
                        Reported_Longitude = longitude,
                        Reported_Narrative = narrative,
                        Reported_Image_Proof = image_proof,
                        Report_Status = 'Unsolved',
                        Read_Status='No',
                        Recipient = recipient,
                        )
        
        incident_report.save()

        try:
            if request.session['public_id']:
                pub_id = request.session['public_id']
                unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
        
        except: pass
        context = {
            'success_message':"Your report has been submitted!",
            "all": authorized, 
            "pub": pub,
            "unread_notif_count":unread_notif_count,

        }
        return render (request, 'submit_report.html', context)

    except:
        image_proof = request.FILES['image']
        
        if not image_proof.name.endswith('.png'| '.jpg'| '.jpeg'):
            messages.error(request, 'Error: Invalid Image Format')

        context = {
            'error_message': "Error sending report!",
            "all": authorized, 
            "pub": pub,
        }

        return render (request, 'submit_report.html', context)



# Dane's Codes
def pub_notif_inbox (request): #Account settings
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    try:
        if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()

    except:
        pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass


    authorized  = Tbl_add_members.objects.all()  
    pub         = tbl_genpub_users.objects.all()
    barangay    = Tbl_barangay.objects.all()

    context     = {
        "all": authorized,
        "pub": pub,
        "barangay": barangay,
        "unread_notif_count":unread_notif_count,
    }
    return render(request, 'public_notif_setting.html', context)

def change_account (request, prof_id): #Change email or password for gen pub and members - settings
    
    if request.method       == "POST":
        try:
            if get_object_or_404(tbl_genpub_users, id = prof_id):
                pub                     = get_object_or_404(tbl_genpub_users, id = prof_id)
            
                gen_username        = request.POST.get("gen_username")
                gen_pass            = request.POST.get("gen_pass")

                if (tbl_genpub_users.objects.filter(gen_username = gen_username) & tbl_genpub_users.objects.exclude(id = prof_id)):
                    messages.success(request, ("Oops! That account already exists. Please make sure your email address is unique."))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))
                elif (Tbl_add_members.objects.filter(Members_Email = gen_username)):
                    messages.success(request, ("Oops! That account already exists. Please make sure your email address is unique."))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))
                else:
                    pub                     = get_object_or_404(tbl_genpub_users, id = prof_id)
                    pub.gen_username        = gen_username
                    pub.gen_pass            = gen_pass

                    pub.save()
                    messages.success(request, ("Changes saved!"))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))

        except:
            if get_object_or_404(Tbl_add_members, id = prof_id):
                gen                     = get_object_or_404(Tbl_add_members, id = prof_id)

                Members_Email       = request.POST.get("Members_Email")
                Members_Username    = request.POST.get("Members_Username")
                Members_Password    = request.POST.get("Members_Password")

                if (Tbl_add_members.objects.filter(Members_Email = Members_Email) & Tbl_add_members.objects.exclude(id = prof_id)) | (Tbl_add_members.objects.filter(Members_Username = Members_Username) & Tbl_add_members.objects.exclude(id = prof_id)):
                    messages.success(request, ("Oops! That account already exists. Please make sure your email address is unique."))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))
                elif (tbl_genpub_users.objects.filter(gen_username = Members_Email)):
                    messages.success(request, ("Oops! That account already exists. Please make sure your email address is unique."))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))
                else:
                    gen                     = get_object_or_404(Tbl_add_members, id = prof_id)
                    gen.Members_Email       = Members_Email
                    gen.Members_Username    = Members_Username
                    gen.Members_Password    = Members_Password

                    gen.save()
                    messages.success(request, ("Changes saved!"))
                    return HttpResponseRedirect(reverse('pub_notif_inbox'))


def add_members (request):
    departments     = Tbl_add_departments.objects.all()
    members         = Tbl_add_members.objects.all()
    substations     = Tbl_substation.objects.all()
    membertypes     = Tbl_member_type.objects.all()
    positions       = Tbl_position.objects.all()
    all_authorized  = Tbl_add_members.objects.all()  
    pub             = tbl_genpub_users.objects.all() 

    context         = {
        'departments': departments,
        'members': members,
        'substations': substations,
        'membertypes': membertypes,
        'positions': positions,
        'all': all_authorized,
        'pub': pub,
         "unread_notif_count":unread_notif_count,
    }
    return render (request, 'add_members.html', context)

def duplicate_members (request): #For checking of duplicates and saving members - add_members
    if request.method       == "POST":
        departments_id      = request.POST["Members_Dept"]
        Members_Dept        = Tbl_add_departments.objects.get( id = departments_id)

        substations_id      = request.POST["Members_Substation"]
        Members_Substation  = Tbl_substation.objects.get( id = substations_id)

        positions_id        = request.POST["Members_Position"]
        Members_Position    = Tbl_position.objects.get( id = positions_id)

        membertypes_id      = request.POST["Members_User"]
        Members_User        = Tbl_member_type.objects.get( id = membertypes_id)

        Members_District    = request.POST["Members_District"].title()
        Members_Fname       = request.POST["Members_Fname"].title()
        Members_Lname       = request.POST["Members_Lname"].title()
        Members_Email       = request.POST["Members_Email"]
        Members_Username    = request.POST["Members_Username"]
        Members_Password    = request.POST["Members_Password"]
        Added_By            = request.POST["Added_By"]

        if request.FILES.get("Members_Pic"):
            Members_Pic     = request.FILES.get('Members_Pic')
        else:
            Members_Pic     = 'Profile/default.jpg'

    try:
        if (Tbl_add_members.objects.filter(Members_Email = Members_Email) | Tbl_add_members.objects.filter(Members_Username = Members_Username)):
            messages.success(request, ("Oops! That account already exists. Please make sure your email address and username is unique."))
            return HttpResponseRedirect(reverse('add_members'))

        elif (tbl_genpub_users.objects.filter(gen_username = Members_Email)):
            messages.success(request, ("Oops! That account has already been registered by a general public user. Please make sure your email address is unique."))
            return HttpResponseRedirect(reverse('add_members'))

        else:
            submit = Tbl_add_members.objects.create(Members_Dept = Members_Dept, Members_User = Members_User, Members_Substation = Members_Substation, Members_District = Members_District, 
            Members_Fname = Members_Fname, Members_Lname = Members_Lname, Members_Position = Members_Position, Members_Email = Members_Email, Members_Username = Members_Username,
            Members_Password = Members_Password, Members_Pic = Members_Pic, Added_By = Added_By)
            submit.save()
            messages.success(request, ("You've added a new member!"))
            return HttpResponseRedirect(reverse('admin_list_members'))

    except (KeyError, Tbl_add_members.DoesNotExist):
        submit = Tbl_add_members.objects.create(Members_Dept = Members_Dept, Members_User = Members_User, Members_Substation = Members_Substation, Members_District = Members_District, 
        Members_Fname = Members_Fname, Members_Lname = Members_Lname, Members_Position = Members_Position, Members_Email = Members_Email, Members_Username = Members_Username,
        Members_Password = Members_Password, Members_Pic = Members_Pic, Added_By = Added_By)
        submit.save()
        messages.success(request, ("You've added a new member!"))
        return HttpResponseRedirect(reverse('admin_list_members'))

def add_dept (request):
    departments     = Tbl_add_departments.objects.raw('SELECT * FROM roadcast_Tbl_add_departments ORDER BY id DESC')

    context = {
    'departments': departments,
    'all': authorized,
    'pub': pub,
     "unread_notif_count":unread_notif_count,
    }

    paginator = Paginator(departments, 10) 
    page_number = request.GET.get('page')
    departments = paginator.get_page(page_number)

    return render (request, 'add_dept.html', context)

def duplicate(request): #For checking of duplicates and saving - add_dept
    Dept_Dept       = request.POST["Dept_Dept"].title()

    try:
        n = Tbl_add_departments.objects.get(Dept_Dept = Dept_Dept)
        messages.success(request, ("Oops! That department already exists. Please enter a different department."))
        return HttpResponseRedirect(reverse('add_dept'))

    except ObjectDoesNotExist:
        submit = Tbl_add_departments.objects.create(Dept_Dept = Dept_Dept)
        submit.save()
        messages.success(request, ("You've added a new department!"))
        return HttpResponseRedirect(reverse('admin_list_departments'))
        
def admin_list_departments(request): #Show list of depaartments
    departments         = Tbl_add_departments.objects.all()

    if request.method   == "POST":
        searched        = request.POST['searched']
        departments     = Tbl_add_departments.objects.filter(Dept_Dept__icontains = searched).order_by('-id') 
        return render (request, 'admin_list_departments.html', {'departments': departments, 'searched': searched, "all": authorized, "pub": pub})

    else:
        departments      = Tbl_add_departments.objects.raw('SELECT * FROM roadcast_Tbl_add_departments ORDER BY id DESC')

        paginator = Paginator(departments, 10) 
        page_number = request.GET.get('page')
        departments = paginator.get_page(page_number)

        return render (request, 'admin_list_departments.html', {'departments': departments, "all": authorized, "pub": pub})

def view_members(request, member_id): #Show specific profile of members 
    members     = Tbl_add_members.objects.get(id = member_id)
    return render (request, 'view_members.html', {'members':members, "all": authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})

def edit_members(request, member_id): 
    members     = Tbl_add_members.objects.get(id = member_id)
    departments = Tbl_add_departments.objects.exclude(Dept_Dept = members.Members_Dept)
    substations = Tbl_substation.objects.exclude(Substation = members.Members_Substation)
    membertypes = Tbl_member_type.objects.exclude(Member_Type = members.Members_User)
    positions   = Tbl_position.objects.exclude(Position = members.Members_Position)

    context = {
        'departments': departments,
        'members': members,
        'substations': substations,
        'membertypes': membertypes,
        'positions': positions,
        "all": authorized, 
        "pub": pub,
        'unread_notif_count': unread_notif_count,
    }
    return render (request, 'edit_members.html', context)


def update_members(request, member_id): #For updating the data and checking for duplicates - edit_members
    members                 = get_object_or_404(Tbl_add_members, id = member_id)
    Members_Pic             = request.FILES.get('Members_Pic')

    if request.method       == 'POST':
        departments_id      = request.POST["Members_Dept"]
        Members_Dept        = Tbl_add_departments.objects.get( id = departments_id)

        substations_id      = request.POST["Members_Substation"]
        Members_Substation  = Tbl_substation.objects.get( id = substations_id)

        positions_id        = request.POST["Members_Position"]
        Members_Position    = Tbl_position.objects.get( id = positions_id)

        membertypes_id      = request.POST["Members_User"]
        Members_User        = Tbl_member_type.objects.get( id = membertypes_id)

        Members_District    = request.POST['Members_District'].title()
        Members_Fname       = request.POST['Members_Fname'].title()
        Members_Lname       = request.POST['Members_Lname'].title()
        Members_Email       = request.POST['Members_Email']
        Members_Username    = request.POST['Members_Username']
        Members_Password    = request.POST['Members_Password']
        Edit_By             = request.POST['Edit_By']
        Date_Edit           = datetime.datetime.now()

        if request.FILES.get("Members_Pic"):
            Members_Pic     = request.FILES.get('Members_Pic')

    try:
        if (Tbl_add_members.objects.filter(Members_Email = Members_Email) & Tbl_add_members.objects.exclude(id = member_id)) | (Tbl_add_members.objects.filter(Members_Username = Members_Username) & Tbl_add_members.objects.exclude(id = member_id)):
            messages.success(request, ("Oops! That account already exists. Please make sure your email address and username is unique."))
            return HttpResponseRedirect(reverse('admin_list_members'))

        elif (tbl_genpub_users.objects.filter(gen_username = members.Members_Email)):
            messages.success(request, ("Oops! That account has already been registered by a general public user. Please make sure your email address is unique."))
            return HttpResponseRedirect(reverse('admin_list_members'))

        else:
            members                     = Tbl_add_members.objects.get(id = member_id)
            members.Members_Dept        = Members_Dept
            members.Members_Substation  = Members_Substation
            members.Members_District    = Members_District
            members.Members_Fname       = Members_Fname
            members.Members_Lname       = Members_Lname
            members.Members_User        = Members_User
            members.Members_Position    = Members_Position
            members.Members_Email       = Members_Email
            members.Members_Password    = Members_Password
            members.Edit_By             = Edit_By
            members.Date_Edit           = Date_Edit

            if Members_Pic:
                members.Members_Pic     = Members_Pic

            members.save()
            messages.success(request, ("Changes saved."))
            return HttpResponseRedirect(reverse('admin_list_members'))
            
    except (KeyError, Tbl_add_members.DoesNotExist):
            messages.success(request, ("Oops! There was a problem updating the details. Please try again."))
            return HttpResponseRedirect(reverse('admin_list_members'))  

def edit_dept(request, dept_id):
    departments         = Tbl_add_departments.objects.get(id = dept_id)
    return render (request, 'edit_dept.html', {'departments': departments, "all": authorized, "pub": pub,'unread_notif_count': unread_notif_count,})


def update_dept(request, dept_id): #For saving the data - edit_dept
    departments         = Tbl_add_departments.objects.get(id = dept_id)

    if request.method   == 'POST':
        Dept_Dept       = request.POST['Dept_Dept'].title()

    try:
        if (Tbl_add_departments.objects.filter(Dept_Dept = Dept_Dept) & Tbl_add_departments.objects.exclude(id = dept_id)):
            messages.error(request, ("Oops! That department already exists. Please enter a different department."))
            return HttpResponseRedirect(reverse('admin_list_departments')) 
        else:  
            departments.Dept_Dept = Dept_Dept
            departments.save()
            messages.success(request, ("Changes saved."))
            return HttpResponseRedirect(reverse('admin_list_departments')) 
    except (KeyError, Tbl_add_departments.DoesNotExist):
            departments.Dept_Dept = Dept_Dept
            departments.save()
            messages.success(request, ("Changes saved."))
            return HttpResponseRedirect(reverse('admin_list_departments'))    

def delete_member(request, member_id):
    Tbl_add_members.objects.filter(id = member_id).delete()
    messages.success(request, ("Member successfully deleted."))
    return HttpResponseRedirect(reverse('admin_list_members')) 

def delete_dept(request, dept_id):
    Tbl_add_departments.objects.filter(id = dept_id).delete()
    messages.success(request, ("Department successfully deleted."))
    return HttpResponseRedirect(reverse('admin_list_departments'))  

def user_profile(request): #Profile of users
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    try:
        if request.session['public_id']:
                pub_id = request.session['public_id']
                unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()
    except:
        pass

    try:
        if request.session['authorized_id']:
            auth_id = request.session['authorized_id']
            auth_row = Tbl_add_members.objects.get(id=auth_id)
            if (auth_row.Members_User_id == 3):
                unread_notif_count = Tbl_public_report.objects.filter(Q(Substation_id = auth_row.Members_Substation_id)&Q(Read_by_subrep="No")).count()

            if (auth_row.Members_User_id == 1):
                unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()
    except:
        pass

    context    = {
        "all": authorized,
        "pub": pub,
        'unread_notif_count': unread_notif_count,
    }
    return render(request, 'user_profile.html', context)


def edit_profile(request, prof_id): #Edit user profile details #*
    if request.session['public_id']:
            pub_id = request.session['public_id']
            unread_notif_count = Tbl_public_report_response.objects.filter(Q(Receiver=pub_id)& Q(Read_Status="No")).order_by('-Response_id').count()

    gen                 = tbl_genpub_users.objects.get(id = prof_id)

    #Functions for profile ek ek
    username            = gen.gen_username.split('@')[0] 
    fname               = gen.gen_fname.split(' ')[0]
    today               = date.today()
    age                 = today.year - gen.gen_bday.year - ((today.month, today.day) < (gen.gen_bday.month, gen.gen_bday.day))

    context = {
        'gen': gen, 
        'username': username, 
        'fname': fname,
        'age': age,
        "all": authorized,
        "pub": pub,
        "unread_notif_count": unread_notif_count

    }
    return render(request, 'edit_profile.html', context)
    

def update_profile(request, prof_id): #For saving and validating public emails - edit_profile (gen pub)
    pub                     = get_object_or_404(tbl_genpub_users, id = prof_id)

    if request.method       == "POST":
        gen_fname           = request.POST["gen_fname"].title()
        gen_surname         = request.POST["gen_surname"].title()
        gen_bday            = request.POST["gen_bday"]
        gen_sex             = request.POST["gen_sex"].title()
        gen_contact_no      = request.POST["gen_contact_no"]
        gen_region          = request.POST["gen_region"].title()
        gen_province        = request.POST["gen_province"].title()
        gen_city            = request.POST["gen_city"].title()
        gen_barangay        = request.POST["gen_barangay"].title()
        gen_profile         = request.FILES.get('gen_profile')
        date_edit           = datetime.datetime.now()

        pub.gen_fname           = gen_fname
        pub.gen_surname         = gen_surname
        pub.gen_bday            = gen_bday
        pub.gen_sex             = gen_sex
        pub.gen_contact_no      = gen_contact_no
        pub.gen_region          = gen_region
        pub.gen_province        = gen_province
        pub.gen_city            = gen_city
        pub.gen_barangay        = gen_barangay
        pub.date_edit           = date_edit

        if request.FILES.get("gen_profile"):
            pub.gen_profile     = gen_profile

        pub.save()
        messages.success(request, ("Changes saved."))
        return HttpResponseRedirect(reverse('user_profile'))

def admin_list_members(request): #Show list of ALL the members (excluding gen pub)
    members = Tbl_add_members.objects.all()

    if request.method == "POST":
        searched      = request.POST['searched']
        members       = Tbl_add_members.objects.filter(Members_Fname__icontains = searched).order_by('-id') | Tbl_add_members.objects.filter(Members_Lname__icontains = searched).order_by('-id') | Tbl_add_members.objects.filter(Members_User__Member_Type__icontains = searched).order_by('-id') 

        paginator = Paginator(members, 10) 
        page_number = request.GET.get('page')
        members = paginator.get_page(page_number)

        return render (request, 'admin_list_members.html', {'members': members, 'searched': searched, "all": authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})
    else:
        members       = Tbl_add_members.objects.raw('SELECT * FROM roadcast_Tbl_add_members ORDER BY id DESC')

        paginator = Paginator(members, 10) 
        page_number = request.GET.get('page')
        members = paginator.get_page(page_number)

        return render (request, 'admin_list_members.html', {'members': members, "all": authorized, "pub": pub, 'unread_notif_count': unread_notif_count,}) 

def admin_investigators(request): #Show list of investigators
    members           = Tbl_add_members.objects.all().order_by('-id') 

    if request.method == "POST":
        searched      = request.POST['searched']
        members       = Tbl_add_members.objects.filter(Members_Fname__icontains = searched).order_by('-id')  | Tbl_add_members.objects.filter(Members_Lname__icontains = searched).order_by('-id') 
        
        return render (request, 'admin_investigators.html', {'members': members, 'searched': searched, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})
    else:
        return render (request, 'admin_investigators.html', {'members': members, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})
  
def admin_view_investigators(request, member_id): #Viewing specific investigator profile
    members           = Tbl_add_members.objects.get(id = member_id)

    return render (request, 'admin_view_investigators.html', {'members': members, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,}) 


# Audit trail 
def admin_audit_members(request): #List of audit for members
    members           = Tbl_add_members.objects.all()

    if request.method == "POST":
        searched      = request.POST['searched']
        audits        = tbl_audit.objects.filter(username__icontains = searched).order_by('-id') | tbl_audit.objects.filter(date_logged_in__icontains = searched).order_by('-id')
        return render (request, 'admin_audit_trail_members.html', {'audits': audits, 'members': members, 'searched': searched, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})
    else:
        audits        = tbl_audit.objects.all().order_by('-id')
        return render (request, 'admin_audit_trail_members.html', {'audits': audits, 'members': members, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})

def audit_members(request, audit_id): #Specific view for members
    audits  = tbl_audit.objects.get(id = audit_id)

    info    = Tbl_add_members.objects.get(Members_Email = audits.username)
    return render (request, 'audit_member.html', {'audits': audits, 'info': info, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,}) 

def admin_audit_genpub(request): #List of audit for gen pub
    public  = tbl_genpub_users.objects.all().order_by('-id')

    if request.method == "POST":
        searched      = request.POST['searched']
        audits        = tbl_audit.objects.filter(username__icontains = searched).order_by('-id') | tbl_audit.objects.filter(date_logged_in__icontains = searched).order_by('-id')

        return render (request, 'admin_audit_trail_genpub.html', {'audits': audits, 'public': public, 'searched': searched, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})
    else:
        audits = tbl_audit.objects.all().order_by('-id')

        return render (request, 'admin_audit_trail_genpub.html', {'audits': audits, 'public': public, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,})

def audit_genpub(request, audit_id): #Specific view for gen pub
    audits  = tbl_audit.objects.get(id = audit_id)
    info    = tbl_genpub_users.objects.get(gen_username = audits.username)

    return render (request, 'audit_genpub.html', {'audits': audits, 'info': info, 'all':authorized, "pub": pub, 'unread_notif_count': unread_notif_count,}) 


#Navbar for all
def navbar (request):
    audit      = tbl_audit.objects.all()

    context    = {
        "all": authorized,
        "pub": pub,
        "audit": audit,
    }
    return render(request, 'nav_admin.html', context)

#Bagong dagdag 
def error_page (request): #403
    context    = {
        "all": authorized,
        "pub": pub,
    }
    return render(request, '403.html', context)

def no_page (request, exception): #404
    context    = {
        "all": authorized,
        "pub": pub,
    }
    return render(request, '404.html', context)

def server_error (request): #500
    return render(request, '500.html', status=500)