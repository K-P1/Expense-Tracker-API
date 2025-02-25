from rest_framework import serializers
from .models import Income, Expense, Category

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    # For writing, accept a category name...
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    # For reading, output the category name via a custom field
    category_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'  # This will include both `category` and `category_name`

    def get_category_name(self, obj):
        # If obj is already a dict, try to get the category value directly.
        if isinstance(obj, dict):
            return obj.get('category') or obj.get('category_name')
        # Otherwise, it's a model instance.
        return obj.category.name if obj.category else None

class CategorySerializer(serializers.ModelSerializer):
    # Include expenses if needed
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

# (Reporting serializers remain unchanged)
class ReportSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

class ReadReportSerializer(serializers.Serializer):
    date_range = serializers.CharField()
    currency = serializers.CharField()
    total_credit = serializers.IntegerField()
    total_debit = serializers.IntegerField()
    total_income = serializers.IntegerField()
    total_expense = serializers.IntegerField()
    start_balance = serializers.IntegerField()
    end_balance = serializers.IntegerField()
    incomes = IncomeSerializer(many=True)
    expenses = ExpenseSerializer(many=True)

class ReadSummarySerializer(serializers.Serializer):
    date_range = serializers.CharField()
    currency = serializers.CharField()
    total_credit = serializers.IntegerField()
    total_debit = serializers.IntegerField()
    total_income = serializers.IntegerField()
    total_expense = serializers.IntegerField()
    start_balance = serializers.IntegerField()
    end_balance = serializers.IntegerField()
