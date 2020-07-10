from django.shortcuts import render

def dashboard(request):
    return render(request,'html/dashboard.html')