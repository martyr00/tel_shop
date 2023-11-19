from django.db import connection
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
        with connection.cursor() as cursor:
            query = """
                UPDATE shop_telephone
                SET
                    title = COALESCE(%s, title),
                    brand = COALESCE(%s, brand),
                    built_in_memory = COALESCE(%s, built_in_memory),
                    price = COALESCE(%s, price),
                    diagonal_screen = COALESCE(%s, diagonal_screen),
                    update_time = COALESCE(%s, update_time)
                WHERE id = %s;
            """
            cursor.execute(query, [
                validated_data.get('title', instance.get('title')),
                validated_data.get('brand', instance.get('brand')),
                validated_data.get('built_in_memory', instance.get('built_in_memory')),
                validated_data.get('price', instance.get('price')),
                validated_data.get('diagonal_screen', instance.get('diagonal_screen')),
                validated_data.get('update_time', instance.get('update_time')),
                instance.get('id')
            ])
            return instance
