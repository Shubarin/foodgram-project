from django.conf import settings

from recipes.models import Recipe


class Cart:
    def __init__(self, request):
        """Инициализация объекта корзины."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем в сессии пустую корзину.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, recipe, quantity=1, update_quantity=False):
        """Добавление товара в корзину или обновление его количества."""
        recipe_id = str(recipe.id)
        if recipe_id not in self.cart:
            self.cart[recipe_id] = {'quantity': 1}
            if update_quantity:
                self.cart[recipe_id]['quantity'] = quantity
            else:
                self.cart[recipe_id]['quantity'] += quantity
            self.save()

    def remove(self, recipe):
        """Удаление товара из корзины."""
        recipe_id = str(recipe.id)
        if recipe_id in self.cart:
            del self.cart[recipe_id]
            self.save()

    def save(self):
        # Помечаем сессию как измененную
        self.session.modified = True

    def __iter__(self):
        """
        Проходим по товарам корзины и
        получаем соответствующие объекты Product.
        """
        recipe_ids = self.cart.keys()
        # Получаем объекты модели Product и передаем их в корзину.
        recipes = Recipe.objects.filter(id__in=recipe_ids)
        cart = self.cart.copy()
        for recipe in recipes:
            cart[str(recipe.id)]['recipe'] = recipe
        for item in cart.values():
            yield item

    def __len__(self):
        """Возвращает общее количество товаров в корзине."""
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # Очистка корзины.
        del self.session[settings.CART_SESSION_ID]
        self.save()
