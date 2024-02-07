from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

#Returning string as response by using FBV(function based views)
def fbv_string(request):
    return HttpResponse('<h1>Returning string from fbv_string')

#Returning string as response by using CBV(class based views)
class CBVString(View):
    def get(self,request):
        return HttpResponse('Returning string from CBVString')
    
#Rendering html by FBV
def fbvhtml(request):
    return render(request,'fbvhtml.html')

#Rendering html by CBV
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    
#Insert data by FBV through model forms
def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')
    return render(request,'insert_school_by_fbv.html',d)


# Insert Data By using Class Based View
class insert_school_by_Cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_school_by_Cbv.html',d)   
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_Cbv is done')
