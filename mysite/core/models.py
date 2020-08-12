from django.db import models


# Create your models here.
class Pdfs(models.Model):
    university = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.pdf.name

    objects = models.Manager()
