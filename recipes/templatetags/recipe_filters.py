from django import template

register = template.Library()


@register.filter
def add_class(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def favorite_by(recipe, user):
    return user.favorites.filter(recipe=recipe).exists()


@register.filter
def translate_verbose_name(num):
    last_two_digits = num % 100
    last_digit = num % 10
    if 5 <= last_two_digits <= 20 or last_two_digits in {0, 5, 6, 7, 8, 9}:
        return f'{num} рецептов'
    if last_digit in {2, 3, 4}:
        return f'{num} рецепта'
    return f'{num} рецепт'
