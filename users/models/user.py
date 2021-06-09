from django.contrib.auth.models import AbstractUser
from django.db import models

from . import Contact


class User(AbstractUser):
    following = models.ManyToManyField('self',
                                       through=Contact,
                                       related_name='followers',
                                       symmetrical=False,
                                       verbose_name='Подписки')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return '{}: {}'.format(self.username, self.email)
