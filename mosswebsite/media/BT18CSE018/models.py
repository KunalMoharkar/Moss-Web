from datetime import datetime

from django.db import models
from django.db.models.fields import DateTimeField
# Create your models here.
from accounts.models import Manager, Participant


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to="competition_categories")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Event(models.Model):
    types = [
        ('WRK','Workshop'),
        ('EXB','Exhibition'),
        ('LEC','Lecture'),
        ('COMP','Competition')
    ]
    type = models.CharField(max_length=5,choices=types)  # string (WORKSHOP,LECTURE,COMPETITION etc)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rules = models.TextField(null=True)
    image = models.FileField(upload_to="events")
    date = models.DateField()
    venue = models.CharField(max_length=40)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fees_vnit = models.IntegerField()
    fees_non_vnit = models.IntegerField()
    google_form_link = models.CharField(max_length=100)
    last_registration_date = models.DateField()
    managers = models.ManyToManyField(Manager)

    def __str__(self):
        return self.title


class Workshop(models.Model):
    event = models.OneToOneField(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


class Exhibition(models.Model):
    event = models.OneToOneField(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


class Lecture(models.Model):
    event = models.OneToOneField(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title


class Competition(models.Model):
    event = models.OneToOneField(Event,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    document = models.FileField(upload_to="competition_docs")
    structure = models.TextField()
    num_participants = models.IntegerField()

    def __str__(self):
        return self.event.title


class Registration(models.Model):
    participants = models.ManyToManyField(Participant)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    date_of_reg = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return f"{self.event.title}"