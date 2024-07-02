from django.db import models

# Create your models here.

class Router(models.Model):
    name = models.CharField(Max_lenght=100)
    quantity = models.IntergerField()
    purchased_date = models.DateTimeField(auto_add_now = True)

    def use(self, quantity):
        self.quantity -= quantity
        self.save()
    

    def return_item(self, quantity):
        self.quantity += quantity
        self.save()

    def __str__(self):
        return self.name


class ONU(models.Model):
    name = models.CharField(Max_length= 100)
    quantity = models.IntergerField()
    purchased_date = models.DateTimeField(auto_add_now = True)

    def use(self, quantity):
        self.quantity -= quantity
        self.save()

    def return_item(self, quantity):
        self.quantity += quantity
        self.save()

    def __str__(self):
        return self.name

