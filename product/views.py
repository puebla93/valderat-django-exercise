from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import status
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Prods
from product.serializers import ProdsSerializer

# Create your views here.

class ListCreateProdsViewSet(generics.ListCreateAPIView):
    """
        GET prods/
        POST prods/
    """
    queryset = Prods.objects.all()
    serializer_class = ProdsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'ref', 'zipcode', 'store', 'amount']
    search_fields = ['id', 'ref', 'zipcode', 'store', 'amount']
    ordering_fields = ['id', 'ref', 'zipcode', 'store', 'amount']


class ProdsDetailView(generics.RetrieveAPIView):
    """
        GET prods/:id/
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
