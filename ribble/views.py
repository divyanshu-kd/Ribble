from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from ribble import models
from .models import details
from django.contrib import messages


# Create your views here.
# data = details.objects.all().values()
def home(request, id):
    # var_name = request.GET.get('data')
    data = details.objects.get(id = id)
    if request.method == "POST":
        item = request.POST
        img = request.FILES.get('avatar')
        location = item.get('location')
        # if data.location == None:
        data.location = location
        data.avatar = img
        data.save()
        return redirect(f'/About/{id}')
        # return render(request, 'About.html', {'data':data})
    return render(request, 'Home.html')
def about(request, id):
    data = details.objects.get(id=id)
    return render(request, 'About.html', {'data':data})

    # return render(request, 'About.html')
def form(request):
    if request.method == "POST":
        username = request.POST['username']
        user = details.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/')
        name = request.POST['name']
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']
        terms = request.POST['terms']
        ins = models.details(name=name, username=username, email=email, password=password, terms=terms)
        ins.save()
        context = details.objects.all()
        for item in context:
            if item.password == password and item.username == username:
                id = item.id
                return redirect(f'/Home/{id}/')
    return render(request, 'Form.html')
def log(request):
    if request.method == "POST":
        user = request.POST['userID']
        pas = request.POST['Password']
        context = details.objects.all()
        for item in context:
            if item.password == pas and item.username == user:
                id = item.id
                data = details.objects.get(id=id)
                # return render(request, 'About.html', {'data':data})
                return redirect(f'/About/{id}')
    return render(request, 'log.html')

