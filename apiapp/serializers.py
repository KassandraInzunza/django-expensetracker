from rest_framework import serializers

from mainapp.models import TransactionModel

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ['id','member_id', 'created', 'category', 'description', 'amount']