from rest_framework import serializers
from .models import Prestation, Realisation, Review

# le serializer sert a convertir les modeles en JSON pour etre interprété par React.

class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = ('id', 'title', 'description',)
        
class RealisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisation
        fields = ('id', 'title', 'lieu', 'date', 'photo_before' , 'photo_after' , 'description')
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'last_name', 'date', 'description', 'rating')