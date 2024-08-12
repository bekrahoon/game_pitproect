from django.urls import path
from . import views

app_name = 'shop_game'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.single_game, name='single_game')
]

