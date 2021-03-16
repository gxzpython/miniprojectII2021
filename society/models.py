from django.db import models

# Create your models here.

class People(models.Model):
    about_me = models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    fav_movies = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=100,unique=True)
    members = models.IntegerField()
    description = models.TextField()
    category =models.TextField()
    website_url= models.URLField(max_length=200)
    creater = models.ForeignKey(People,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    description= models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    location =models.CharField(max_length=100)
    event_title =models.CharField(max_length=100)
    creater = models.ForeignKey(People,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.event_title






