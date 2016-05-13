from django.contrib.auth.models import User
from django.db.models import Q
import models
from django import forms
from django.forms import ModelForm
from projet2.notes.models import Event




class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()



class EventForm(forms.ModelForm):
    class Meta:
        model = Event

    
