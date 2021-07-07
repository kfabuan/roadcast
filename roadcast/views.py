from django.shortcuts import render
from .models import Tbl_pasig_incidents

from django.views.generic import View #for charts
from django.http import JsonResponse
from django.db.models import Q

def index(request): #landing/home
    return render (request, 'landing.html')

def login(request):
    return render (request, 'login.html') 

class DashboardView (View):
    def get(self, request, *args, **kwargs):
        d2_brgy_distinct = []
        d2_brgy_distinct_count = []

        d2_brgys = Tbl_pasig_incidents.objects.filter(Q(District__icontains='District 1')).values_list('Barangay', flat=True).distinct()

        for dis in d2_brgys:
            d2_brgy_distinct.append(dis)
            x = Tbl_pasig_incidents.objects.filter(Barangay=dis).count()
            d2_brgy_distinct_count.append(x)

        data = {
            "district2_labels": d2_brgys,
            "district2_count": d2_brgy_distinct_count,
            "number": "helllooo",
        }
        
        return render (request, 'dashboard.html', data)

def get_data(request, *args, **kwargs):
    district_distinct = []
    district_distinct_count = []

    d1_brgy_distinct = []
    d1_brgy_distinct_count = []

    d2_brgy_distinct = []
    d2_brgy_distinct_count = []

    district = Tbl_pasig_incidents.objects.values_list('district', flat=True).distinct()
    d1_brgys = Tbl_pasig_incidents.objects.filter(Q(District__icontains='District 1')).values_list('Barangay', flat=True).distinct()
    d2_brgys = Tbl_pasig_incidents.objects.filter(Q(District__icontains='District 2')).values_list('Barangay', flat=True).distinct()
    
    for dis in district:
        district_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(District=dis).count()
        district_distinct_count.append(x)

    for dis in d1_brgys:
        d1_brgy_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(Barangay=dis).count()
        d1_brgy_distinct_count.append(x)

    for dis in d2_brgys:
        d2_brgy_distinct.append(dis)
        x = Tbl_pasig_incidents.objects.filter(Barangay=dis).count()
        d2_brgy_distinct_count.append(x)


    data = {
        "district_labels": district_distinct,
        "district_count": district_distinct_count,

        "district1_labels": d1_brgy_distinct,
        "district1_count": d1_brgy_distinct_count,

        "district2_labels": d2_brgy_distinct,
        "district2_count": d2_brgy_distinct_count,
      
        "number": "helllooo",
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
    return render (request, 'add_incident.html')
