from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.contrib import messages
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
    # print(budgets_orgIDs)
    limits = []
    expenses = []
    for i in range(len(budgets_orgIDs)):
        limits += Limit.objects.filter(budgetID=budgets_orgIDs[i])
        expenses += Expense.objects.filter(budgetID=budgets_orgIDs[i])
    
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

def addBudget(request):
    return render(request, 'updateDB/addBudget.html', {'NewBudgetForm': NewBudgetForm})

def addLimit(request):
    return render(request, 'updateDB/addLimit.html', {'NewLimitForm': NewLimitForm(user=request.user)})

def addExpense(request):
    return render(request, 'updateDB/addExpense.html', {'NewExpenseForm': NewExpenseForm(user=request.user)})

def addCategory(request):
    return render(request, 'updateDB/addCategory.html', {'NewCategoryForm': NewCategoryForm})

def success(request):
    if 'addBudget' in request.POST:
        form = NewBudgetForm(request.POST)
        if form.is_valid():
            newBudget = form.save(commit=False)
            try:
                newBudget.user = request.user
                newBudget.save()
                messages.success(request, "Successfully added a new budget")
                return redirect('dashboard.html')
            except:
                pass
        messages.error(request, "Cannot have two budgets with the same name")
        return redirect('dashboard.html')

    elif 'addLimit' in request.POST:
        print('in limit')
        form = NewLimitForm(request.POST, user=request.user)
        if form.is_valid():
            newLimit = form.save(commit=False)
            try:
                print('in limit success')
                newLimit.user = request.user
                newLimit.save()
                messages.success(request, "Successfully added a new limit")
                return redirect('dashboard.html')
            except:
                pass    
        messages.error(request, "Cannot have two limits with the same name in the same budget")
        return redirect('dashboard.html')

    elif 'addCategory' in request.POST:
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            newCategory = form.save(commit=False)
            try:
                newCategory.user = request.user
                newCategory.save()
                messages.success(request, "Successfully added a new category")
                return redirect('dashboard.html')
            except:
                pass
        messages.error(request, "Cannot have two categories with the same name")
        return redirect('dashboard.html')
    else:
        form = NewExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            newExpense = form.save(commit=False)
            newExpense.user = request.user
            newExpense.save()
            messages.success(request, "Successfully added a new expense")
            return redirect('dashboard.html')
        messages.error(request, "Oops, something went wrong, the expense was not added")
        return redirect('dashboard.html')