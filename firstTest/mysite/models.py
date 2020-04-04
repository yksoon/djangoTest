from django.db import models

# Create your models here.

class BlogModel(models.Model):
    content = models.CharField(max_length=50, verbose_name = "내용")
    who = models.CharField(max_length=20, verbose_name = "글쓴이")
    