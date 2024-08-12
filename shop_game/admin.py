from django.contrib import admin
from .models import About_Game, Category


admin.site.site_header = "Games Admin"
admin.site.site_title = "My Games"
admin.site.index_title = "Welcome to the Games admin area"

class GameAdmin(admin.ModelAdmin):
    list_display = ('title','price','category')
    
    
    
class GameInline(admin.TabularInline):
    model = About_Game
    exclude = ['update_at']
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','update_at')
    fieldsets = [
        (None, {'fields':['title']}),
        ('Dates', {
            'fields':['update_at'],
            'classes':['collapse']
        })
    ]
    inlines=[GameInline]
    
    
    
# Register your models here.
admin.site.register(Category)
admin.site.register(About_Game, GameAdmin)
