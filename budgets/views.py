from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# custom login page: will render login.html upon request
def login(self, request):
    return render(request, 'registration/login.html')

# custom dashboard: will render dashboard.html upon request
def dashboard(request):
    # print(request.user)
    budgets = Budget.objects.filter(user=request.user, current=True)
    # budgets = budgets.filter(current=True)
    budgets_orgIDs = [budget.budgetID for budget in budgets]
    if len(budgets_orgIDs) > 0:
        limits = Limit.objects.filter(budgetID=budgets_orgIDs[0])
        expenses = Expense.objects.filter(budgetID=budgets_orgIDs[0])
    else: 
        limits = []
        expenses = []
    # limits_names = [limit.category.category for limit in limits]
    # print(limits_names)
    
    # expense_titles = [expense.title for expense in expenses]
    # print(expense_titles)
    args = {
        'budgets': budgets,
        'limits': limits,
        'expenses': expenses,
    }
    return render(request, 'data.html', args)

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'