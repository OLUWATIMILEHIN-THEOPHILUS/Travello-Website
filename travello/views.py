from django.shortcuts import render
from .models import Destination     

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'Dests': dests})


def destination(request, name):
    dest = Destination.objects.get(name=name)
    context = {'dest':dest}
    return render(request, 'destination.html', context)