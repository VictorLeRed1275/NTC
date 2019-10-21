from django import forms
from .models import *

SKILLS = (
    ('', 'Choose level...'),
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advanced'),
)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')

class MembershipForm(forms.ModelForm):
    skill_level = forms.ChoiceField(choices=SKILLS, required=False)
    terms_and_guidelines = forms.BooleanField(required=True)

    class Meta:
        model = Membership
        fields = ('name', 'email', 'cell_number', 'ID_number', 'PO_box', 'skill_level', 'previous_clubs', 'terms_and_guidelines')

class CalendarForm(forms.ModelForm):

    class Meta:
        model = Calendar
        fields = ('title', 'comments', 'URL' , 'start_time', 'end_time')

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'start_time', 'end_time')