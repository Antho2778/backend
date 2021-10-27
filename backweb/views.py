from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PrestationSerializer, RealisationSerializer, ReviewSerializer
from .models import Prestation, Realisation, Review

# Create your views here.

class PrestationView(viewsets.ModelViewSet):
    serializer_class = PrestationSerializer
    queryset = Prestation.objects.all()
    
    
class RealisationView(viewsets.ModelViewSet):
    serializer_class = RealisationSerializer
    queryset = Realisation.objects.all()
    
class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()