from django.shortcuts import render
from rest_framework import viewsets, mixins, views
from .models import Pulse
from .serializers import PulseSerializer

# Create your views here.


class PulseViewSet(viewsets.ModelViewSet):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer
