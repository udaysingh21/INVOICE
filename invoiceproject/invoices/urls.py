from django.urls import path
from .views import InvoiceListCreateView, InvoiceDetailView, InvoiceDetailCreateView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice-details/', InvoiceDetailCreateView.as_view(), name='invoice-detail-create'),
]
