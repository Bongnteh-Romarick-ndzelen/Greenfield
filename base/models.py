from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    number = models.IntegerField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LiveChat(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    message = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    image = models.ImageField(upload_to="Blog-Images")
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    author = models.CharField(max_length=100)
    author_img =  models.ImageField(upload_to="Authors_images")
    date = models.DateField(auto_now_add=True)

    class meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title
