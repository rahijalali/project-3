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
    
def addtransaction(request):
    customer= Customer.objects.get(pk=request.POST["customerId"])
    tr=Transaction(customer=customer, credit=request.POST["credit"], debit=request.POST["debit"],modifiedDate=timezone.now())
    tr.save()
    customer.balance=customer.balance+int(request.POST["credit"])- int(request.POST["debit"])
    customer.save()
    return redirect('/wallet/' + request.POST["customerId"])
    
def voidtransaction(request):
    tr= Transaction.objects.get(pk=request.POST["transactionId"])
    customer= Customer.objects.get(pk=tr.customer.id)
    voidTr=Transaction(customer= tr.customer, debit=tr.credit, credit=tr.debit,modifiedDate=timezone.now())
    voidTr.save()
    customer.balance=customer.balance+int(request.POST["credit"])- int(request.POST["debit"])
    customer.save()
    return redirect('/wallet/' + str(tr.customer.id))
    
def customer(request):
    customer = Customer(name=request.POST["name"],balance=0, modifiedDate=timezone.now())
    customer.save()
    return redirect('/wallet/' )

def details(request, customer_id):
    logging.debug(customer_id)
    try:
        logging.info("customer_id")
        customer = Customer.objects.get(pk=customer_id)
        transaction_list= Transaction.objects.all().filter(customer_id=customer_id)
    except customer.DoesNotExist:
        raise Http404("customer does not exist")
    return render(request, "wallet/details.html", {"customer": customer,"transaction_list":transaction_list})    

def customerdelete(customerId):
    logging.info(customerId)
    customer = Customer.objects.get(pk=5)
    customer.delete()
    return redirect('/wallet/' + str(5))

def customerupdate(request):
    customer= Customer.objects.get(pk=request.POST["customerId"]) 
    customer.name=request.POST["name"]
    customer.balance=request.POST["balance"]
    customer.save()
    return redirect('/wallet/' + request.POST["customerId"])
