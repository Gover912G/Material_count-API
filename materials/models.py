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

class DropCable(models.Model):
    name = models.CharField(max_length=100)
    total_length = models.FloatField()  # Length in meters
    purchased_date = models.DateTimeField(auto_now_add=True)

    def use(self, length):
        self.total_length -= length
        self.save()

    def return_item(self, length):
        self.total_length += length
        self.save()

    def __str__(self):
        return self.name

class DropCableUsageRecord(models.Model):
    drop_cable = models.ForeignKey(DropCable, on_delete=models.CASCADE)
    length_before_use = models.FloatField()  # Length in meters
    length_after_use = models.FloatField()  # Length in meters
    used_by = models.CharField(max_length=100)
    used_date = models.DateTimeField(auto_now_add=True)

    @property
    def length_used(self):
        return self.length_before_use - self.length_after_use

    def __str__(self):
        return f"{self.drop_cable.name} used by {self.used_by}"