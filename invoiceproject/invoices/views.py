from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'invoices/home.html')

from .models import  Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer
from rest_framework import viewsets,generics

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer


class InvoiceDetailCreateView(generics.ListCreateAPIView):
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer