from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.
class Category(models.Model):
    categoryID = models.AutoField(primary_key = True, db_column='CategoryID')
    category = models.CharField(max_length=50, db_column='Category')

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Categories"

class Budget(models.Model):
    budgetID = models.AutoField(primary_key=True, db_column='BudgetID')
    name = models.CharField(max_length=200, db_column='Budget Name')
    startDate = models.DateField(default=date.today, db_column='Start Date')
    endDate = models.DateField(default=date.today, db_column='End Date')
    current = models.BooleanField(default=True, db_column='Current Budget')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User', null=True)

class Expense(models.Model):
    expenseID = models.AutoField(primary_key=True, db_column='ExpenseID')
    budgetID = models.ForeignKey(Budget, on_delete=models.CASCADE, db_column='BudgetID')
    title = models.CharField(max_length=100, db_column='Title')
    description = models.TextField(db_column='Description')
    date = models.DateField(default=date.today, db_column='Date')
    amount = models.FloatField(db_column='Amount')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='Category')

class Limit(models.Model):
    limitID = models.AutoField(primary_key=True, db_column='LimitID')
    budgetID = models.ForeignKey(Budget, on_delete=models.CASCADE, db_column='BudgetID')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='Category')
    amount = models.FloatField(db_column='Amount')

