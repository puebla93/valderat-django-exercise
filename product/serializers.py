from rest_framework import serializers

from product.models import Prods

class ProdsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prods
        fields = ['id', 'ref', 'zipcode', 'store', 'amount']
