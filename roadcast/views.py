from django.shortcuts import render, get_object_or_404, reverse #get_object_or_404 & reverse for processEdit
from .models import Tbl_pasig_incidents, Tbl_barangay, Tbl_district, Tbl_public_report
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.views.generic import View #for charts
from django.http import JsonResponse
from django.db.models import Q
from collections import Counter
from itertools import chain
from django.db import connection

from PIL import Image


from django.contrib import messages #for csv upload

import csv, io

def index(request): #landing/home
    return render (request, 'landing.html')

def login(request):
    return render (request, 'login.html') 

def about_us(request):
    return render (request, 'about_us.html') 

def contact_us(request):
    return render (request, 'contact_us.html') 

def contact_no(request):
    return render (request, 'contact_no.html') 

def sign_up (request):
    return render (request, 'sign_up.html')
    
def sign_up_validation (request):
    return render (request, 'sign_up_validation.html')

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

class DashboardView (View):
    def get(self, request, *args, **kwargs):
        d2_brgy_distinct = []
        d2_brgy_distinct_count = []

        d2_brgys = Tbl_pasig_incidents.objects.select_related('Barangay_id').filter(Q(District='1')).values_list('Barangay_id', flat=True).distinct()

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
    #term = 'Marcos Highway' since di parati nag ssearch si user, mag-eerror so mag lalagay ng blank para i-allow nya
    #pasig_incident_list = Tbl_pasig_incidents.objects.filter(Q(along_highway__icontains=term) |Q(corner_highway__icontains=term)).order_by('-id') 
    #pasig_incident_list = Tbl_pasig_incidents.objects.all().order_by('-id')

    # cursor=connection.cursor()
    # cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id DESC")
    # pasig_incident_list = cursor.fetchall()

    incident_type = request.GET.get('coltype') 
  
    barang= request.GET.get('barangay')
    
 
    all_entries = Tbl_pasig_incidents.objects.all()
    context1 = {
            'pasig_incident_list': all_entries,  
        }

    pasig_incident_list=Tbl_pasig_incidents.objects.filter(Q(Incident_Type=incident_type) & Q(Barangay_id_id=barang))
    pasig_incident_list_it= Tbl_pasig_incidents.objects.filter(Q(Incident_Type=incident_type))
    
    pasig_incident_list_br= Tbl_pasig_incidents.objects.filter(Q(Barangay_id_id=barang))
    context3 = {
        'pasig_incident_list': pasig_incident_list_br,  
    }

    context2 = {
        'pasig_incident_list': pasig_incident_list,  
    }
  
    if bool(incident_type) & bool(barang):
         return render (request, 'encoder_view_incidents.html', context2)
    elif (incident_type==0):
        return render (request, 'encoder_view_incidents.html', context3) 
    else:
        return render (request, 'encoder_view_incidents.html', context1) 



