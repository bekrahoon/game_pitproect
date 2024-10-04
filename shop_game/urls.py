from django.urls import path
from . import views

app_name = 'shop_game'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.single_game, name='single_game'),
    path('add-to-cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
