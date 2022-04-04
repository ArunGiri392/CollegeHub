from xml.dom import UserDataHandler
from django.shortcuts import render
from .models import Colleges,Essays
from .forms import ScoresForm
# Create your views here.
def startingpage(request):
    form = ScoresForm()
    if request.method == 'POST':
        value = request.POST['collegename']
        # college = Colleges.objects.filter(Name__iexact = value)
        college = Colleges.objects.filter(Name__contains = value)
        if len(college) == 0 or len(value) <= 3:
           return render(request, "colleges/collegenotfound.html",{"college":college})
        else:
            college = college[0]
            return render(request, "colleges/collegedetail.html",{"college":college})
    else:
        return render(request, "colleges/index.html",{"form":form})


def detailcollege(request,value):
    college = Colleges.objects.get(id=value)
    return render(request, "colleges/collegedetail.html",{"college":college})


def linkpages(request, value):
    if value == "Scholarship":
        colleges = Colleges.objects.all().order_by("Name")
        return render(request, "colleges/scholarship.html",{"colleges":colleges})
    
     
    elif value == "College Essays":
         essay = Essays.objects.all()[0]
         return render(request, "colleges/Collegeessays.html",{"essay":essay})
    
    elif value == "Essay_detail":
        essay = Essays.objects.all()[0]
        return render(request, "colleges/essaydetail.html",{"essay":essay})
    

     
    elif value == "Terminologies":
        return render(request, "colleges/Terminologies.html")
    
     
    elif value == "Tips and Tricks":
        return render(request, "colleges/Tips.html")
    
    elif value == "submitinformation":
        return render(request, "colleges/submitinformation.html")
    
    
def scores(request):
    if request.method == "POST":
        userdata = ScoresForm(request.POST)
        if userdata.is_valid():
            Satscore = userdata.cleaned_data.get("SAT")
            Gpa = userdata.cleaned_data.get("GPA")
            Matched_Colleges = Colleges.objects.filter(MinimumSAT__lte=Satscore, MinimumGpa__lte=Gpa)
            return render(request, "colleges/filteredcolleges.html",{"Matched_colleges":Matched_Colleges})
    


    form = ScoresForm()
    return render(request, "colleges/index.html",{"form":form})

