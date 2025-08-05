from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Lead,Agent
from .forms import LeadForm

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
    form = LeadForm()
    if request.method == "POST":
        print("received")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("form valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )
            print("lead created")
            return redirect('/')
    context = {
        "form":form
    }
    return render(request, "leads/lead_create.html",context)