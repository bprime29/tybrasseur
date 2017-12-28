from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^allrecette', views.allrecettes, name="allrecettes"),
    url(r'^recette/(?P<id>\d+)/', views.recette, name="recette"),
    url(r'^ajouter$', views.nouvelleRecette, name="ajout")
]