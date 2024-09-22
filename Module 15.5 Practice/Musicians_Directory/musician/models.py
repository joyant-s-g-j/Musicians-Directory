from django.db import models

# Create your models here.
class Musician(models.Model):
    fst_name = models.CharField(max_length=50)
    lst_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=12)
    insturment = models.CharField(max_length=50)

    def __str__(self):
        return self.fst_name
    