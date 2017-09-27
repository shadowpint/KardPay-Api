from rest_framework import serializers

from users.models import Profile
from users.serializers import UserSerializer
from .models import *


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
        depth=1
class ShopCartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item=OfferSerializer()
    class Meta:
        model = ShopCart
        fields = '__all__'
        depth=1