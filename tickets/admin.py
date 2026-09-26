from django.contrib import admin

# Register your models here.
from .models import Usuario, Ticket, Articulo

admin.site.register(Usuario)
admin.site.register(Ticket)
admin.site.register(Articulo)