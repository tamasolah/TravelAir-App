from django.contrib import admin
from .models import Destinatie, PachetTuristic, Rezervare
from .models import Oferta

admin.site.register(Oferta)
admin.site.register(Destinatie)
admin.site.register(PachetTuristic)
admin.site.register(Rezervare)
