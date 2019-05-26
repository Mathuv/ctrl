from rest_framework import serializers as drf_serializers
from rest_framework_json_api import serializers
from .models import Pulse


class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulse
        # fields = ('id', )
        fields = "__all__"
