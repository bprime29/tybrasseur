from django import template
from blog.models import Methode, Recette


register = template.Library()


@register.inclusion_tag('blog/menu.html')
def show_menu():
    return {'types': Methode.objects.all()}


@register.inclusion_tag('blog/nb_recette_total.html')
def show_nb_recette():
    return {'nb_total': Recette.objects.all().count()}