def add_incident (request):
    try:
        # GET request returns the value of the data with the specified key.
        if request.method == "GET":
            return render(request, 'add_incident.html')

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

            brgy_list = Tbl_barangay.objects.values_list('Barangay', flat=True).distinct()

            context = {
                'brgy_list': brgy_list, 
                'success_message':"Successfully Added!",
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

def processAddIncident(request):

    city = "Pasig"
    unit_station = "Pasig City Police Station"
    crime_offense = request.POST.get('display_offense')
    #week 
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
    #avenue
    #road
    #street
    #bound
    #highway
    #others
    surface_cond = request.POST.get('surface_condition')
    surface_type = request.POST.get('surface_type')
    road_class = "Ewan" #idk
    road_repair = request.POST.get('road-repair')
    hit_and_run = request.POST.get('hit-and-run')
    road_char = request.POST.get('road_character')

    sus_name = request.POST.get('sus_name')
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
    # sus_vec_model = request.POST.get('sus_vec_model')

    vic_type = request.POST.get('vic_type')
    vic_name = request.POST.get('vic_name')
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
   
    narrative = request.POST.get('narrative')

    # date_today = request.POST.get('date-today')
    added_by = "wala pa"
    #inv_name = request.POST.get('inv_name')
    
    incident_record = Tbl_pasig_incidents.objects.create(
                    City=city, 
                    UnitStation=unit_station,               
                    CrimeOffense=crime_offense,           
                    Date=date_committed,               
                    Time=current_time, 
                    Day = day, 
                    Incident_Type=col_type, 
                    Number_of_Persons_Involved=no_of_person_involved, 
                    Light=light, 
                    Weather=weather, 
                    Case_Status=case_status, 
                    District_id = district, 
                    Barangay_id_id = barangay, 
                    Address = address, 

                    Surface_Condition=surface_cond, 
                    Surface_Type=surface_type, 
                    Road_Class=road_class, 
                    Road_Repair = road_repair, 
                    Hit_and_Run = hit_and_run,
                    Road_Character=road_char, 
    
                    Suspect_Name=sus_name, 
                    Suspect_Severity=sus_severity,
                    Suspect_Age=sus_age, 
                    Suspect_Sex=sus_sex, 
                    Suspect_Civil_Status = sus_civil_status, 
                    Suspect_Address=sus_add,  
                    Suspect_Vehicle=sus_vehicle, 
                    Suspect_Vehicle_Body_Type=sus_vehicle_body_type, 
                    Suspect_Plate_No=sus_plate_no,
                    Suspect_Reg_Owner=sus_reg_owner, 
                    Suspect_Drl_No=sus_drl, 
                    # Suspect_Vehicle_Year_Model=sus_vec_model, 
                    
                    Victim_Type = vic_type,
                    Victim_Name=vic_name, Victim_Severity=vic_severity,Victim_Age=vic_age, 
                    Victim_Sex=vic_sex, Victim_Civil_Status = vic_civil_status, Victim_Address=vic_add, 
                    Victim_Vehicle=vic_vehicle, Victim_Vehicle_Body_Type=vic_vehicle_body_type, 
                    Victim_Plate_No=vic_plate_no,Victim_Reg_Owner=vic_reg_owner, 
                    Victim_Drl_No=vic_drl, 
                    #Victim_Vehicle_Year_Model=vic_vec_model,

                    Narrative=narrative, 
                    added_by=added_by )
                    
    incident_record.save()
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


def encoder_view_incident_detail(request, incident_id): #pag view lang ng edit page, pas sinubmit form, YUNG def processEdit mag hahandle
    try:
        pasig_incident_detail = Tbl_pasig_incidents.objects.get(id=incident_id)

    except Tbl_pasig_incidents.DoesNotExist:
        raise Http404("Incident does not exist")

    return render(request, 'encoder_view_incident_detail.html', {'pasig_incident_detail': pasig_incident_detail})

def processEditIncident(request, incident_id):
    incident_detail = get_object_or_404(Tbl_pasig_incidents, id=incident_id)

    try:
        crime_offense = request.POST.get('display_offense')
        #week 
        date_committed = request.POST.get('DateCommitted') #name attribute of textbox
        current_time = request.POST.get('currentTime')
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
        # road
        # street
        # bound
        # highway
        # others
        surface_cond = request.POST.get('surface_condition')
        surface_type = request.POST.get('surface_type')
        road_class = "Ewan" #idk
        road_repair = request.POST.get('road-repair')
        hit_and_run = request.POST.get('hit-and-run')
        road_char = request.POST.get('road_character')

        sus_name = request.POST.get('sus_name')
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
        # sus_vec_model = request.POST.get('sus_vec_model')

        vic_type = request.POST.get('vic_type')
        vic_name = request.POST.get('vic_name')
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
    
        narrative = request.POST.get('narrative')

        # date_today = request.POST.get('date-today')
        added_by = "wala pa"
        inv_name = request.POST.get('inv_name')
      
    except (KeyError, Tbl_pasig_incidents.DoesNotExist): #KeyError is partner nung get_object_or_404
        return render(request, 'encoder_view_incident_detail.html', {
            'detail':incident_detail,
            'error_message': "Problem Updating Record.",
        })
    else:
        incident = Tbl_pasig_incidents.objects.get(id=incident_id) #kukunin yung row sa database na kapareha ng incident_id
        incident.CrimeOffense=crime_offense         
        # incident.Date=date_committed             
        # incident.Time=current_time
        # incident.Day = day 
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
        incident.Road_Class=road_class
        incident.Road_Repair = road_repair 
        incident.Hit_and_Run = hit_and_run
        incident.Road_Character=road_char

        incident.Suspect_Name=sus_name
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
        # Suspect_Vehicle_Year_Model=sus_vec_model 
        
        incident.Victim_Type = vic_type
        incident.Victim_Name=vic_name 
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
        # #Victim_Vehicle_Year_Model=vic_vec_model

        incident.Narrative=narrative
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

    cursor=connection.cursor()
    cursor.execute("SELECT roadcast_tbl_pasig_incidents.* , roadcast_tbl_barangay.barangay FROM roadcast_tbl_pasig_incidents LEFT JOIN roadcast_tbl_barangay ON roadcast_tbl_pasig_incidents.Barangay_id_id=roadcast_tbl_barangay.id ORDER BY roadcast_tbl_pasig_incidents.id")
    pasig_incident_list = cursor.fetchall()

    pasig_public_reports = Tbl_public_report.objects.all().order_by('-id')

    data = {
        'pasig_incident_list': pasig_incident_list, 
        'public_reports_list': pasig_public_reports 
    }
    return render (request, 'notification.html', data)

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

        user_id ="Nakay Dane Pa"
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



