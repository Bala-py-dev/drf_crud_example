from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
