from django.shortcuts import render

def SiteHome(request):
    return render(request,'sc/site_home.html')

def ScHome(request):
    return render(request,'sc/sc_home.html')
