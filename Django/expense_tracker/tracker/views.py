from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime
from .models import Income, Expense, Category
from .serializers import IncomeSerializer, ExpenseSerializer, CategorySerializer, ReportSerializer, ReadReportSerializer, ReadSummarySerializer
import logging

logger = logging.getLogger(__name__)

# CRUD for Income
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

# CRUD for Expense
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# CRUD for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Reporting endpoints as API views

@api_view(['GET'])
def report_summary(request):
    serializer = ReportSerializer(data=request.query_params)
    if serializer.is_valid():
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        if start_date > end_date:
            return Response({"detail": "Start date cannot be greater than end date"}, status=status.HTTP_400_BAD_REQUEST)

        date_range = f"{start_date} to {end_date}"
        currency = "NGN"
        total_credit = Income.objects.filter(date__range=(start_date, end_date)).aggregate(total=Sum('amount'))['total'] or 0
        total_debit = Expense.objects.filter(date__range=(start_date, end_date)).aggregate(total=Sum('amount'))['total'] or 0
        total_income = Income.objects.count()
        total_expense = Expense.objects.count()
        start_balance = Income.objects.filter(date__lte=start_date).aggregate(total=Sum('amount'))['total'] or 0
        end_balance = start_balance + total_credit - total_debit

        data = {
            "date_range": date_range,
            "currency": currency,
            "total_credit": total_credit,
            "total_debit": total_debit,
            "total_income": total_income,
            "total_expense": total_expense,
            "start_balance": start_balance,
            "end_balance": end_balance,
        }
        logger.info("Generated summary report for range %s", date_range)
        return Response(ReadSummarySerializer(data).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def full_report(request):
    serializer = ReportSerializer(data=request.query_params)
    if serializer.is_valid():
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        if start_date > end_date:
            return Response({"detail": "Start date cannot be greater than end date"}, status=status.HTTP_400_BAD_REQUEST)
        
        date_range = f"{start_date} to {end_date}"
        currency = "NGN"
        total_credit = Income.objects.filter(date__range=(start_date, end_date)).aggregate(total=Sum('amount'))['total'] or 0
        total_debit = Expense.objects.filter(date__range=(start_date, end_date)).aggregate(total=Sum('amount'))['total'] or 0
        start_balance = Income.objects.filter(date__lte=start_date).aggregate(total=Sum('amount'))['total'] or 0
        end_balance = start_balance + total_credit - total_debit
        total_income = Income.objects.count()
        total_expense = Expense.objects.count()
        incomes = Income.objects.filter(date__range=(start_date, end_date))
        expenses = Expense.objects.filter(date__range=(start_date, end_date))
        
        data = {
            "date_range": date_range,
            "currency": currency,
            "total_credit": total_credit,
            "total_debit": total_debit,
            "total_income": total_income,
            "total_expense": total_expense,
            "start_balance": start_balance,
            "end_balance": end_balance,
            "incomes": IncomeSerializer(incomes, many=True).data,
            "expenses": ExpenseSerializer(expenses, many=True).data,
        }
        logger.info("Generated full report for range %s", date_range)
        return Response(ReadReportSerializer(data).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
