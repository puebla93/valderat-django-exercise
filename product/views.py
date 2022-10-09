from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import status

from product.models import Prods
from product.serializers import ProdsSerializer

# Create your views here.

class ListCreateProdsViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows prods to be viewed or edited.
    """
    queryset = Prods.objects.all()
    serializer_class = ProdsSerializer


class ProdsDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows prods to be viewed or edited.
    """
    queryset = Prods.objects.all()
    serializer_class = ProdsSerializer

    def get(self, request, *args, **kwargs):
        try:
            prod = self.queryset.get(id=kwargs["id"])
            return Response(ProdsSerializer(prod).data)
        except Prods.DoesNotExist:
            return Response(
                data={
                    "message": "Prod: \"{}\" does not exist".format(kwargs["id"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
