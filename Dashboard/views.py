from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
   return render(request,'dashboard.html')