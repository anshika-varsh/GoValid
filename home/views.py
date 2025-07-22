from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/landing.html")

def contact(request):
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")