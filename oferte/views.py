from rest_framework import generics, permissions
from .models import Oferta, Review
from .serializers import OfertaSerializer, ReviewSerializer
from rest_framework.exceptions import ValidationError


class OfferListView(generics.ListAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class OfferDetailView(generics.RetrieveAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        oferta_id = self.kwargs.get('oferta_id')
        return Review.objects.filter(oferta_id=oferta_id).order_by('-created_at')

    def perform_create(self, serializer):
        oferta_id = self.kwargs.get('oferta_id')

        try:
            oferta = Oferta.objects.get(pk=oferta_id)
        except Oferta.DoesNotExist:
            raise ValidationError("Oferta nu există.")

        serializer.save(user=self.request.user, oferta=oferta)
