from rest_framework import serializers

from StaticYoungModulus.models import *


class StaticYoungModulusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticYooungModulus
        fields = "__all__"