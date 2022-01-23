import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    cat_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.cat_name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Detail(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sex = models.CharField(max_length=3)
    tnr = models.CharField(max_length=3)
    birthday = models.CharField(max_length=20)

