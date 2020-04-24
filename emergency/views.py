from django.shortcuts import render
from django.http import HttpResponse
from .models import Symx
from emergency import forms
from .forms import  nSymx
# Create your views here.
def index(request):
    return render(request,'emergency/index.html')

def next(request):
    return render(request,'emergency/next.html')

def results(request):
    symptom_list = Symx.objects.order_by('MRN_number')
    symptom_dict = {"symptoms":symptom_list}
    return render(request,'emergency/results.html',context=symptom_dict)


def symptoms(request):
    form = nSymx()
    if request.method == "POST":
        form = nSymx(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return next(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'emergency/symptoms.html',{'form':form})
