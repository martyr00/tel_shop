from rest_framework import serializers

from shop.models import Telephone


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)

    price = serializers.IntegerField(max_value=1000000)

    brand = serializers.CharField(max_length=100)
    built_in_memory = serializers.CharField(max_length=100)
    diagonal_screen = serializers.FloatField(max_value=100)

    update_time = serializers.DateTimeField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Telephone
        fields = '__all__'

    def create(self, validated_data):
        return Telephone.post_new_item(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.built_in_memory = validated_data.get('built_in_memory', instance.built_in_memory)
        instance.price = validated_data.get('price', instance.price)
        instance.diagonal_screen = validated_data.get('diagonal_screen', instance.diagonal_screen)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance
