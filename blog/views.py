from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils import timezone
from .models import Recette, Methode, Ingredient, Etape, Photo, Commentaire
from .forms import RecetteForm, EtapeFormset, IngredientFormset, ImageFormset, CommentaireForm


# Create your views here.

TYPE_CHOICES = ['1','2','3','4'];

def index(request):
    return render(request, 'blog/index.html')

def allrecettes(request):

    recettes = Recette.objects.all().order_by('-id');
    typeObjet=None
    if request.method == 'GET':
        if request.GET.get('type'):
            if request.GET['type'] in TYPE_CHOICES:
                type = request.GET['type']
                typeObjet = Methode.objects.get(id=type)
                recettes = Recette.objects.filter(type=type);
    paginator = Paginator(recettes, 10)
    page = request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recettes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recettes = paginator.page(paginator.num_pages)
    contexte = {
        'typeObjet': typeObjet,
        'recettes': recettes,
    }
    return render(request, 'blog/allrecettes.html', contexte)

def recette(request, id):
    if (request.method == 'POST'):
        commentaire_form = CommentaireForm(request.POST)

        if commentaire_form.is_valid():
            commentaire = commentaire_form.save()
            commentaire.recette = Recette.objects.get(id=id)
            commentaire.user = request.user
            commentaire.save()
    recette = Recette.objects.get(id=id)
    etapes = Etape.objects.filter(recette=id)
    ingredients = Ingredient.objects.filter(recette=id)
    photos = Photo.objects.filter(recette=id)
    commentaires = Commentaire.objects.filter(recette=id)
    form_com = CommentaireForm();
    contexte = {
        'recette'    : recette,
        'etapes'     : etapes,
        'ingredients': ingredients,
        'photos'     : photos,
        'commentaires': commentaires,
        'form_com': form_com,
    }
    return render(request, 'blog/affiche-recette.html', contexte)

def search(request):

    query = request.GET.get('search_query')
    orderby = ''
    orderway = ''
    if request.GET.get('orderby') and request.GET.get('orderway'):
        orderby = request.GET.get('orderby')
        orderway = request.GET.get('orderway')
        if orderway == 'desc':
            results = Recette.objects.filter(titre__contains=query).order_by('-' + orderby).select_related()
        elif orderway == 'asc':
            results = Recette.objects.filter(titre__contains=query).order_by(orderby).select_related()
    else :
        results = Recette.objects.filter(titre__contains=query).select_related()

    paginator = Paginator(results, 10)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        results = paginator.page(paginator.num_pages)
    contexte = {
        'page': page,
        'orderby': orderby,
        'orderway': orderway,
        'query': query,
        'results' : results
    }
    return render(request, 'search/search_result.html', contexte)

def nouvelleRecette(request):

    form = RecetteForm()
    IngredientForm = IngredientFormset()
    EtapeForm = EtapeFormset()
    ImageForm = ImageFormset()

    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            recette = form.save()
            recette.user = request.user
            recette.save()
            IngredientForm = IngredientFormset(request.POST,instance=recette)
            if IngredientForm.is_valid():
                IngredientForm.save()
                EtapeForm = EtapeFormset(request.POST,instance=recette)
                if EtapeForm.is_valid():
                    EtapeForm.save()
                    ImageForm = ImageFormset(request.POST,request.FILES,instance=recette)
                    if ImageForm.is_valid():
                        ImageForm.save()
                        return render(request, "blog/nouvelle-recette.html", {
                            'form': form,
                            'IngredientForm': IngredientForm,
                            'EtapeForm': EtapeForm,
                            'ImageForm': ImageForm,
                            'success_message':'success'
                        })

    return render(request, "blog/nouvelle-recette.html", {
        'form': form,
        'IngredientForm': IngredientForm,
        'EtapeForm': EtapeForm,
        'ImageForm':ImageForm,
    })