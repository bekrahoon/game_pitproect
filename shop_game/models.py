from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class About_Game(models.Model):
    title = models.CharField(max_length=255)
    images = models.URLField(blank=False, null=False)
    video = models.URLField()
    about_game = models.CharField(max_length=2000)
    price = models.FloatField()
    download_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    game = models.ForeignKey(About_Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.game.title}"

    @property
    def total_price(self):
        return self.quantity * self.game.price
