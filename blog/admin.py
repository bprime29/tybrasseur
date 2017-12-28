from django.contrib import admin
from .models import Recette,  Ingredient,  Etape,  Photo, Methode, Commentaire


class EtapeAdmin(admin.StackedInline):
    model = Etape


class IngredientAdmin(admin.StackedInline):
    model = Ingredient

class CommentaireAdmin(admin.ModelAdmin):
    model = Commentaire
    list_display = ('message','recette','user')
    list_display_links = ('message','recette','user')


class IngredientAdmin2(admin.ModelAdmin):
    model = Ingredient
    list_display = ('nom','quantite')
    list_display_links = ('nom','quantite')


class PhotoAdmin(admin.StackedInline):
    model = Photo


class RecetteAdmin(admin.ModelAdmin):
    inlines = [ EtapeAdmin,IngredientAdmin,PhotoAdmin ]
    list_display = ('titre','user')
    list_display_links = ('titre','user')


class IngredientAdmin(admin.ModelAdmin):
    inlines = [ IngredientAdmin2 ]


class MethodeAdmin(admin.ModelAdmin):
    model = Methode

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Methode, MethodeAdmin)
admin.site.register(Ingredient, IngredientAdmin2)
