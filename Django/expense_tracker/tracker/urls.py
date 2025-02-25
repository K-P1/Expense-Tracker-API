from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, CategoryViewSet, report_summary, full_report

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('report/summary/', report_summary, name='report-summary'),
    path('report/full/', full_report, name='full-report'),
]
