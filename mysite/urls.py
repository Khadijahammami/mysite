from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from rest_framework import routers
from magasin.views import ProductViewset

# mysite/urls.py
router=routers.SimpleRouter()
router.register('produit',ProductViewset,basename='produit ')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('jeux/', include('jeux.urls')),
    path('', views.index, name='acceuil'),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include (router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
