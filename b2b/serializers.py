from rest_framework import serializers
from .models import Company,Product,OrderItem,Order



class CompanySerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=120)
    def create(self, validated_data):
        return Company.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class OrderSerializer(serializers.Serializer):
    buyer = serializers.CharField()
    seller = serializers.CharField()


class OrderItemSerializer(serializers.Serializer):
    order = serializers.CharField
    product = serializers.CharField
    price = serializers.CharField
    quantity = serializers.CharField


    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)