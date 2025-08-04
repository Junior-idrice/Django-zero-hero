from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Lead

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "names":leads
    }
    return render(request, 'base.html', context)
