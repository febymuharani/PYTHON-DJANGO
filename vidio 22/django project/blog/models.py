from django.db import models

# Create your models here.
 
class Post(models.Model):
    judul = models.CharField(max_length=255)
    body = models.TextField()
    kategori = models.CharField(max_length=255)
    waktuPosting = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return "{}. {}".format(self.id, self.judul)