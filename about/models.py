from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/', default='default_image.jpg')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()



    def __str__(self):
        return self.title