from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(request):
    return render(request, 'base/home.html', {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'base/contact.html', {'form': form})

def member(request):
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MembershipForm()
    return render(request, 'base/join.html', {'form': form})

def guide(request):
    return render(request, 'base/join_guide.html', {})

def admin(request):
    return render(request, 'base/admin.html', {})

def calendar_new(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('calendar')
    else:
        form = CalendarForm()
    return render(request, 'base/calendar_new.html', {'form': form})

def calendar(request):
    posts = Calendar.objects.all()
    return render(request, 'base/calendar.html', {'posts': posts})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    else:
        form = EventForm()
    return render(request, 'base/event_new.html', {'form': form})