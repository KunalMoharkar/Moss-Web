from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # github = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=100,blank=True)
    fb = models.CharField(max_length=100,blank=True)
    insta = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.first_name

class Blog(models.Model):
    heading = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    likes = models.IntegerField(default=0)
    content = models.TextField()
    image = models.FileField(upload_to="blogs", default='img_avatar.jpg') # add some default image to this
    def __str__(self):
        return self.heading