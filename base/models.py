from django.conf import settings
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class Membership(models.Model):
    SKILLS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    
    name = models.CharField(max_length=200)
    ID_number = models.CharField(max_length=13)
    PO_box = models.TextField()
    cell_number = models.CharField(max_length=13)
    previous_clubs = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    skill_level = models.CharField(max_length=20, choices=SKILLS, blank=True)

    def __str__(self):
        return self.email


class Calendar(models.Model):
    title = models.CharField(max_length=200)
    comments = models.TextField(blank=True, null=True)
    URL = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title