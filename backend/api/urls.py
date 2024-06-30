from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PriceHistoryViewSet, BudgetViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'price-history', PriceHistoryViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
