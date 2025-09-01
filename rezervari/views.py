from rest_framework import viewsets
from .models import Rezervare
from .serializers import RezervareSerializer
from oferte.models import Oferta
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class RezervareViewSet(viewsets.ModelViewSet):
    serializer_class = RezervareSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rezervare.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        oferta_id = self.request.data.get('oferta')

        if not oferta_id:
            raise ValidationError({"oferta": "Câmpul 'oferta' este obligatoriu."})

        try:
            oferta = Oferta.objects.get(pk=oferta_id)
        except Oferta.DoesNotExist:
            raise ValidationError({"oferta": "Oferta specificată nu există."})

        serializer.save(user=self.request.user, oferta=oferta)
