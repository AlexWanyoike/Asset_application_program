from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .forms import ApplicationRequestForm
#from .models import Employee, Asset_allocation, Associate, Team_leader, Manager
from django.contrib.auth.forms import UserCreationForm
#from .forms import EmployeeForm, AssociateForm, Team_leaderForm, ManagerForm, Asset_allocationForm
from .decorators import managerdecorator

# Create your views here.


def welcome(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


@managerdecorator(allowed_roles=['associate'])
def request(request):
    form = ApplicationRequestForm()
    if request.method == "POST":
        form = ApplicationRequestForm(
            request.POST
        )
        form.instance.applicant = request.user
        if form.is_valid():
            form.save()
            redirect('request')
    context = {
        "form": form
    }
    return render(request, 'request.html', context)


@managerdecorator(allowed_roles=['manager'])
def approval(request):
    return render(request, 'manager.html')


@managerdecorator(allowed_roles=['teamleader'])
def allocate(request):
    return render(request, 'allocate.html')
