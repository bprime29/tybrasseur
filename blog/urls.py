from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allrecette', views.allrecettes, name="allrecettes"),
    url(r'^recette/(?P<id>\d+)/', views.recette, name="recette"),
    url(r'^ajouter$', views.nouvelleRecette, name="ajout"),
    url(r'^calc_taux', views.calc_with_refracto, name='calc_with_refracto'),
    url(r'^calc_with_densimetre', views.calc_with_densimetre, name='calc_with_densimetre')
]