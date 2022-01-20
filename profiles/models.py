from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    tnr = models.CharField(max_length=5)
    age = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

    # img = models.ImageField(uploaded_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    post = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
