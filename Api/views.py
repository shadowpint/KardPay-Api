import os

import django_filters
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django_filters import DateFilter
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from engine.compute import comp


from .models import *
import json
from django.contrib.auth.models import User
from .serializers import *
import pandas as pd
from os import path
import string
import random
def id_generator(size=12, chars=string.ascii_lowercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

class OfferList(generics.ListCreateAPIView):
    """
    Get / Create questions
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

class OfferDetail(generics.RetrieveDestroyAPIView):
    """
    Get / Create questions
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

class TrasactionList(APIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        print json.dumps(request.data)
        print (float(data['amount'])*.01*float(data['reward']))
        transaction= Transaction.objects.create(user=request.user,tr_id=id_generator(),amount=data['amount'],item=data['item'],reward=float(data['amount'])*0.01*float(data['reward']),tr_date=datetime.date.today())
        wallet=Wallet.objects.get(user=request.user)
        wallet.amount=str(float(wallet.amount)-float(transaction.amount))
        if wallet.amount<0:

         return JsonResponse({
                'error': 'Insufficient Balance',

            })
        else :
         wallet.treward=str(float(wallet.treward)+float(transaction.reward))
         print wallet.amount
         print wallet.treward
         transaction.save()
         wallet.save()
         return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        id = request.user.pk
        transaction =Transaction.objects.filter(user=id)

        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)

class TransactionDetail(generics.RetrieveDestroyAPIView):
    """
    Get / Create questions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class WalletList(APIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        print json.dumps(request.data)

        wallet = Wallet.objects.create(user=request.user,amount=5000,treward=200)
        wallet.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        id = request.user.pk
        wallet = Wallet.objects.filter(user=id)

        serializer = WalletSerializer(wallet, many=True)
        return Response(serializer.data)
class WalletDetail(generics.RetrieveDestroyAPIView):
    """
    Get / Create questions
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

class CardList(APIView):
    queryset = Transaction.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        print json.dumps(request.data)
        try:
         car=Card.objects.get(user=request.user)
         car.cardnumber=data['cardnumber']
         car.expiry_month = data['expiry_month']
         car.expiry_year = data['expiry_year']
         car.cvv = data['cvv']
         car.card_type = data['card_type']
         car.save()
        except ObjectDoesNotExist:
            card = Card.objects.create(user=request.user, cardnumber=data['cardnumber'],
                                       expiry_month=data['expiry_month'],
                                       expiry_year=data['expiry_year'], cvv=data['cvv'], card_type=data['card_type'])
            wallet = Wallet.objects.create(user=request.user, amount=5000, treward=200)
            wallet.save()
            card.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        id = request.user.pk
        cards = Card.objects.get(user=id)

        serializer = CardSerializer(cards)
        return Response(serializer.data)

class CardDetail(generics.RetrieveDestroyAPIView):
    """
    Get / Create questions
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]



class LastTransaction(APIView):
    """
    Get / Create questions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        id = request.user.pk
        transaction = Transaction.objects.latest('id')

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)


class Redeem(APIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        wallet = Wallet.objects.get(user=request.user)
        wallet.amount = float(wallet.amount) + float(wallet.treward)
        wallet.treward=0.0
        wallet.save()
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

class ProfileList(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        print json.dumps(request.data)
        try:
         pro=Profile.objects.get(user=request.user)
         if 'dob' in data:
          pro.dob=data['dob']
         if 'firstname' in data:
          pro.firstname = data['firstname']
         if 'lastname' in data:
          pro.lastname = data['lastname']
         if 'contact' in data:
          pro.contact = data['contact']
         if 'gender' in data:
          pro.gender = data['gender']
         if 'pic_url' in data:
             pro.pic_url = data['pic_url']
         pro.save()
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=request.user, dob=data['dob'],
                                       firstname=data['firstname'],lastname=data['lastname'],
                                       gender=data['gender'], contact=data['contact'])

            profile.save()
        pr=Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(pr)
        return Response(serializer.data)

    def get(self, request, format=None):
        id = request.user.pk
        profile = Profile.objects.get(user=id)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ShopCartList(APIView):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data.copy()
        print json.dumps(request.data)

        shopcart= ShopCart.objects.create(user=request.user,item=Offer.objects.get(id=data['item_id']))

        shopcart.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        id = request.user.pk
        shopcart =Transaction.objects.filter(user=id)

        serializer = ShopCartSerializer(shopcart, many=True)
        return Response(serializer.data)
