from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'spotify/index.html')

def form2(request):
    return render(request,'spotify/form2.html')