from django.db import models
# Create your models here.
class Blog_detail(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    Firstname = models.CharField(max_length=400)
    Lastname = models.CharField(max_length=400)
    email = models.EmailField(max_length=100, blank=True, unique=True)


    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    message=models.TextField()

    def __str__(self):
        return self.email
