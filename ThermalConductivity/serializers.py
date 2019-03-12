from rest_framework import serializers

from ThermalConductivity.models import *


class ThermalConductivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermalConductivity
        fields = "__all__"