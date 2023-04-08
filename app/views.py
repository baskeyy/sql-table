from django.shortcuts import render
from app.models import *

# Create your views here.
def display_dept(request):
    lod=DEPT.objects.all()
    d={'dept':lod}
    return render(request,'display_dept.html',d)

def display_emp(request):
    loe=EMP.objects.all()
    d={'emp':loe}
    return render(request,'display_emp.html',d)
