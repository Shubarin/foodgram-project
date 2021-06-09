from django.db import models


class Measurement(models.Model):
    name = models.CharField(max_length=32, unique=True,
                            verbose_name='Название')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.name
