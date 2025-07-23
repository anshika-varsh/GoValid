from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Validate_form
# Create your views here.
@login_required
def dashboard(request):
    if request.method=="POST":
        startup_idea = request.POST.get("startup_idea")
        business_domain = request.POST.get("business_domain")
        problem_statement = request.POST.get("problem_statement")

        business_goal = request.POST.get("business_goal")
        monetization_strategy = request.POST.get("monetization_strategy")
        social_impact = request.POST.get("social_impact")
        timeline = request.POST.get("timeline")
# ========================================================Creating an object=============================================================
        form = Validate_form(
            startup_idea=startup_idea,
            business_domain=business_domain,
            problem_statement=problem_statement,
            business_goal=business_goal,
            monetization_strategy=monetization_strategy,
            social_impact=social_impact,
            timeline=timeline
        )
        form.save()
        return redirect("dashboard")
    
    return render(request,"dashboard/dashboard.html")