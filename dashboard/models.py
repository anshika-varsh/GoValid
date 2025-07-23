from django.db import models

# Create your models here.

DOMAIN_CHOICES = [
    ('TECH', 'Technology & Software'),
    ('HEALTH', 'Healthcare & Medical'),
    ('EDTECH', 'Education & EdTech'),
    ('FINTECH', 'Finance & FinTech'),
    ('ECOM', 'E-commerce & Retail'),
    ('FOOD', 'Food & Beverage'),
    ('LOGISTICS', 'Transportation & Logistics'),
    ('ENV', 'Sustainability & Environment'),
    ('MEDIA', 'Entertainment & Media'),
    ('OTHER', 'Other'),
]

class Validate_form(models.Model):
    startup_idea = models.TextField()
    business_domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)
    problem_statement = models.TextField()

    business_goal = models.TextField()
    monetization_strategy = models.TextField()
    social_impact = models.TextField()
    timeline = models.TextField()