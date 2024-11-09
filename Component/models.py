from django.db import models

# Create your models here.

class Departement (models.Model):

  name = models.CharField (max_length=30)
  Discribe = models.TextField (blank=True)

  def __str__(self) -> str:
    return self.name


class Requrement(models.Model):
  first_name = models.CharField (max_length=20)
  last_name = models.CharField (max_length=30)
  Dob = models.DateField (auto_now=False, auto_now_add=False)
  grade = models.IntegerField ()
  departement = models.ForeignKey(Departement, on_delete=models.SET_NULL,null=True)

  def __str__(self) -> str:
    return self.first_name + " " + self.last_name