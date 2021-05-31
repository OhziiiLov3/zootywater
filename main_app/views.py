from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Customer

# Create your views here.


class Home(TemplateView):
     template_name= "home.html"       

class About(TemplateView):
    template_name = "about.html"


class CustomerProfile(TemplateView):
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Customer.objects.all()
        return context
