from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Confirmed
from .forms import ConfirmedForm, FOCForm, EnquiryForm
from django.contrib.auth.models import User
from django.db.models import Count
# Create your views here.
@login_required( login_url='user_login')
def home(request):
    confirmed = Confirmed.objects.all()
    context = {
        'confirmed':confirmed
    }
    return render(request, "Dashboard/home.html", context)


@login_required( login_url='user_login')
def Staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    context = {
        'workers': workers,
        'workers_count': workers_count
    }
    return render(request, "Dashboard/staff.html", context)

def Staff_detail(request, pk):
    staffs = User.objects.get(id=pk)
    return render(request, "Dashboard/Staff_detail.html", {'staffs':staffs})

@login_required( login_url='user_login')
def enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EnquiryForm()

    context = {
        'form': form
    }
    return render(request, "Dashboard/Enquiry.html", context)

@login_required( login_url='user_login')
def confirmed(request):
    distinct_confirmed = Confirmed.objects.values('sector').distinct()
    confirmed = Confirmed.objects.all()
    confirmed_count = confirmed.count()
    sector_count = (
        Confirmed.objects.values('sector')
        .annotate(count=Count('sector'))
    )
    if request.method == "POST":
        form = ConfirmedForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConfirmedForm()
    
    context = {
        'confirmed': confirmed,
        'form': form,
        'confirmed_count':confirmed_count,
        'sector_count': sector_count
    }
    print(sector_count)
    return render(request, "Dashboard/Confirmed.html", context)

def confirmed_delete(request, pk):
    confirmed = Confirmed.objects.get(id=pk)
    if request.method == "POST":
        confirmed.delete()
        return redirect('Confirmed')
    
    return render(request, "dashboard/Confirmed_delete.html", {'confirmed':confirmed})


def confirmed_edit(request, pk):
    confirmed = Confirmed.objects.get(id=pk)
    if request.method == "POST":
        form = ConfirmedForm(request.POST, instance = confirmed)
        if form.is_valid():
            form.save()
            return redirect('Confirmed')
    
    else:
        form = ConfirmedForm(instance= confirmed)
    
    context = {
        'confirmed':confirmed,
        'form':form
    }

    return render(request, 'dashboard/Confirmed_edit.html', context)


def foc(request):
    if request.method == "POST":
        form = FOCForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = FOCForm()
    
    return render(request, "Dashboard/FOC.html", {'form':form})