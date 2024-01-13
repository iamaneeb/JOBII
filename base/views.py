from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'base/home.html')


def Jobs(request):
    
    return render(request,'base/jobs.html')