from django.urls import path
from .views import OfferListView, OfferDetailView, ReviewListCreateView

urlpatterns = [
    path('api/oferte/', OfferListView.as_view(), name='offer-list'),
    path('api/oferte/<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),
    path('api/oferte/<int:oferta_id>/recenzii/', ReviewListCreateView.as_view(), name='offer-reviews'),
]
