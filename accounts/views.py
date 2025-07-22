from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
# ===========================================Register==============================================
def register(request):
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

# ====================================Object============================================================
        new_user = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
)
        new_user.set_password(password)  #Setting the password for the user in an encrpted
        new_user.save()
        return redirect("dashboard")
    return render(request,"accounts/register.html")

# ==================================Login==================================================
def login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request,username=username , password=password)
        if user is not None :
            auth.login(request,user)
            return redirect("dashboard")
        
    return render(request,"accounts/login.html")