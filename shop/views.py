from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Telephone
from shop.serializer import ProductSerializer


class TelephoneAPIView(APIView):
    queryset = Telephone.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        telephone_id = kwargs.get("telephone_id", None)
        if telephone_id:
            try:
                serializer = ProductSerializer(Telephone.get_item(telephone_id))
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Telephone.DoesNotExist:
                return Response({'error': 'Object does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(Telephone.get_all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(None, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        telephone_id = kwargs.get("telephone_id", None)
        if not telephone_id:
            return Response({"error": "Method PATCH not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            serializer = ProductSerializer(data=request.data, instance=Telephone.get_item(telephone_id))
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Telephone.DoesNotExist:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        telephone_id = kwargs.get("telephone_id", None)
        if not telephone_id:
            return Response({"error": "Method DElETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            Telephone.delete_item(telephone_id)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Telephone.DoesNotExist:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

