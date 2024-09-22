from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    albm_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    RATING_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.albm_name
    