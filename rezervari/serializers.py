from rest_framework import serializers
from .models import Rezervare
from oferte.serializers import OfertaSerializer 

class RezervareSerializer(serializers.ModelSerializer):
    oferta_titlu = serializers.CharField(source="oferta.titlu", read_only=True)
    oferta_destinatie = serializers.CharField(source="oferta.destinatie", read_only=True)
    oferta_imagine = serializers.ImageField(source="oferta.imagine", read_only=True)
    oferta_id = serializers.IntegerField(source="oferta.id", read_only=True)

    class Meta:
        model = Rezervare
        fields = ["id", "numar_persoane", "data_rezervare",
                  "oferta", "oferta_titlu", "oferta_destinatie", "oferta_imagine", "oferta_id"]
