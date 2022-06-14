from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from django.db.models import Avg


from .serializers import UserSerializer, InvoiceSerializer
from .models import User, Invoice


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


def total_paid_invoices(request):
    paid_invoices = Invoice.objects.filter(is_paid=True)
    total = sum([invoice.price for invoice in paid_invoices])
    return HttpResponse(total)


def average_invoices_price(request):
    paid_invoices = Invoice.objects.filter(
        is_paid=True).filter(price__gt=5000000).aggregate(Avg('price'))
    # paid_invoices_length = Invoice.objects.filter(is_paid=True).count()
    # total = sum([invoice.price for invoice in paid_invoices])
    return HttpResponse(paid_invoices['price__avg'])
