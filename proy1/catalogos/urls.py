from django.contrib import admin
from django.urls import path
from catalogos import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('homeCatalogos/', views.homeCatalogos, name='homeCatalogos'),
    path('carrerasRead/', views.carrerasRead, name='carrerasRead'),
    
]
