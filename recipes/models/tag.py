from django.db import models


class Tag(models.Model):
    choices = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),)
    name = models.CharField(max_length=32, choices=choices, unique=True)
    show_name = models.CharField(max_length=32)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        colors = {'breakfast': 'orange', 'lunch': 'green', 'dinner': 'purple'}
        color = colors.get(str(self.name), 'blue')
        names = {'breakfast': 'Завтрак', 'lunch': 'Обед', 'dinner': 'Ужин'}
        show_name = names.get(str(self.name))
        self.color = color
        self.show_name = show_name
        super(Tag, self).clean()

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Tag, self).save(*args, **kwargs)
