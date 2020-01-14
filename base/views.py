from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'base/home.html', {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            subject = post.subject
            message = post.message
            email = post.email
            post.save()
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
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

@login_required
def admin(request):
    contacts = Contact.objects.all()
    members = Membership.objects.all()
    return render(request, 'base/admin.html', {
        'contacts': contacts,
        'members': members
    })

@login_required
def calendar_new(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = CalendarForm()
    return render(request, 'base/calendar_new.html', {'form': form})

def calendar(request):
    posts = Calendar.objects.all()
    return render(request, 'base/calendar.html', {'posts': posts})

@login_required
def event_remove(request, pk):
    post = get_object_or_404(Event, pk=pk)
    post.delete()
    return redirect('event')

@login_required
def calendar_remove(request, pk):
    post = get_object_or_404(Calendar, pk=pk)
    post.delete()
    return redirect('calendar')

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event')
    else:
        form = EventForm()
    return render(request, 'base/event_new.html', {'form': form})

def event(request):
    posts = Event.objects.all()
    return render(request, 'base/event.html', {'posts': posts})

@login_required
def event_remove(request, pk):
    post = get_object_or_404(Event, pk=pk)
    post.delete()
    return redirect('event')

@login_required
def gallery_new(request):
    if request.method =="POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryForm()
    return render(request, 'base/gallery_new.html', {'form': form})

def gallery(request):
    posts = []
    posts += Event.objects.all()
    posts += Gallery.objects.all()
    return render(request, 'base/gallery.html', {'posts': posts})
