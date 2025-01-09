from django.db import models
from django.utils.timezone import now


class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    reference_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


from django.db import models

class Billboard(models.Model):
    location = models.CharField(max_length=255)
    coordinates = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="Enter latitude and longitude in the format: 'latitude,longitude'"
    )
    rented_by = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.location} - {'Paid' if self.is_paid else 'Unpaid'}"

class Payment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=now)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.company.name} - {self.amount} - {self.date.strftime('%Y-%m-%d')}"
