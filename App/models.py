from django.db import models

class Carousel(models.Model):
  image = models.ImageField(upload_to='pics')
  title = models.CharField(max_length=100)
  heading = models.CharField(max_length=100)
  description = models.TextField()
  
  
class Courses(models.Model):
  
  img = models.ImageField(upload_to='pics')
  price = models.IntegerField()
  rate = models.IntegerField()
  title = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  time = models.CharField(max_length=100)
  num_stu = models.IntegerField()
  
  
class Expert(models.Model):
  img = models.ImageField(upload_to='pics')
  fb = models.URLField()
  tw = models.URLField()
  ig = models.URLField()
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  
  
class Testimonials(models.Model):
  img = models.ImageField(upload_to='pics')
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  desc = models.TextField()