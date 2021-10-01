from django.shortcuts import render, get_object_or_404, reverse #get_object_or_404 & reverse for processEdit
from .models import Tbl_add_members, Tbl_member_type, Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report, Tbl_substation, tbl_audit, tbl_genpub_users, Tbl_forecast, Tbl_public_report_response
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
from django.utils import timezone

from django.db.models import Avg
import datetime
from urllib.parse import urlencode
import requests
from django.core.paginator import Paginator 

today = date.today()

def index(request): #landing/home
    return render (request, 'landing.html')

def login_f8(request):
    try:
        #landing ng login / wala pang process
        if request.method =="GET":
            return render(request, 'login.html') 

        #start na if may process / nag login na si user

        gen_pub_list = tbl_genpub_users.objects.all()
        authorized_list = Tbl_add_members.objects.all()

        username = request.POST.get('username')
        password = request.POST.get('password')

        count_gen = tbl_genpub_users.filter(gen_username=username, gen_pass= password)
        count_authorized = Tbl_add_members.filter(Members_Email=username, Members_Password = password)

        if count_gen and count_authorized is not None:
            context = {
                    'count_gen':count_gen,
                    'count_authorized': count_authorized,
                }

            return render (request, 'login.html', context)

    
    #ito if may error sa process ni user :)
    except:
        messages.success(request, ("Oops! Please check your email or password"))
        return render(request, 'login.html')



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

                return HttpResponseRedirect('/dashboard')
            else: 
                messages.success(request, ("Oops! Please check your email or password"))
                return render(request, 'login.html')
            
        if b:
            if (public.gen_username == username) and (public.gen_pass == password):
                submit = tbl_audit(username = username, password = password)
                submit.save()

                public_session = tbl_genpub_users.objects.get(gen_username=username, gen_pass= password)

                request.session['public_id'] = public_session.id

                return HttpResponseRedirect('/dashboard')
            else: 
               messages.success(request, ("Oops! Please check your email or password"))
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
    return render (request, 'about_us.html') 

def contact_us(request):
    return render (request, 'contact_us.html') 

def contact_no(request):
    return render (request, 'contact_no.html') 

def sign_up (request):
    return render (request, 'sign_up.html')
    
def duplicate_gen (request): #Jew
    if request.method=="POST": #save data when button is clicked
        gen_surname = request.POST["gen_surname"].title()
        gen_fname = request.POST["gen_fname"].title()
        gen_sex = request.POST["gen_sex"]
        gen_bday = request.POST["gen_bday"]
        gen_region = request.POST["gen_region"].title()
        gen_province = request.POST["gen_province"].title()
        gen_city = request.POST["gen_city"].title()
        gen_barangay = request.POST["gen_barangay"].title()
        gen_contact_no = request.POST["gen_contact_no"]
        gen_username = request.POST["gen_username"]
        gen_pass = request.POST["gen_pass"]
        gen_valid_id = request.POST["gen_valid_id"]
        gen_upload_id = request.POST["gen_valid_id"]

        #save image to database 
        if request.FILES.get("gen_upload_id"):
            gen_upload_id = request.FILES.get('gen_upload_id')
        else:
            gen_upload_id = 'Public/default.png'

        # members = tbl_genpub_users.objects.get(gen_username = gen_username)
        # print(members)
        if tbl_genpub_users.objects.filter(gen_username = gen_username):
            # context = {'error': 'error yern, alreay reg'}
            messages.success(request, ("Oops! That email address is already taken. Please use a different one."))
            return render(request, 'sign_up.html')  

        if Tbl_add_members.objects.filter(Members_Email=gen_username):
            messages.success(request, ("Oops! That email address is already taken. Please use a different one."))
            return HttpResponseRedirect('signup')

        submit = tbl_genpub_users.objects.create(gen_surname = gen_surname,gen_fname = gen_fname, gen_sex = gen_sex, gen_bday=gen_bday, gen_region = gen_region, gen_province = gen_province, gen_city = gen_city,
        gen_barangay = gen_barangay, gen_contact_no = gen_contact_no, gen_username = gen_username, gen_pass = gen_pass, gen_valid_id = gen_valid_id,gen_upload_id=gen_upload_id )#,gen_upload_id=gen_upload_id
        submit.save()
        # return redirect(request, 'login.html')  
        return HttpResponseRedirect(reverse('login'))
        # return HttpResponseRedirect('/incidents/view')
    return render(request, 'sign_up.html')
            
