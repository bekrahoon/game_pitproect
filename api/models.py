from tastypie.resources import ModelResource
from shop_game.models import Category, About_Game
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        
class GameResource(ModelResource):
    class Meta:
        queryset = About_Game.objects.all()
        resource_name = 'games'
        allowed_methods = ['get','post','delete']
        authentication = CustomAuthentication()
        authorization = Authorization()
        excludes = ['reviews_qty','created_at']
        
        
    
    def hydrate(self,bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    
    def dehydrate(self,bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
    
    def dehydrate_title(self,bundle):
        return bundle.data['title'].upper() 