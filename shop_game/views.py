from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import About_Game
# Create your views here.

def index(request):
    games = About_Game.objects.all()
    return render(request,'shop_games/games.html',{'games':games})


def single_game(request, game_id):
    # #Option 1
    # try:
    #     course = Course.objects.get(pk=game_id)
    #     return render(request, 'shop/single_course.html', {'course':course})
    # except Course.DoesNotExist:
    #     raise Http404()
    #Option 2
    game = get_object_or_404(About_Game, pk=game_id)
    return render(request, 'shop_games/single_game.html', {'game':game})