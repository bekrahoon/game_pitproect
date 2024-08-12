from api.models import GameResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include




api = Api(api_name='v1')
api.register(GameResource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name = 'index')
]