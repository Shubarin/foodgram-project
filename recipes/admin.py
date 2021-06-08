from django.contrib import admin

from .models import Ingredient, Measurement, Recipe, RecipeIngredient, Tag


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_of_measurement')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')
    ordering = ('recipe',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    fields = ('ingredient', 'quantity')
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'body', 'cooking_time')
    list_filter = ('author', 'title', 'cooking_time', 'tags')
    search_fields = ('title', 'body', 'tags', 'ingredients')
    inlines = (RecipeIngredientInline,)
    raw_id_fields = ('author',)
    ordering = ('-pub_date', 'title', 'cooking_time')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
