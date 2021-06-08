from django.db import models

from . import Measurement


class Ingredient(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    unit_of_measurement = models.ForeignKey(Measurement,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='ingredients')

    class Meta:
        ordering = ('name',)
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'unit_of_measurement'],
                name='unique_ingredient')
        ]

    def __str__(self):
        return f'{self.name}, {self.unit_of_measurement}'
