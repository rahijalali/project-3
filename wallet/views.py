from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import Http404
from .models import Customer
from .models import Transaction
import logging

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

def details(request, customer_id):
    logging.debug(customer_id)
    try:
        logging.info("customer_id")
        customer = Customer.objects.get(pk=customer_id)
        transaction_list= Transaction.objects.all().filter(customer_id=customer_id)
    except customer.DoesNotExist:
        raise Http404("customer does not exist")
    return render(request, "wallet/details.html", {"customer": customer,"transaction_list":transaction_list})    

def customerdelete(request):
    customer = Customer.objects.get(id=1)
    customer.delete()
    return redirect('/wallet/')

def customerupdate(request):
    customer = Customer.objects.get(id=1)
    customer.update()
    return redirect('/wallet/')