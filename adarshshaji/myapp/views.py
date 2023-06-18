from django.shortcuts import render
from myapp import templates
def index(request):
    return render(request,'index.html')
def protfolio(request):
    return render(request,'protfolio.html')
# Create your views here.
