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
    #Required vars for logic
    flu = 0
    hypoglycemia = 0
    food_poisoning = 0
    counter_list = [flu, hypoglycemia]
    flu_list = ["sneeze", "cough", "fever"]
    hypoglycemia_list = ["confusion", "nausea", "personality changes"]
    food_poisoning_list = ["abdominal pain", "vomiting", "fever", "Headache"]
    # Create a form instance with POST data.
    form = nSymx()
    if request.method == "POST":
        form = nSymx(request.POST)

        #create new instance
        new_author = form.save(commit=False)


        #Food Poisoning
        if (new_author.first_symx in (food_poisoning_list)):
            food_poisoning += 1
        if (new_author.second_symx in (food_poisoning_list)):
            food_poisoning += 1
        if (new_author.third_symx in (food_poisoning_list)):
            food_poisoning += 1
        if (new_author.fourth_symx in (food_poisoning_list)):
            food_poisoning += 1
        if (new_author.fifth_symx in (food_poisoning_list)):
                    food_poisoning += 1

        #FLu
        if (new_author.first_symx in (flu_list)):
            flu += 1
        if (new_author.second_symx in (flu_list)):
            flu += 1
        if (new_author.third_symx in (flu_list)):
            flu += 1
        if (new_author.fourth_symx in (flu_list)):
            flu += 1
        if (new_author.fifth_symx in (flu_list)):
            flu += 1

        #Hypoglycemia
        if (new_author.first_symx in (hypoglycemia_list)):
            hypoglycemia += 1
        if (new_author.second_symx in (hypoglycemia_list)):
            hypoglycemia += 1
        if (new_author.third_symx in (hypoglycemia_list)):
            hypoglycemia += 1
        if (new_author.fourth_symx in (hypoglycemia_list)):
            hypoglycemia += 1
        if (new_author.fifth_symx in (hypoglycemia_list)):
            hypoglycemia += 1

        #Diagnose
        if max(flu, hypoglycemia, food_poisoning) == hypoglycemia and hypoglycemia != 0:
            new_author.diagnosis = "Hypoglycemia"
        if max(flu, hypoglycemia, food_poisoning) == flu and flu != 0:
            new_author.diagnosis = "Flu"
        if max(flu, hypoglycemia, food_poisoning) == food_poisoning and food_poisoning != 0:
            new_author.diagnosis = "Food Poisoning"
        # Add if here so it can add the symptoms is PPD
        print(hypoglycemia)
        print(flu)
        print(food_poisoning)


        #save after change
        new_author.save()
        if form.is_valid():
            form.save_m2m()
            return next(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'emergency/symptoms.html',{'form':form})
