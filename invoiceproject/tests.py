from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(APITestCase):
    def setUp(self):
        # Create test data
        self.invoice = Invoice.objects.create(date='2023-01-01', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Description',
            quantity=2,
            unit_price=10.0,
            price=20.0
        )

    def test_get_invoices(self):
        url = reverse('invoice-list-create')  # Replace with your actual endpoint name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Add more assertions to check the response content

    def test_get_single_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Add more assertions to check the response content

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        data = {
            'date': '2023-12-31',
            'customer_name': 'New Test Customer'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)  # Assuming successful creation returns 201

        # Add assertions to check if the invoice was created correctly

    def test_update_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        data = {
            'date': '2023-01-02',  # Updated date
            'customer_name': 'Updated Customer Name'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

        # Add assertions to check if the invoice was updated correctly

    def test_delete_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)  # Assuming successful deletion returns 204

        # Add assertions to check if the invoice was deleted correctly

    def test_create_invoice_with_details(self):
        url = reverse('invoice-list-create')
        data = {
            'date': '2023-12-31',
            'customer_name': 'New Test Customer',
            'invoice_details': [
                {
                    'description': 'Test Description 1',
                    'quantity': 3,
                    'unit_price': 15.0,
                    'price': 45.0
                },
                {
                    'description': 'Test Description 2',
                    'quantity': 1,
                    'unit_price': 20.0,
                    'price': 20.0
                }
                # Add more invoice details if needed
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  # Assuming successful creation returns 201

        # Add assertions to check if the invoice and associated invoice details were created correctly

    def test_update_invoice_with_details(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        data = {
            'date': '2023-01-02',  # Updated date
            'customer_name': 'Updated Customer Name',
            'invoice_details': [
                {
                    'id': self.invoice_detail.id,  # Existing invoice detail ID
                    'description': 'Updated Description',
                    'quantity': 5,
                    'unit_price': 18.0,
                    'price': 90.0
                }
                # Add more updated invoice details if needed
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        # Add assertions to check if the invoice and associated invoice details were updated correctly
