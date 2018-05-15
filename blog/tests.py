from django.db.models import QuerySet
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class blog(TestCase):
    def test_index(self):
        """
        Affichage de la page des recettes : liste des articles.
        """
        response = self.client.get(reverse('blog:index'))
        #self.failUnless(isinstance(response.context['index'], QuerySet))
        self.assertTemplateUsed(response, 'blog/index.html')
        self.failUnlessEqual(response.status_code, 200)

    def test_allrecettes(self):
        """
        Affichage de la page des recettes : liste des articles.
        """
        response = self.client.get(reverse('blog:allrecettes'))
        #self.failUnless(isinstance(response.context['recettes'], QuerySet))
        self.assertTemplateUsed(response, 'blog/allrecettes.html')
        self.failUnlessEqual(response.status_code, 200)

    def test_existing_recette(self):
        """
        Affichage d'un article public existant, sans restriction d'accès.
        """
        response = self.client.get(reverse('blog:recette', kwargs={'id': 1}))
        #self.failUnless(isinstance(response.context['recette'], Article))
        self.assertTemplateUsed(response, 'blog/affiche-recette.html')
        self.failUnlessEqual(response.status_code, 200)

    def test_404_public_article(self):
        """
        Tentative d'affichage d'un article inexistant.
        """
        response = self.client.get(reverse('blog:recette', kwargs={'id': 19829897}))
        self.failUnlessEqual(response.status_code, 404)