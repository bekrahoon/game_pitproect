from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import About_Game, Cart, CartItem
from django.utils import timezone


def index(request):
    games = About_Game.objects.all()
    return render(request, "shop_games/games.html", {"games": games})


def single_game(request, game_id):
    # #Option 1
    # try:
    #     course = Course.objects.get(pk=game_id)
    #     return render(request, 'shop/single_course.html', {'course':course})
    # except Course.DoesNotExist:
    #     raise Http404()
    # Option 2
    game = get_object_or_404(About_Game, pk=game_id)
    return render(request, "shop_games/single_game.html", {"game": game})


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(About_Game, pk=game_id)
    cart, created = Cart.objects.get_or_create(
        user=request.user, defaults={"created_at": timezone.now()}
    )

    cart_item, created = CartItem.objects.get_or_create(cart=cart, game=game)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Game added to cart!")
    return redirect("shop_game:view_cart")


@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, "shop_games/cart.html", {"cart": cart})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    messages.success(request, "Game removed from cart!")
    return redirect("shop_game:view_cart")
