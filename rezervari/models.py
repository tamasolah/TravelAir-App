from django.contrib.auth.models import User
from django.db import models
from oferte.models import Oferta



class Rezervare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nume_client = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telefon = models.CharField(max_length=20, blank=True)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='rezervari_oferta')
    data_rezervare = models.DateTimeField(auto_now_add=True)
    numar_persoane = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username if self.user else self.nume_client} - {self.pachet}"
