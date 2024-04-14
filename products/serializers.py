from products.models import *

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    types = serializers.SerializerMethodField()

    def get_types(self, obj):
        return obj.types.values()
    
    class Meta:
        model = Product
        fields = "__all__"

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = "__all__"

class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"