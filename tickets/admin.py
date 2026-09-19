from django.contrib import admin

# Register your models here.
from .models import Usuario, Ticket

admin.site.register(Usuario)
admin.site.register(Ticket)
