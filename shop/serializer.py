from rest_framework import serializers

from shop.models import Telephone


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telephone
        fields = '__all__'
