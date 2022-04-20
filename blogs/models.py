from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogArticle(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=50,blank=False)
    para1 = models.TextField(max_length=500,blank=False)
    para2 = models.TextField(max_length=500,blank=False)
    para3 = models.TextField(max_length=500,blank=False)
    image = models.ImageField(upload_to='pics',blank=True)
    date  = models.DateTimeField(auto_now_add=True)