from rest_framework import serializers
from favorites.models import *

class PirateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pirate
        fields = ['name', 'dog', 'color']