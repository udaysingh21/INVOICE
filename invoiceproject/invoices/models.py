from django.db import models

# Create your models here.


class Invoice(models.Model):
    date=models.DateField()
    customer_name=models.CharField(max_length=200)

class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=3)
    price=models.DecimalField(max_digits=10,decimal_places=3)

