from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100, help_text="Enter the first name.")
    last_name = models.CharField(max_length=100, help_text="Enter the last name.")
    email = models.EmailField(max_length=100, help_text="Enter the email address.")
    phone_number = models.CharField(max_length=100, help_text="Enter the phone number.")
    instrument_type = models.CharField(max_length=100, help_text="Enter the instrument type.")
    
    def __str__(self) -> str:
        return f'{self.first_name}'