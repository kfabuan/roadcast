from django.shortcuts import render
from .models import Tbl_pasig_incidents, Tbl_barangay, Tbl_district
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import View #for charts
from django.http import JsonResponse
from django.db.models import Q
from collections import Counter
from itertools import chain
from django.db import connection

import numpy as np

def index(request): #landing/home
    return render (request, 'landing.html')

def login(request):
    return render (request, 'login.html') 

class DashboardView (View):
    def get(self, request, *args, **kwargs):
        d2_brgy_distinct = []
        d2_brgy_distinct_count = []

        d2_brgys = Tbl_pasig_incidents.objects.filter(Q(District='1')).values_list('Barangay_id', flat=True).distinct()

        for dis in d2_brgys:
            d2_brgy_distinct.append(dis)
            x = Tbl_pasig_incidents.objects.filter(Barangay_id=dis).count()
            d2_brgy_distinct_count.append(x)

        #CRIME/OFFENSE
        offense =[]
        new_crime = []
        offenses = Tbl_pasig_incidents.objects.values_list('CrimeOffense', flat=True)

        str = ",".join(offenses)
        offense = str.split(",")

        distinct_offense= set(offense)
        offense_count = []

        for dis in distinct_offense:
            x = offense.count(dis)
            offense_count.append(x)
            
        data = {
            "district2_labels": d2_brgys,
            "district2_count": d2_brgy_distinct_count,
            "new_crime": new_crime,
            "offense":offense,
            "distinct_offense":distinct_offense,
            "offense_count": offense_count,
        }
        
        return render (request, 'dashboard.html', data)

def get_data(request, *args, **kwargs):
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


    #CRIME/OFFENSE
    offense =[]
    offenses = Tbl_pasig_incidents.objects.values_list('CrimeOffense', flat=True)

    str = ",".join(offenses)
    offense = str.split(",")

    distinct_offense= set(offense)
    offense_count = []
    offense_total = 0
    
    for dis in distinct_offense:
        x = offense.count(dis)
        offense_count.append(x)
        offense_total = offense_total + int(x)

    data = {
        "district_labels": district_distinct,
        "district_count": district_distinct_count,

        "district1_labels": d1_brgy_distinct,
        "district1_count": d1_brgy_distinct_count,

        "district2_labels": d2_brgy_distinct,
        "district2_count": d2_brgy_distinct_count,
      
    }

    return JsonResponse(data) #http response

def view_incidents (request):
    term = 'Marcos Highway' #since di parati nag ssearch si user, mag-eerror so mag lalagay ng blank para i-allow nya
    #pasig_incident_list = Tbl_pasig_incidents.objects.filter(Q(along_highway__icontains=term) |Q(corner_highway__icontains=term)).order_by('-id') 
    pasig_incident_list = Tbl_pasig_incidents.objects.all().order_by('-id')
    context = {
        'pasig_incident_list': pasig_incident_list,  
    }
    return render (request, 'view_incidents.html', context) 

def uploadcsv (request):
    return render (request, 'upload_csv.html')

def add_incident (request):
    brgy_list = Tbl_barangay.objects.values_list('Barangay_id', flat=True).distinct()
    context = {
        'brgy_list': brgy_list,  
    }
    return render (request, 'add_incident.html', context)

def processAddIncident(request):
    city = "Pasig"
    unitstation="Pasig City Police Station"
    crime_offense=request.POST.get('display_offense')
    date_committed = request.POST.get('DateCommitted') #name attribute of textbox
    current_time = request.POST.get('currentTime')
    col_type = request.POST.get('collision_type')
    weather = request.POST.get('weather')
    surface_type = request.POST.get('surface_type')
    road_char = request.POST.get('road_character')
    surface_cond = request.POST.get('surface_condition')
    road_repair = request.POST.get('road-repair')
    case_status = request.POST.get('case_status')
    hit_and_run = request.POST.get('hit-and-run')
    inv_name = request.POST.get('inv_name')
    barangay = "1"
    district = "1"
    
    print(date_committed)
    print(current_time)
    incident_record = Tbl_pasig_incidents.objects.create(City=city, UnitStation=unitstation, CrimeOffense=crime_offense, Barangay_id=barangay, District_id=district, Date=date_committed, Time=current_time, Incident_Type=col_type, Weather=weather, Surface_Condition=surface_cond, Surface_Type=surface_type, Road_Character=road_char)
    incident_record.save()
    return HttpResponseRedirect('/incidents/view')

def report_summary (request):
    return render (request, 'report_summary.html')

def report_monthly (request):

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
    offenses = Tbl_pasig_incidents.objects.values_list('CrimeOffense', flat=True)

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

    suspect_age_m = Tbl_pasig_incidents.objects.filter(Q(Suspect_Sex='Male')).values_list('Suspect_Age', flat=True)
    victim_age_m = Tbl_pasig_incidents.objects.filter(Q(Victim_Sex='Male')).values_list('Victim_Age', flat=True)

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
    
    for geriatric in range(60, max(age_combined_m)+1):
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
    
    for geriatric in range(60, max(age_combined_f)+1):
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


def notification (request):
    # pasig_barangay_list = Tbl_barangay.objects.all().order_by('-id')
    # pasig_incident_list = Tbl_pasig_incidents.objects.all().order_by('-id')

    cursor=connection.cursor()
    cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id")
    pasig_incident_list = cursor.fetchall()

    data = {
        'pasig_incident_list': pasig_incident_list,  
    }
    return render (request, 'notification.html', data)

def sign_up_validation (request):
    return render (request, 'sign_up_validation.html')

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

