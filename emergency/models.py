from django.db import models

# Create your models here
class Symx(models.Model):
    MRN_number = models.CharField(max_length=264)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    first_symx = models.CharField(max_length=264)
    second_symx = models.CharField(max_length=264)
    third_symx = models.CharField(max_length=264)
    fourth_symx = models.CharField(max_length=264)
    fifth_symx = models.CharField(max_length=264)
    
    class test(models.Model):
        test = models.CharField(max_length=264)
