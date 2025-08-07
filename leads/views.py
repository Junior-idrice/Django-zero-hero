from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm

def landing(request):
    return render(request, 'landing.html')

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
    form = LeadModelForm()
    if request.method == "POST":
        print("received")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("form valid")
            print(form.cleaned_data)
            form.save()
            print("lead created")
            return redirect('/')
    context = {
        "form":form
    }
    return render(request, "leads/lead_create.html",context)

def update(request,pk):
    lead= Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form =LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "lead":lead,
        "form":form
    }
    return render(request,'leads/update.html',context)

def delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')
