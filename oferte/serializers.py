from rest_framework import serializers
from .models import Oferta, Review


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_username', 'oferta', 'text', 'rating', 'created_at']
        read_only_fields = ['user', 'oferta', 'created_at'] 


class OfertaSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  

    class Meta:
        model = Oferta
        fields = '__all__'
