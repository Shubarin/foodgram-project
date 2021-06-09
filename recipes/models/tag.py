from django.db import models


class TagChoices(models.TextChoices):
    BREAKFAST = ('breakfast', 'Breakfast')
    LUNCH = ('lunch', 'Lunch')
    DINNER = ('dinner', 'Dinner')


class Tag(models.Model):
    name = models.CharField(max_length=32, choices=TagChoices.choices,
                            unique=True, verbose_name='Название')
    show_name = models.CharField(max_length=32,
                                 verbose_name='Отображаемое имя')
    color = models.CharField(max_length=50, blank=True, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

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
