from django.shortcuts import render
from .models import Requrement
# Create your views here.

def index (request):
    write = Requrement.objects.all()

    context = {
        'write': write
    }

    return render (request, 'index.html' , context=context)