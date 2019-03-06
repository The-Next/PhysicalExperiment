from  rest_framework import serializers
from Spectrometer.models import *

class SpectrometerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spectrometer
        fields = '__all__'