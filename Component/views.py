from django.shortcuts import render
from .models import Requrement
from .forms import FormInput
# Create your views here.

def index (request):

    form = FormInput (request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = FormInput()
    write = Requrement.objects.all()

    context = {
        'write': write,
        'form' : form
    }

    return render (request, 'index.html' , context=context)