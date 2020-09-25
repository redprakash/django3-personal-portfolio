from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/images/')
    date = models.DateField()
    objects = models.Manager()

    #  this returns the title in the backend
    def __str__(self):
        return self.title