def success(request):
    return render(request, 'submit_success.html')

def sign_up_validation (request): #Jew
    list = tbl_genpub_users.objects.all()
    context={'list':list}
    return render (request, 'sign_up_validation.html',context)

def admin_audit_trail(request):
    return render (request, 'admin_audit_trail.html')  

def admin_list_members(request):
    return render (request, 'admin_list_members.html') 

def admin_departments(request):
    return render (request, 'admin_list_members.html')   

def admin_investigators(request):
    return render (request, 'admin_investigators.html')  

def admin_view_investigators(request):
    return render (request, 'admin_view_investigators.html')  


def is_valid(param):
    return param != "" and param is not None
def is_not_valid(param):
    return param == "" and param is None

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


class DashboardView (View):
   
    def get(self, request, *args, **kwargs):

        # FOR FORECASTING
        # today = date.today() 

        # earliest_day= Tbl_pasig_incidents.objects.all().order_by("Date")[0].Date
        
        # a_week= date(2019,1,1)
        # test=date.today() + timedelta(7)

        # end_date=date(2019,2,28)+ timedelta(7)
        # forecast_query_set= Tbl_pasig_incidents.objects.filter(Date__gte=earliest_day, Date__lte=a_week).count()
        # limit = Tbl_forecast.objects.all().count()
        # start_i=0
        # end_i=7
        # i_day=6
        # count=0
        # for insert_date in daterange(earliest_day,test):

        #     date_exist=Tbl_forecast.objects.filter(Date=insert_date,).exists()


        #     if not date_exist:
        #         incident_count=Tbl_pasig_incidents.objects.filter(Date=insert_date).count()
        #         create= Tbl_forecast.objects.create(Date=insert_date.strftime("%Y-%m-%d"), Incidents=incident_count, Averages=0)
        #     else:
        #         incident_count=Tbl_pasig_incidents.objects.filter(Date=insert_date).count()
        #         create= Tbl_forecast.objects.filter(Date=insert_date.strftime("%Y-%m-%d")).update(Incidents=incident_count)

        #         while i_day < limit:
        #             count_avg=Tbl_forecast.objects.all().order_by('Date')[start_i:end_i].aggregate(Avg('Incidents'))
        #             nth=Tbl_forecast.objects.all().order_by('Date')[i_day]
        #             insert=Tbl_forecast.objects.filter(Date=nth.Date).update(Averages=count_avg['Incidents__avg'])
        #             start_i += 1
        #             end_i += 1
        #             i_day += 1 #may mali dito di gumagana yung iteration
        # END OF FORECASTING

        all_total = Tbl_pasig_incidents.objects.count()

        
        yesterday = today - timedelta(days=1)
        year, week_num, day_of_week =  date.today().isocalendar()

        this_week = Tbl_pasig_incidents.objects.filter(Date__year__gte=today.year, Date__year__lte=today.year, Date__week=week_num,).count()
        yesterday_total = Tbl_pasig_incidents.objects.filter(Date__gte = yesterday, Date__lt = today).count()
        this_day = Tbl_pasig_incidents.objects.filter(Date__gte = today, Date__lte = today, Date__year__gte=today.year, Date__year__lte=today.year).count()


        all_authorized = Tbl_add_members.objects.all()  
        pub = tbl_genpub_users.objects.all()  
        
        data = {
            "all_total": all_total,
            "this_week": this_week,
            "week_num": week_num,
            "yesterday_total":yesterday_total,
            "this_day": this_day,
         

          

            "all": all_authorized,
            "pub": pub,  
            
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


    data = {
            "district2_labels": d2_brgys,
            "district2_count": d2_brgys_count,

            "district1_labels": d1_brgys,
            "district1_count": d1_brgys_count,

            "offense_labels":offense_labels,
            "offense_count": offense_count,

            "sex_labels": sex_labels,
            "sex_count": sex_count,

            "time_count":time_count
    }

    return JsonResponse(data) #http response


def view_incidents (request):
    #term = 'Marcos Highway' since di parati nag ssearch si user, mag-eerror so mag lalagay ng blank para i-allow nya
    #pasig_incident_list = Tbl_pasig_incidents.objects.filter(Q(along_highway__icontains=term) |Q(corner_highway__icontains=term)).order_by('-id') 
    #pasig_incident_list = Tbl_pasig_incidents.objects.all().order_by('-id')

    # cursor=connection.cursor()
    # cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id DESC")
    # pasig_incident_list = cursor.fetchall()

   if request.method=="GET":
        incident_type = request.GET.get('coltype') 
        barang= request.GET.get('barangay')
        from_date =  request.GET.get('from_date')
        to_date =   request.GET.get('to_date')
    
        if is_valid(from_date) & is_valid(to_date):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search})
                
        elif is_valid(from_date) & is_valid(to_date) & is_not_valid(incident_type) & is_not_valid(barang):
            incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'"AND Date BETWEEN "'+from_date+'" AND "'+to_date+'" order by id DESC')
            return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search})
   
        if bool(incident_type) & bool(barang) :
            if incident_type=="Collision":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search})
            elif barang=="0":
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE Incident_Type = "'+incident_type+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search})
            
            else:
                incident_model_search=Tbl_pasig_incidents.objects.raw('Select * from roadcast_tbl_pasig_incidents WHERE Incident_Type = "'+incident_type+'" AND Barangay_id_id = "'+barang+'" order by id DESC')
                return render(request, 'encoder_view_incidents.html', {"pasig_incident_list":incident_model_search})
        else:
            unread_count = Tbl_pasig_incidents.objects.filter(read_status = "No").count()
            incident_model=Tbl_pasig_incidents.objects.raw('select * from roadcast_tbl_pasig_incidents order by id DESC')
            
            paginator = Paginator(incident_model, 10) #ano at ilan ang ipapakita per page
            page_number = request.GET.get('page') #ganto talaga
            incident_model = paginator.get_page(page_number) #ito ren, except sa var name

             
            # context = {'user_list': user_list}
            # return render (request, 'users/index.html', context)
            return render (request, 'encoder_view_incidents.html',
                                    {"pasig_incident_list":incident_model,"unread_count": unread_count
                                    })



