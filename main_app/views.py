from django.shortcuts import render,redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Customer , Order, Product
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView  
from django.urls import reverse
from django.views.generic import DetailView
import stripe
from django.conf import settings 
from django.http import JsonResponse


stripe.api_key = settings.STRIPE_SECRET_KEY 



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
    success_url = "/accounts/logout"
    

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
    fields = ['email', 'quantity', 'street_address',
              'city', 'state', 'zip_code']
    template_name = "order_create.html"
    

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super(OrderCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})

   
class OrderDetail(DetailView):
    model = Order
    template_name = "order_detail.html"


class OrderUpdate(UpdateView):
    model = Order
    fields = ['email', 'quantity', 'street_address','city', 'state','zip_code']
    template_name = "order_update.html"

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class OrderDelete(DeleteView):
    model = Order
    template_name = "order_delete_confirmation.html"
    def get_success_url(self):
        return reverse('order_create', kwargs={'pk': self.object.pk})


# STRIPE CHECKOUT 

class SuccessView(TemplateView):
    model = Product
    template_name = "success.html"

class CancelView(TemplateView):
    model = Product
    template_name = "cancel.html"


class CreateCheckoutSessionView(View):
    model = Product
   
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product= Product.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            'images': ['https://media.giphy.com/media/4RgNp8iCLmEjF9Dfsy/giphy.gif'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

class ProductCheckoutView(TemplateView):
    model = Product
    template_name = "checkout.html"
    

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Zooty Water")
        context = super(ProductCheckoutView, self).get_context_data(**kwargs)
        context.update ({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context 


