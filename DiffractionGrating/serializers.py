
from rest_framework import serializers
from DiffractionGrating.models import *

class DiffractionGratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiffractionGrating
        fields = '__all__'