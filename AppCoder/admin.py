from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Surf)
admin.site.register(Body)
admin.site.register(Horario)
admin.site.register(Reserva)
