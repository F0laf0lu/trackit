from rest_framework import serializers
from .models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_type', 'parent']

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = [
            'id', 'amount', 'description', 'category', 'category_id', 'date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']