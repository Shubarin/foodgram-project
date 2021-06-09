from django.conf import settings

from recipes.models import Recipe


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, recipe, quantity=1, update_quantity=False):
        recipe_id = str(recipe.id)
        if recipe_id not in self.cart:
            self.cart[recipe_id] = {'quantity': 1}
            if update_quantity:
                self.cart[recipe_id]['quantity'] = quantity
            else:
                self.cart[recipe_id]['quantity'] += quantity
            self.save()

    def remove(self, recipe):
        recipe_id = str(recipe.id)
        if recipe_id in self.cart:
            del self.cart[recipe_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        recipe_ids = self.cart.keys()
        recipes = Recipe.objects.filter(id__in=recipe_ids)
        cart = self.cart.copy()
        for recipe in recipes:
            cart[str(recipe.id)]['recipe'] = recipe
        for item in cart.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
