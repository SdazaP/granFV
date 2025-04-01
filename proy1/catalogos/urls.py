from django.contrib import admin
from django.urls import path
from catalogos import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('homeCatalogos/', views.homeCatalogos, name='homeCatalogos'),
    #CRUD Carrera
    path('carrerasRead/', views.carrerasRead, name='carrerasRead'),
    path('carreraCreate/', views.carrerasCreate, name='carreraCreate'),
    path('carrerasUpdate/<int:id>',views.carrerasUpdate, name='carrerasUpdate'),
    path('carrerasDelete/<int:id>', views.carrerasDelete, name='carrerasDelete'),
    #CRUD Aulas
    path('aulasRead/', views.aulasRead, name='aulasRead'),
    path('aulasCreate/', views.aulasCreate, name='aulasCreate'),
    path('aulasUpdate/<int:id>',views.aulasUpdate, name='aulasUpdate'),
    path('aulasDelete/<int:id>', views.aulasDelete, name='aulasDelete'),
    #CRUD Maestros
    path('maestrosRead/', views.maestrosRead, name='maestrosRead'),
    path('maestroCreate/', views.maestroCreate, name='maestrosCreate'),
    path('maestrosUpdate/<int:id>', views.maestrosUpdate, name='maestrosUpdate'),
    path('maestrosDelete/<int:id>', views.maestrosDelete, name='maestrosDelete'),
]
