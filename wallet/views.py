from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Customer

def index(request):
    customer_list = Customer.objects.all()
    context = {
        "customer_list": customer_list,
    }
    return render(request,"wallet/index.html",context)

def customer(request):
    customer = Customer(name=request.POST["name"],balance=0, modifiedDate=timezone.now())
    customer.save()
    return redirect('/wallet/')