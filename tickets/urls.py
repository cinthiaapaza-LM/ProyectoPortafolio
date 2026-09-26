from django.urls import path

from . import views

urlpatterns = [

    path('crear-prueba/', views.crear_tickets_prueba, name='crear_tickets_prueba'),

    path('mensajes/', views.mostrar_mensajes, name='mostrar_mensajes'),

    path('', views.lista_tickets, name='lista_tickets'),

    path('<int:id>/', views.detalle_ticket, name='detalle_ticket'),

]