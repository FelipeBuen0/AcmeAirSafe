from django.db import models
from django.contrib.auth.models import User

class Bag(models.Model):
    bag_id = models.AutoField(primary_key=True)
    number_identification = models.CharField(max_length=100)
    weight = models.FloatField()
    destiny = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Load(models.Model):
    load_id = models.AutoField(primary_key=True)
    type_of_merch = models.CharField(max_length=100)
    weight = models.FloatField()
    destiny = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Location(models.Model):
    lcoation_id = models.AutoField(primary_key=True)
    bag_id = models.ForeignKey(Bag, on_delete=models.CASCADE)
    load_id = models.ForeignKey(Load, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    receiver = models.CharField(max_length=100)
    content = models.TextField()
    hour = models.DateTimeField()

class Occurrence(models.Model):
    occurrence_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    bag_id = models.ManyToManyField(Bag)

class Recovery(models.Model):
    recovery_id = models.AutoField(primary_key=True)
    bag_id = models.ForeignKey(Bag, on_delete=models.CASCADE)
    passenger = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    occurrence_id = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class Employee(User):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Role(models.TextChoices):
        BAG_LOADER = 'BL'
        OVERSEER = 'OS'
        SERVICE_AGENT = 'SA' # Service for the clients and the manager
        MANAGER = 'MA'
    role = models.CharField(
        max_length=2,
        choices=Role.choices
    )
    user_ptr = models.OneToOneField(
        to='auth.User', 
        parent_link=True, 
        related_name='Employee',
        on_delete=models.CASCADE
    )
    sector = models.CharField(max_length=100)
    access_level = models.CharField(max_length=100)

class Passenger(User):
    passenger_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    bag_id = models.ManyToManyField(Bag)
    occurrence_id = models.ForeignKey(Occurrence, on_delete=models.CASCADE)
    