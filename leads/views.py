from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    context = {
        "name":"idrice",
        "age":22
    }
    return render(request, 'base.html', context)
