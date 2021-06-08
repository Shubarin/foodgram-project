from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse

from foodgram.settings import RECORDS_ON_THE_PAGE
from recipes.forms.create_recipe import RecipeForm
from recipes.models import Recipe, Tag
from recipes.utils import save_recipe
from users.models import User

TAGS = ['breakfast', 'lunch', 'dinner']


def home(request):
    tags = request.GET.getlist('tags', TAGS)
    all_tags = Tag.objects.all()
    recipes = Recipe.objects.filter(tags__name__in=tags).distinct()
    paginator = Paginator(recipes, RECORDS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page': page,
        'tags': tags,
        'all_tags': all_tags,
    }
    return render(request, 'index.html', context)


def recipe_detail(request, slug, user_id):
    recipe = get_object_or_404(Recipe, slug=slug, author__pk=user_id)
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)


@login_required
def create_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        recipe = save_recipe(request, form)
        return redirect(reverse('recipe_detail',
                                kwargs={'slug': recipe.slug,
                                        'user_id': recipe.author.pk}))
    return render(request, 'form_recipe.html', {'form': form})


@login_required
def edit_recipe(request, slug, user_id):
    recipe = get_object_or_404(Recipe, slug=slug, author__pk=user_id)
    if request.user != recipe.author and not request.user.is_superuser:
        return redirect(reverse('home'))
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None,
                      instance=recipe)
    if form.is_valid():
        author = recipe.author
        recipe = save_recipe(request, form, author, is_edit=True)
        return redirect(reverse('recipe_detail',
                                kwargs={'slug': recipe.slug,
                                        'user_id': recipe.author.pk}))
    return render(request, 'form_recipe.html', {'form': form,
                                                'recipe': recipe})


@login_required
def recipe_delete(request, slug, user_id):
    recipe = get_object_or_404(Recipe, slug=slug, author__pk=user_id)
    if request.user != recipe.author and not request.user.is_superuser:
        return redirect(reverse('home'))
    recipe.delete()
    return redirect(reverse('home'))


def profile(request, user_id):
    tags = request.GET.getlist('tags', TAGS)
    all_tags = Tag.objects.all()
    author = get_object_or_404(User, pk=user_id)
    recipes = Recipe.objects.filter(author__pk=user_id,
                                    tags__name__in=tags).distinct()
    paginator = Paginator(recipes, RECORDS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page': page,
        'tags': tags,
        'all_tags': all_tags,
        'author': author
    }
    return render(request, 'profile.html', context)


@login_required
def favorites(request):
    tags = request.GET.getlist('tags', TAGS)
    all_tags = Tag.objects.all()
    recipes = Recipe.objects.filter(favorite_by__user=request.user,
                                    tags__name__in=tags).distinct()
    paginator = Paginator(recipes, RECORDS_ON_THE_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'paginator': paginator,
        'page': page,
        'tags': tags,
        'all_tags': all_tags,
    }
    return render(request, 'index.html', context)
