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
    #Planes de estudio
    path('planesRead/', views.planesRead, name='planesRead'),
    path('planesCreate/', views.planesCreate, name='planesCreate'),
    path('planesUpdate/<int:id>/', views.planesUpdate, name='planesUpdate'),
    path('planesDelete/<int:id>/', views.planesDelete, name='planesDelete'),
    #Materias
    path('materiasRead/', views.materiasRead, name='materiasRead'),
    path('materiasCreate/', views.materiasCreate, name='materiasCreate'),
    path('materiasUpdate/<int:id>/', views.materiasUpdate, name='materiasUpdate'),
    path('materiasDelete/<int:id>/', views.materiasDelete, name='materiasDelete'),
    # URLs para Alumnos
    path('alumnosRead/', views.alumnosRead, name='alumnosRead'),
    path('alumnosCreate/', views.alumnosCreate, name='alumnosCreate'),
    path('alumnosUpdate/<int:id>/', views.alumnosUpdate, name='alumnosUpdate'),
    path('alumnosDelete/<int:id>/', views.alumnosDelete, name='alumnosDelete'),
    path('get_planes_estudio/', views.get_planes_estudio, name='get_planes_estudio'),
]
