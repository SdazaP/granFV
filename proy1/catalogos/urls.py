from django.contrib import admin
from django.urls import path
from catalogos import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('homeCatalogos/', views.homeCatalogos, name='homeCatalogos'),

    path('carrerasRead/', views.carrerasRead, name='carrerasRead'),
    path('carreraCreate/', views.carrerasCreate, name='carreraCreate'),
    path('carrerasUpdate/<int:id>',views.carrerasUpdate, name='carrerasUpdate'),
    path('carrerasDelete/<int:id>', views.carrerasDelete, name='carrerasDelete'),
    
]
