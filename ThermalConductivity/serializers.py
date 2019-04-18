from rest_framework import serializers

from ThermalConductivity.models import *


class ThermalConductivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermalConductivity
        fields = "__all__"

class ThermalConductivity_PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThermalConductivity_PDF
        fields = '__all__'