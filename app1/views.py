from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sam(request):
    return HttpResponse('<h1>WELCOME TO HOME PAGE</h1>')

def carry_data(request,data):
    return HttpResponse(f'<h1>The Recived data is {data}</h1>')

def facto(request,num):
    fact = 1
    for i in range(int(num),1,-1):
        fact*=i
    return HttpResponse(f'<h1>The factorial of {num} is {fact}</h1>')

def add(request,num1,num2):
    try:
        num1 = int(num1)
    except:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except:
        num2 = float(num2)
    return HttpResponse(num1+num2)
    
