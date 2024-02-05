from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("deletecustomer/", views.customer, name="deletecustomer"),
    path("<int:customer_id>/", views.details, name="details"),
]