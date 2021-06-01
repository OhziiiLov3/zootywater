from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Customer
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.


class Home(TemplateView):
     template_name= "home.html"       

class About(TemplateView):
    template_name = "about.html"


class CustomerProfile(TemplateView):

    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Customer.objects.get()
        return context

class CustomerProfileUpdate(UpdateView):
    model = Customer
    fields = ['name', 'email', 'join_date', 'is_subscribe']
    template_name = "profile_update.html"
    success_url = "/profile/"

class CustomerProfileDelete(DeleteView):
    model = Customer
    template_name = "profile_delete_confirmation.html"
    success_url = "/profile/"
    
