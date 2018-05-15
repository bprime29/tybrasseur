from django.contrib import admin
from .models import Recette,  Ingredient,  Etape, \
    Ebullition, Etape_ebullition, \
    Fermentation, Etape_fermentation, \
    Empatage, Etape_empatage, \
    Photo, Methode, Commentaire


class EtapeAdmin(admin.StackedInline):
    model = Etape


class EmpatageAdmin(admin.StackedInline):
    model = Empatage


class EtapeEmpatageAdmin(admin.ModelAdmin):
    model = Etape_empatage


class EbullitionAdmin(admin.StackedInline):
    model = Ebullition


class EtapeEbullitionAdmin(admin.ModelAdmin):
    model = Etape_ebullition


class FermentationAdmin(admin.StackedInline):
    model = Fermentation


class EtapeFermentationAdmin(admin.ModelAdmin):
    model = Etape_fermentation


class IngredientAdmin(admin.StackedInline):
    model = Ingredient


class CommentaireAdmin(admin.ModelAdmin):
    model = Commentaire
    list_display = ('message', 'recette', 'user')
    list_display_links = ('message', 'recette', 'user')


class IngredientAdmin2(admin.ModelAdmin):
    model = Ingredient
    list_display = ('nom', 'quantite')
    list_display_links = ('nom', 'quantite')


class PhotoAdmin(admin.StackedInline):
    model = Photo


class RecetteAdmin(admin.ModelAdmin):
    inlines = [IngredientAdmin, EtapeAdmin, EmpatageAdmin, EbullitionAdmin, FermentationAdmin, PhotoAdmin]
    list_display = ('titre', 'user')
    list_display_links = ('titre', 'user')


class IngredientAdmin(admin.ModelAdmin):
    inlines = [IngredientAdmin2]


class MethodeAdmin(admin.ModelAdmin):
    model = Methode


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Etape_empatage, EtapeEmpatageAdmin)
admin.site.register(Etape_ebullition, EtapeEbullitionAdmin)
admin.site.register(Etape_fermentation, EtapeFermentationAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Methode, MethodeAdmin)
admin.site.register(Ingredient, IngredientAdmin2)
