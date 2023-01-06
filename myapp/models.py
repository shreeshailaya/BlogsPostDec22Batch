from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, )
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=40)
    publisher = models.CharField(max_length=100)
    no_lines = models.IntegerField()
    img = models.ImageField(upload_to='images/', default='default.png')


    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.comment