def add_incident (request): #add using CSV
    try:
        #Landing page ng add incident page / wala pang process
        if request.method == "GET":
            member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
            investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
            brgy_list = Tbl_barangay.objects.all()
            context = {
                'brgy_list': brgy_list, 
                'investigators_list': investigators_list
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
                'url':'url'
                
            }

            return render (request, 'add_incident.html', context)
    except:
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Error: This is not a CSV file.')

        context = {
            'error_message': "Error uploading file. Please check file format.",
            
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
    Tbl_pasig_incidents.objects.filter(id=incident_id)
    messages.success(request, ("Successfully Deleted!"))
    return HttpResponseRedirect('/incidents/view')

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
         'brgy_list':brgy_list })

def processEditIncident(request, incident_id):
    incident_detail = get_object_or_404(Tbl_pasig_incidents, id=incident_id)

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

    
        narrative = request.POST.get('narrative')
        # added_by = "Encoder"
        inv_name = request.POST.get('inv_name')
      
    except (KeyError, Tbl_pasig_incidents.DoesNotExist): #KeyError is partner nung get_object_or_404
        return render(request, 'encoder_view_incident_detail.html', {
            'detail':incident_detail,
            'error_message': "Problem Updating Record.",
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
        return HttpResponseRedirect(reverse('incident_detail_view', args=(incident_id, ))) #name ng url yung gen_incident_detail_view NOT MISMONG URL


def report_summary (request):
    return render (request, 'report_summary.html')

# def report_monthly (request):
class Report_monthly (View):
    def get(self, request, *args, **kwargs):

        #1. BARANGAY STATS - monthly
        d1_brgy_distinct = []
        d1_brgy_distinct_count = []

        d2_brgy_distinct = []
        d2_brgy_distinct_count = []
        
        d1_brgys = Tbl_barangay.objects.filter(Q(District_id='1')).values_list('Barangay', flat=True).distinct()
        d2_brgys = Tbl_barangay.objects.filter(Q(District_id='2')).values_list('Barangay', flat=True).distinct()

        d1_total = 0
        d2_total = 0

        for dis in d1_brgys:
            d1_brgy_distinct.append(dis)
            x = Tbl_barangay.objects.filter(Barangay=dis).count()
            d1_brgy_distinct_count.append(x)
            d1_total = d1_total + int(x)


        for dis in d2_brgys:
            d2_brgy_distinct.append(dis)
            x = Tbl_barangay.objects.filter(Barangay=dis).count()
            d2_brgy_distinct_count.append(x)
            d2_total = d2_total + int(x)

        #2. CRIME/OFFENSE STATS - monthly
        offense = []
        offenses = Tbl_pasig_incidents.objects.filter(~Q(CrimeOffense='')).values_list('CrimeOffense', flat=True)

        str = ",".join(offenses)
        offense = str.split(",")

        distinct_offense= set(offense)
        offense_count = []
        offense_total = 0

        for dis in distinct_offense:
            x = offense.count(dis)
            offense_count.append(x)
            offense_total = offense_total + int(x)
            
        #3. VEHICLE STATS - monthly
        suspect_vehicles = []
        victim_vehicles = []

        suspect_vehicles = Tbl_pasig_incidents.objects.values_list('Suspect_Vehicle_Body_Type', flat=True)
        victim_vehicles = Tbl_pasig_incidents.objects.values_list('Victim_Vehicle_Body_Type', flat=True)

        vehicles_combined = list(chain(suspect_vehicles, victim_vehicles))
        distinct_vehicles = set(vehicles_combined)
        vehicle_count = []
        vehicle_total = 0

        for vehicle in distinct_vehicles:
            x = vehicles_combined.count(vehicle)
            vehicle_count.append(x)
            vehicle_total = vehicle_total + int(x)

        #4. AGE STATS - MALE - monthly
        suspect_age_m = []
        victim_age_m = []

        suspect_age_m = Tbl_pasig_incidents.objects.filter(Q(Suspect_Sex='Male') & ~Q(Suspect_Age ='')).values_list('Suspect_Age', flat=True)
        victim_age_m = Tbl_pasig_incidents.objects.filter(Q(Victim_Sex='Male')& ~Q(Victim_Age ='')).values_list('Victim_Age', flat=True)

        age_combined_m = list(chain(suspect_age_m, victim_age_m))
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
        
        for geriatric in range(60, 120):
            x = age_combined_m.count(geriatric)
            geriatric_m = geriatric_m + x

        age_total_m = child_m + adolescent_m + adult_m + geriatric_m 
        male_max = max(age_combined_m)

        #5. AGE STATS - FEMALE - monthly
        suspect_age_f = []
        victim_age_f = []

        suspect_age_f = Tbl_pasig_incidents.objects.filter(Q(Suspect_Sex='Female')).values_list('Suspect_Age', flat=True)
        victim_age_f = Tbl_pasig_incidents.objects.filter(Q(Victim_Sex='Female')).values_list('Victim_Age', flat=True)

        age_combined_f = list(chain(suspect_age_f, victim_age_f))
        age_total_f = child_f = adolescent_f = adult_f = geriatric_f = 0


        for child in range(0, 13):
            x = age_combined_f.count(child)
            child_f = child_f + x

        for adolescent in range(13, 20):
            x = age_combined_f.count(adolescent)
            adolescent_f = adolescent_f + x

        for adult in range(20, 60):
            x = age_combined_f.count(adult)
            adult_f = adult_f + x
        
        for geriatric in range(60, 120):
            x = age_combined_f.count(geriatric)
            geriatric_f = geriatric_f + x

        age_total_f = child_f + adolescent_f + adult_f + geriatric_f 

        data = {   
            "district1_data": zip(d1_brgy_distinct, d1_brgy_distinct_count),
            "district2_data": zip(d2_brgy_distinct, d2_brgy_distinct_count),
            "d1_total": d1_total,
            "d2_total": d2_total,

            "offense_data": zip(distinct_offense, offense_count),
            "offense_total": offense_total,

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
        }
        
        return render (request, 'monthly_summary/2018/january.html', data)

def get_monthly_data(request, *args, **kwargs):
    district_distinct = []
    district_distinct_count = []

    d1_brgy_distinct = []
    d1_brgy_distinct_count = []

    d2_brgy_distinct = []
    d2_brgy_distinct_count = []

    district = Tbl_pasig_incidents.objects.values_list('District', flat=True).distinct()
    d1_brgys = Tbl_pasig_incidents.objects.filter(Q(District='1')).values_list('Barangay_id_id', flat=True).distinct()
    d2_brgys = Tbl_pasig_incidents.objects.filter(Q(District='2')).values_list('Barangay_id_id', flat=True).distinct()

    district_distinct = ['D1', 'D2']
    # d1_brgy_distinct = ['']
    # d2_brgy_distinct = []


    for dis in district:
        # district_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(District=dis).count()
        district_distinct_count.append(x)

    for dis in d1_brgys:
        d1_brgy_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(Barangay_id_id=dis).count()
        d1_brgy_distinct_count.append(x)

    for dis in d2_brgys:
        d2_brgy_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(Barangay_id_id=dis).count()
        d2_brgy_distinct_count.append(x)


    #2. CRIME/OFFENSE STATS - monthly
        offense = []
        offenses = Tbl_pasig_incidents.objects.values_list('CrimeOffense', flat=True)

        str = ",".join(offenses)
        offense = str.split(",")

        distinct_offense= list(set(offense))
        offense_count = []
        offense_total = 0

        for dis in distinct_offense:
            x = offense.count(dis)
            offense_count.append(x)
            offense_total = offense_total + int(x)
            
        #3. VEHICLE STATS - monthly
        suspect_vehicles = []
        victim_vehicles = []

        suspect_vehicles = Tbl_pasig_incidents.objects.values_list('Suspect_Vehicle_Body_Type', flat=True)
        victim_vehicles = Tbl_pasig_incidents.objects.values_list('Victim_Vehicle_Body_Type', flat=True)

        vehicles_combined = list(chain(suspect_vehicles, victim_vehicles))
        distinct_vehicles = list(set(vehicles_combined))
        vehicle_count = []
        vehicle_total = 0

        for vehicle in distinct_vehicles:
            x = vehicles_combined.count(vehicle)
            vehicle_count.append(x)
            vehicle_total = vehicle_total + int(x)

    
    monthly_data = {
        "district_labels": district_distinct,
        "district_count": district_distinct_count,

        "district1_labels": d1_brgy_distinct,
        "district1_count": d1_brgy_distinct_count,

        "district2_labels": d2_brgy_distinct,
        "district2_count": d2_brgy_distinct_count,

        "offense_labels": distinct_offense, 
        "offense_count": offense_count,
        # "offense_total": offense_total,

        "vehicle_labels": distinct_vehicles, 
        "vehicle_count":vehicle_count,
        # "vehicle_total": vehicle_total,
      
    }
    return JsonResponse(monthly_data) #http response

def notification (request):
    # pasig_barangay_list = Tbl_barangay.objects.all().order_by('-id')
    # pasig_incident_list = Tbl_pasig_incidents.objects.all().order_by('-id')

    #for new incident accident
    cursor=connection.cursor()
    cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id")
    pasig_incident_list = cursor.fetchall()

    #for gen pub reports inbox
    pasig_public_reports = Tbl_public_report.objects.all().order_by('-id')
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    data = {
        'pasig_incident_list': pasig_incident_list, 
        'public_reports_list': pasig_public_reports,
        'unread_notif_count': unread_notif_count
    }
    return render (request, 'notification.html', data)


def notif_public_report_detail (request, gen_pub_report_id):

    member_type = Tbl_member_type.objects.get(Member_Type='Investigator')
    investigators_list = Tbl_add_members.objects.filter(Members_User_id=member_type.id)
    substation_list = Tbl_substation.objects.all()

    unread_public_report = Tbl_public_report.objects.get(id=gen_pub_report_id)
    unread_public_report.Read_Status = "Yes"
    #unread_public_report.Report_Status = "Unsolved"
    # unread_public_report.Substation_id = ""

    unread_public_report.save()
    
    #for gen pub reports inbox
    pasig_public_reports = Tbl_public_report.objects.all().order_by('-id')
    unread_notif_count = Tbl_public_report.objects.filter(Read_Status="No").count()

    #to see admin replies <3
    admin_responses = Tbl_public_report_response.objects.filter(Report_id = gen_pub_report_id)
    data = {
        'public_reports_list': pasig_public_reports,
        'detail': unread_public_report,
        'unread_notif_count': unread_notif_count,
        'investigators_list': investigators_list,
        'substation_list': substation_list,
        'admin_responses': admin_responses
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

    admin_responses = Tbl_public_report_response.objects.create(
                    Sender        = "Admin",
                    Response = admin_reply,
                    Report_id = report_id, )

    admin_responses.save()

    return HttpResponseRedirect(reverse('notif_public_report_detail', args=(report_id,)))

def sub_notification (request):
    return render (request, 'sub_notification.html')

def public_notification (request):
    return render (request, 'gen_notification.html')

def unsolved_cases (request):
    cursor=connection.cursor()
    cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id")
    pasig_incident_list = cursor.fetchall()

    data = {
        'pasig_incident_list': pasig_incident_list,  
    }
    return render (request, 'unsolved_cases.html', data)

def logout (request):
    return render (request, 'logout.html')

#PUBLIC
def submit_report (request):
    try:
        if request.method == "GET":
            return render (request, 'submit_report.html')#Load view

        user_id ="Faith Abuan"
        city = request.POST.get('city')
        barangay = request.POST.get('Barangay')
        district = request.POST.get('district')
        address = request.POST.get('address')
        along = request.POST.get('along')
        corner = request.POST.get('corner')
        narrative = request.POST.get('narrative')
        recipient = "Admin"

        if request.FILES.get('image'):
            image_proof = request.FILES.get('image')

        incident_report = Tbl_public_report.objects.create(
                        User_ID = user_id,
                        Reported_City=city, 
                        Reported_Brgy_id=barangay,               
                        Reported_District=district,           
                        Reported_Location=address,               
                        Reported_Along=along,
                        Reported_Corner=corner, 
                        Reported_Narrative = narrative,
                        Reported_Image_Proof = image_proof,
                        Report_Status = 'Unsolved',
                        Read_Status='No',
                        Recipient = recipient)
        
        incident_report.save()

        context = {
            'success_message':"Your report has been submitted!",
        }
        return render (request, 'submit_report.html', context)

    except:
        image_proof = request.FILES['image']
        
        if not image_proof.name.endswith('.png'| '.jpg'| '.jpeg'):
            messages.error(request, 'Error: Invalid Image Format')

        context = {
            'error_message': "Error sending report!",
        }

        return render (request, 'submit_report.html', context)

def pub_notif_inbox (request):
    return render (request, 'public_notif_setting.html')

def pub_notif_view (request):
    return render (request, 'gen_notification_view.html')

def pub_incident_detail_view (request, incident_id):

    pasig_incident_detail = Tbl_pasig_incidents.objects.get(pk=incident_id)

    context = {
        "incident_detail": pasig_incident_detail,

    }
    return render (request, 'gen_incident_detail_view.html', context)

# Audit trail - Jew

def admin_audit_trail(request, ):

    audit = tbl_audit.objects.all()
    context={'audit':audit}
 
    return render (request, 'admin_audit_trail_members.html',context)  

def user_profile(request):
    return render (request, 'user_profile.html')

