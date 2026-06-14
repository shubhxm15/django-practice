from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def kitchen_view(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image =  request.FILES.get('receipe_image')

        kitchen.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/kitchen/')
    
    queryset = kitchen.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'kitchen': queryset}

    return render(request, 'receipe.html', context)

def delete_receipe(request, id):
    queryset = kitchen.objects.get(id=id)
    queryset.delete()
    return redirect('/kitchen/')

def update_receipe(request, id):
    queryset = kitchen.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/kitchen/')

    context = {'kitchen': queryset}
    return render(request, 'update_receipe.html', context)
    
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username = email).exists():
            messages.error(request, 'Email does not exist')
            return redirect('/login/')

        user = authenticate(username = email, password = password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')

        else:
            login(request, user)
            return redirect('/kitchen/')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        if user.exists():
            messages.info(request, 'Email already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            username=email,
            email = email,
            first_name = first_name,
            last_name = last_name
            )
        user.set_password(password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('/register/')
    
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')