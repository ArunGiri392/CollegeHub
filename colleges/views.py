from django.shortcuts import render
from .models import Colleges,Interview
# Create your views here.
def startingpage(request):
    return render(request, "colleges/index.html")


def detailcollege(request,value):
    college = Colleges.objects.get(id=value)
    return render(request, "colleges/collegedetail.html",{"college":college})


def linkpages(request, value):
    if value == "Scholarship":
        colleges = Colleges.objects.all().order_by("Name")
        return render(request, "colleges/scholarship.html",{"colleges":colleges})
    
     
    elif value == "Interview experiences":
         interviews = Interview.objects.all()
         return render(request, "colleges/interviewexperiences.html",{"interviews":interviews})
    
    elif value == "interview_detail":
       interviews = Interview.objects.all()
       return render(request, "colleges/interviewdetail.html",{"interviews":interviews})
    

     
    elif value == "Terminologies":
        return render(request, "colleges/Terminologies.html")
    
     
    elif value == "Tips and Tricks":
        return render(request, "colleges/Tips.html")
    
    elif value == "submitinformation":
        return render(request, "colleges/submitinformation.html")
    
    
