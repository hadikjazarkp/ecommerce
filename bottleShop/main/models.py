from django.db import models

# Create your models here.
class catogory(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
    
    def __str__(self):
        return self.title
