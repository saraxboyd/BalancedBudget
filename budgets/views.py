from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# custom login page: will render login.html upon request
def login(self, request):
    return render(request, 'registration/login.html')

# custom logout page: will render logout.html upon request
def logout(request):
    return render(request, 'registration/logout.html')

# custom dashboard: will render dashboard.html upon request
def dashboard(request):
    budgets = Budget.objects.filter(current=True)
    budgets_orgIDs = [budget.budgetID for budget in budgets]
    # print(budgets_orgIDs)
    limits = Limit.objects.filter(budgetID=budgets_orgIDs[0])
    # limits_names = [limit.category.category for limit in limits]
    # print(limits_names)
    expenses = Expense.objects.filter(budgetID=budgets_orgIDs[0])
    # expense_titles = [expense.title for expense in expenses]
    # print(expense_titles)
    args = {
        'budgets': budgets,
        'limits': limits,
        'expenses': expenses,
    }
    return render(request, 'data.html', args)