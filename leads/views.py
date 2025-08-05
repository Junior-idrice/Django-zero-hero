from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Lead

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, 'leads/layout.html', context)

def lead_details(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context={
        "lead":lead
    }
    print(lead)
    return render(request, 'leads/details.html',context)

def lead_create(request):
    return render(request, "leads/lead_create.html")