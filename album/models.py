from django.db import models
from musician.models import Musician

from django.utils import timezone
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name of the album.")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(default=timezone.now, help_text="Enter the release date.")
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    
    def __str__(self) -> str:
        return f'{self.name}'