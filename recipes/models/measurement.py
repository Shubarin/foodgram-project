from django.db import models


class Measurement(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
