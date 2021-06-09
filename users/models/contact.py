from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE,
                                  verbose_name='Подписчик')
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='rel_to_set',
                                on_delete=models.CASCADE,
                                verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-created',)
        constraints = [
            models.UniqueConstraint(
                fields=['user_from', 'user_to'], name='unique_follow')
        ]

    def clean(self, *args, **kwargs):
        if self.user_to == self.user_from:
            raise ValidationError('it is forbidden to subscribe to yourself')
        super(Contact, self).clean()

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)
