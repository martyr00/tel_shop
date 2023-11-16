from rest_framework import generics
from rest_framework.permissions import AllowAny

from shop.models import Telephone
from shop.serializer import ProductSerializer


class ItemOfTelephone(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telephone.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ListOfTelephone(generics.ListCreateAPIView):
    queryset = Telephone.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
