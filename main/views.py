from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    title = "Hello there...."
    return render(request, "home.html", {"title": title})

def about(request):
    return render(request, "about.html", {"title": "About"})

def contact(request):
    return render(request, "contact.html", {"title": "Contact Information"})
