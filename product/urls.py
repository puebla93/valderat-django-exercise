from django.urls import path

from product.views import *

urlpatterns = [
    path('prods/', ListCreateProdsViewSet.as_view(), name="prods-list-create"),
    path('prods/<int:id>/', ProdsDetailView.as_view(), name="prods-detail"),
    path('coordsprods/', CoordsProdsView.as_view(), name="coordsprods"),
]
