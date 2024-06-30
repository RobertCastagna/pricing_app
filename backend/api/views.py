from rest_framework import viewsets
from .models import Product, PriceHistory, Budget
from .serializers import ProductSerializer, PriceHistorySerializer, BudgetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import calculate_affordable_amount

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


    @action(detail=True, methods=['get'])
    def affordable_amount(self, request, pk=None):
        budget = self.get_object()
        affordable_amount = calculate_affordable_amount(budget)
        return Response({'affordable_amount': affordable_amount})
