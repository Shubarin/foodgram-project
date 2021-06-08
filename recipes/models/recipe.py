from autoslug import AutoSlugField
from django.db import models
from slugify import slugify

from . import Ingredient


def translate_slugify(value):
    return slugify(value)


class Recipe(models.Model):
    author = models.ForeignKey('users.User',
                               on_delete=models.CASCADE,
                               related_name='recipes', )
    title = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='title', max_length=256,
                         slugify=translate_slugify,
                         allow_unicode=True, unique_with='author__username')
    image = models.ImageField(upload_to='static/images/recipes/%Y/%m/%d',
                              blank=True)
    body = models.TextField()
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredient')
    tags = models.ManyToManyField('Tag', related_name='recipes')
    cooking_time = models.PositiveSmallIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                    blank=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)
