from django.db import models

class Scrap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model"""
        return self.title
    