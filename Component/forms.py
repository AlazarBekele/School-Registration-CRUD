from django import forms
from .models import Requrement

class FormInput (forms.ModelForm):
  class Meta:
    model = Requrement
    fields = '__all__'

    widgets = {
      'first_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'last_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'Dob' : forms.DateInput(attrs={
        'class' : 'form-control',
        'type' : 'Date'
      }),
      'grade' : forms.NumberInput(attrs={
        'class' : 'form-control',
        'type' : 'Number'
      }),
      'image' : forms.ClearableFileInput(attrs={
        'class' : 'form-control',
        'id' :'formFileMultiple',
        'type' : 'file'
      })
    }