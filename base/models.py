from django.db import models
from django.core.validators import FileExtensionValidator

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
    image = models.ImageField(upload_to="Blog-Images", validators=[FileExtensionValidator(['jpg','png'])])
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    author = models.CharField(max_length=100)
    author_img =  models.ImageField(upload_to="Authors_images", validators=[FileExtensionValidator(['jpg','png'])])
    date = models.DateField(auto_now_add=True)

    class meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title
#Blog comment
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Gallery
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    gallery_image= models.ImageField(upload_to='Gallery_images', validators=[FileExtensionValidator(['jpg','png'])])
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#team members
class Team(models.Model):
    name = models.CharField(max_length=50)
    member_img = models.ImageField(upload_to='Team_images', validators=[FileExtensionValidator(['jpg','png'])])
    description = models.TextField()

    def __str__(self):
        return self.name


