from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from magasin.views import CategoryAPIView, ProduitAPIView, ProductViewset

router = SimpleRouter()
router.register(r'produit', ProductViewset, basename='produit')
#from crispy_form import 

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('commande/', views.commande, name='commande'),
    path('ajouterProduit/', views.ajouterProduit, name='ajoutProduit'),
    path('nouveauFournisseur/', views.nouveauFournisseur, name='nouvFour'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
    path('register/',views.register, name = 'register'),
     path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),
    path('api/', include(router.urls)),
]