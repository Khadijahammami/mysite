from django.shortcuts import render,redirect
from django.template import loader

from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import ProduitForm
from .forms import CommandeForm
from .forms import FournisseurForm
from .forms import UserRegistrationForm, UserCreationForm

from .models import Produit
from .models import Categorie
from .models import Commande
from .models import Fournisseur
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from magasin.models import Categorie, Produit
from magasin.serializers import CategorySerializer, ProduitSerializer

# Create your views here.
def index(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    products = Produit.objects.all()
    #context = {'products':products}
    #return render(request,'magasin/majProduits.html',{'form':form})
    return render(request, 'magasin/vitrine.html', {'list':products})#context est une variable python qui assure la communication avec le template

def test(request):
    categories = Categorie.objects.all()
    context = {'categories':categories}
    return render(request,'magasin/test.html',context)

def commande(request):
    if( request.method == "POST" ):
        form = CommandeForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = CommandeForm()
    commandes = Commande.objects.all()
    
    return render(request, 'magasin/commande.html', {'form':form, 'commandes':commandes})

def nouveauFournisseur(request):
    if( request.method == "POST" ):
        form = FournisseurForm(request.POST, request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = FournisseurForm()
    listFour = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form':form, 'fournisseurs':listFour})

def ajouterProduit(request):
    if( request.method == "POST" ):
        form = ProduitForm(request.POST,request.FILES)
        if( form.is_valid() ):
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    
    return render(request,'magasin/majProduits.html',{'form':form})

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('acceuil')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})
class CategoryAPIView(APIView):
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProduitAPIView(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id', None)
        if category_id:
            # Use the correct field name "catégorie_id" here
            queryset = queryset.filter(catégorie_id=category_id)
        return queryset


