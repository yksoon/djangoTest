from django.db import models

# Create your models here.


class split_pdf(models.Model):
    origin_file = models.FileField(upload_to='origin/split/')
    completed_file = models.FileField(blank=True, null=True, upload_to='complete/split/')

class merge_pdfs(models.Model):
    origin_file = models.FileField(upload_to='origin/merge/')
    completed_file = models.FileField(blank=True, null=True, upload_to='complete/merge/')

