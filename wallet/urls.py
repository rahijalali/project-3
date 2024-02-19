from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("addtransaction/", views.addtransaction, name="addtransaction"),
    path("voidtransaction/", views.voidtransaction, name="voidtransaction"),
    path("customerupdate/", views.customerupdate, name="customerupdate"),
    path("customerdelete/<int:customerId>", views.customerdelete, name="customerdelete"),
    path("<int:customer_id>/", views.details, name="details"),
]
