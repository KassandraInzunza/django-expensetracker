from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse

from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from apiapp.serializers import TransactionSerializer
from rest_framework.parsers import JSONParser

from .serializers import *

from mainapp.models import TransactionModel

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def transactions_list(request):
    if request.method == 'GET':
        transactions = TransactionModel.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            transactions = transactions.filter(title__icontains=title)

        transactions_serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(transactions_serializer.data, safe=False)

    elif request.method == 'POST':
        transaction_data = JSONParser().parse(request)
        transactions_serializer = TransactionSerializer(data=transaction_data)
        if transactions_serializer.is_valid():
            transactions_serializer.save()
            return JsonResponse(transactions_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
