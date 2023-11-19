from rest_framework import serializers

from shop.models import Telephone


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telephone
        fields = '__all__'

    def create(self, validated_data):
        return Telephone.post_new_item(validated_data)
