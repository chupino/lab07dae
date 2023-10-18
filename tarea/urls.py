from tarea import views
from django.urls.conf import include
from django.urls import path
from .views import EventoCreateView

urlpatterns = [
    path('', views.eventos_list, name='eventos_list'),
    path('<int:mes>/', views.eventos_list, name='eventos_list_por_mes'),
    path('evento/<int:evento_id>/', views.evento_detail, name='evento_detail'),
    path('crear_evento/', EventoCreateView.as_view(), name='crear_evento'),
    path('registro/', views.register, name='register'),
    path('inscribir_evento/', views.inscribir_persona_evento, name='inscribir_evento'),
    path('usuario_mas_participativo/', views.usuario_mas_participativo, name='usuario_mas_participativo'),
    path('eventos_usuario/', views.eventos_realizados_por_usuario, name='eventos_realizados_por_usuario'),
    path('eliminar_evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('editar_evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
]