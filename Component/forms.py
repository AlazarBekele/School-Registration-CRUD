from django import forms
from .models import Requrement

class FormInput (forms.ModelForm):
  class Meta:
    model = Requrement
    fields = '__all__'

    widget = {
      'first_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'last_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'Dob' : forms.DateInput(attrs={
        'class' : 'form-control',
        'type' : 'Date'
      })
    }