from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    # if request.method=="POST":
    #     startup_idea = request.POST.get("startup_idea")
    #     business_domain = request.POST.get("business_domain")
    #     problem_statement = request.POST.get("problem_statement")

    #     business_goal = request.POST.get("business_goal")
    #     monetization_strategy = request.POST.get("monetization_strategy")
    #     social_impact = request.POST.get("social_impact")
    #     timeline = request.POST.get("timeline")
        
    #     dashboard.save()

    return render(request,"dashboard/dashboard.html")