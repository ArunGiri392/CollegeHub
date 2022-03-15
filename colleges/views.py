from django.shortcuts import render
from .models import Colleges,Interview
# Create your views here.
def startingpage(request):
    if request.method == 'POST':
        value = request.POST['collegename']
        # college = Colleges.objects.filter(Name__iexact = value)
        college = Colleges.objects.filter(Name__contains = value)
        if len(college) == 0 or len(value) <= 3:
           return render(request, "colleges/collegenotfound.html",{"college":college})
        else:
            college = college[0]
            return render(request, "colleges/collegedetail.html",{"college":college})

        
        # if college != []:
        #     return render(request, "colleges/collegedetail.html",{"college":college})

        print(value)
        print(college)
    return render(request, "colleges/index.html",{"value":college})


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
    
    
