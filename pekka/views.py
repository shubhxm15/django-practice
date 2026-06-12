from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello what's up!!")

def good(request):
    return HttpResponse("<h1>This is a path page.</h1>")

def lorem(request):
    return render(request, 'index.html')

def dataa(request):

    peoples = [
        {'Name': 'Shubham', 'age': 20},
        {'Name': 'Shubham singh', 'age': 19},
        {'Name': 'Shubham sharma', 'age': 16},
        {'Name': 'Shubham goyal', 'age': 25},
        {'Name': 'Shubham dutt', 'age': 200},
    ]
    return render(request, 'index1.html', context= {'peoples': peoples})

def sample(request):
    
    return render(request, 'sample.html', context = {'page' : 'sample page'})