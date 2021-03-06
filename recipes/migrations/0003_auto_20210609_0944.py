# Generated by Django 3.2.3 on 2021-06-09 09:44

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipes.models.recipe


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'Ингредиент рецепта', 'verbose_name_plural': 'Ингредиенты рецепта'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(db_index=True, max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit_of_measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='recipes.measurement', verbose_name='Единицы измерения'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='body',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/recipes/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='recipes.Ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, editable=False, max_length=256, populate_from='title', slugify=recipes.models.recipe.translate_slugify, unique_with=('author__username',), verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=1, max_digits=6, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredient', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=32, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='show_name',
            field=models.CharField(max_length=32, verbose_name='Отображаемое имя'),
        ),
    ]
