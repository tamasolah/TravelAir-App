from django.db import models
from django.contrib.auth.models import User 

class Destinatie(models.Model):
    tara = models.CharField(max_length=100)
    oras = models.CharField(max_length=100)
    descriere = models.TextField()
    imagine = models.ImageField(upload_to='destinatii/')

    def __str__(self):
        return f"{self.oras}, {self.tara}"


class PachetTuristic(models.Model):
    destinatie = models.ForeignKey(Destinatie, on_delete=models.CASCADE)
    titlu = models.CharField(max_length=100)
    pret = models.DecimalField(max_digits=8, decimal_places=2)
    data_start = models.DateField()
    data_sfarsit = models.DateField()
    locuri_disponibile = models.IntegerField()

    def __str__(self):
        return self.titlu


class Rezervare(models.Model):
    nume_client = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    pachet = models.ForeignKey(PachetTuristic, on_delete=models.CASCADE)
    data_rezervare = models.DateTimeField(auto_now_add=True)
    numar_persoane = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nume_client} - {self.pachet}"


class Oferta(models.Model):
    titlu = models.CharField(max_length=255)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    imagine = models.ImageField(upload_to="oferte/", null=True, blank=True)
    destinatie = models.CharField(max_length=255, default="Necunoscut")
    durata = models.CharField(max_length=50, default="1 zi")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)
    facilitati = models.TextField(default="N/A")
    transport = models.CharField(max_length=100, default="Autocar")
    numar_locuri = models.IntegerField(default=20)
    tip_cazare = models.CharField(max_length=100, default="Hotel")
    disponibilitate = models.BooleanField(default=True)

    def __str__(self):
        return self.titlu


class Review(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('oferta', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.rating}⭐ pentru {self.oferta.titlu}"

