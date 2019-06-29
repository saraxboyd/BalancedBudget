from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
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
    return render(request, 'updateDB/addBudget.html', {
        # 'categories': Category.objects.order_by('category'), 
        'NewBudgetForm': NewBudgetForm})

def addLimit(request):
    # 'budgets': Budget.objects.filter(user=request.user), 
    form = NewLimitForm(**{'userObj': request.user})
    return render(request, 'updateDB/addLimit.html', {'NewLimitForm': form})

def addExpense(request):
    return render(request, 'updateDB/addExpense.html', {'NewExpenseForm': NewExpenseForm})

def success(request):
    if 'addBudget' in request.POST:
        print('new budget')
        form = NewBudgetForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            name = form_data['name']
            startDate = form_data['startDate']
            endDate = form_data['endDate']
            show = form_data['show']
            newBudget = Budget.objects.create(name=name, startDate=startDate, endDate=endDate, current=show, user=request.user)
            newBudget.save()
        return render(request, 'updateDB/success.html')

    elif 'addLimit' in request.POST:
        print('new limit')
        # user_details = {'user': request.user}
        form = NewLimitForm(request.POST, **{'userObj': request.user})
        # form.fields['budgetID'] = forms.ModelChoiceField(Budget.objects.filter(user=request.user))
        # print(form.fields['budgetID'])
        # LimitFormSet = modelformset_factory(Limit, fields=('budgetID', 'category', 'amount'), extra=0)
        # data = request.POST or None
        # formset = LimitFormSet(data=data, queryset=Budget.objects.filter(user=request.user))
        # form.fields['budgetID'].queryset = Budget.objects.filter(user=request.user)
        # for form in formset:
        #     form.fields['budgetID'].queryset = Budget.objects.filter(user=request.user)
        if form.is_valid() and request.method =='POST':
            newLimit = form.save(commit=False)
            # newLimit.user = request.user
            # print(request.user)
            newLimit.save()
            # form_data = form.cleaned_data
            # name = form_data['name']
            # budget = form_data['budget']
            # category = form_data['categories']
            # amount = form_data['amount']
            # print(form_data)
            # newLimit = Limit.objects.create(budgetID = budget, category=category, amount=amount)
            # newLimit.save()
        return render(request, 'updateDB/success.html')

    else:
        form = NewExpenseForm(request.POST)
        if form.is_valid():
            newExpense = form.save()
            newExpense.user = request.user
            newExpense.save()
        return render(request, 'updateDB/success.html')