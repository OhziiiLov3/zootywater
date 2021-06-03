from django.shortcuts import render,redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Customer , Order
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView  
from django.urls import reverse
from django.views.generic import DetailView



# Create your views here.


class Home(TemplateView):
     template_name= "home.html"       

class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class CustomerProfile(TemplateView):

    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.customer
        return context

class CustomerProfileUpdate(UpdateView):
    model = Customer
    fields = ['name', 'email', 'is_subscribe']
    template_name = "profile_update.html"
    success_url = "/profile/"


class CustomerSubscribeUpdate(UpdateView):
    model = Customer
    fields = ['name', 'email']
    template_name = "profile_update.html"
    success_url = "/profile/"

class CustomerProfileDelete(DeleteView):
    model = Customer
    template_name = "profile_delete_confirmation.html"
    success_url = "/"
    

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        name = request.POST.get("name")
        email = request.POST.get("email")

        if form.is_valid():
            user = form.save()
            Customer.objects.create(name=name, email=email, user=user)
            login(request,user)
            return redirect("profile_detail")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# Order Model 


@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):

    model = Order 
    fields = ['email', 'quantity']
    template_name = "order_create.html"
    

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super(OrderCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

   
class OrderDetail(DetailView):
    model = Order
    template_name = "order_detail.html"


