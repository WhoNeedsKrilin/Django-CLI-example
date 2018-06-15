from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    baranggay = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


    def __str__(self):
        return self.city

class Resident(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default="")
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    @property
    def full_name(self):
        return self.first_name+" "+self.last_name

    def __str__(self):
        return self.full_name
