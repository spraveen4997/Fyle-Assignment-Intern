from rest_framework import serializers
from .models import Branches
from .models import Banks

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields='__all__'