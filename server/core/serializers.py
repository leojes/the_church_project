from django.urls import path, include
from core import models as core_models
from rest_framework import serializers, viewsets
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        try:
            token = Token.objects.get(user_id=obj.id)
            return token.key
        except Token.DoesNotExist:
            return "token failed create a new one"

    class Meta:
        model = core_models.User
        fields = ['id', 'email', 'token']


class FamilySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    # def get_family_members(self, obj):
    #     return ""

    class Meta:
        model = core_models.Family
        fields = ['username', 'hash_number', 'updated_at', 'members']


class FamilyCardSerializer(serializers.ModelSerializer):
    family = FamilySerializer()

    # def get_family(self, obj):
    #     objects = core_models.Family.objects.get(pk=obj.family.pk)
    #     fam_details = FamilySerializer(objects, many=True)

    class Meta:
        model = core_models.FamilyCard
        fields = ['card_number', 'expiry_date', 'family']

class FamilyViewset(viewsets.ModelViewSet):
    queryset = core_models.Family.objects.all()
    serializer_class = FamilySerializer

class FamilyCardViewset(viewsets.ModelViewSet):
    queryset = core_models.FamilyCard.objects.all()
    serializer_class = FamilyCardSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = core_models.User.objects.all()
    serializer_class = UserSerializer
