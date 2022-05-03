from django.db import models
import datetime


    

class event(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    desc= models.TextField(max_length=200, default="")
    rule = models.TextField(default="")
    judging = models.TextField( default="")
    name_of_coordinator_1 = models.CharField(max_length = 200, default="")
    contact_number_of_coordinator_1 = models.CharField(max_length=50,default="")
    email_of_coordinator_1 = models.CharField(max_length=100,default="")
    coordinator_1_profile = models.ImageField(upload_to='static/',default="")
    name_of_coordinator_2 = models.CharField(max_length = 200, default="")
    contact_number_of_coordinator_2 = models.CharField(max_length=50,default="")
    email_of_coordinator_2 = models.CharField(max_length=100,default="")
    coordinator_2_profile = models.ImageField(upload_to='static/',default="")
    event_images = models.ImageField(upload_to='static/')
    sc_group_link = models.CharField(max_length=200,default="")
    venu = models.CharField( max_length=100,default="" )
    reg_url = models.CharField( max_length=500,default="" )

   

    def __str__(self):
        return self.title

class banner(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    desc= models.CharField(max_length = 50, default="")
    images = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.title

class winners(models.Model):
    player_name = models.CharField(max_length=50)
    player_profile = models.ImageField(upload_to='static/')
    event_name = models.CharField( max_length=50)
    desc = models.CharField( max_length=50)
    social_link = models.CharField( max_length=200)

    def __str__(self):
        return self.player_name
