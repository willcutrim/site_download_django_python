from django.db import models

class link(models.Model):
    link = models.CharField(max_length=155, blank=True, null=True)
