from django.db import models
# Create your models here.

class BoardModel(models.Model):
    title= models.CharField(max_length = 100)
    keyword = models.CharField(max_length = 200)
    content = models.TextField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length = 400, null=True, blank=True, default='a')

