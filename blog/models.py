from audioop import maxpp
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=250, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    desc = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)