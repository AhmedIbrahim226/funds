from ..models import Article
from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    is_read = serializers.BooleanField(write_only=True)
    received_decimal = serializers.FloatField(write_only=True)

    class Meta:
        model = Article
        fields = ('id', 'link', 'created_at', 'is_read', 'received_decimal')


    def create(self, validated_data):
        is_read = validated_data.pop('is_read')
        received_decimal = validated_data.pop('received_decimal')
        return super().create(validated_data)


