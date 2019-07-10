from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from crispy_forms.bootstrap import PrependedText
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta
from .models import *

class NewBudgetForm(forms.ModelForm):
    # Crispy Forms
    helper = FormHelper()

    class Meta:
        model = Budget
        fields = ['name', 'startDate', 'endDate', 'current']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-5'}),
            'startDate': forms.DateInput(attrs={'class': 'form-control datepicker col-md-5'}),
            'endDate': forms.DateInput(attrs={'class': 'form-control datepicker col-md-5'})
        }
        labels = {
            'current': 'Show'
        }

class NewLimitForm(forms.ModelForm):
    # Crispy Forms
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NewLimitForm, self).__init__ (*args, **kwargs)
        self.fields['budgetID'].queryset = Budget.objects.filter(user=user)
    class Meta:
        model = Limit
        fields = ['budgetID', 'category', 'amount']
        widgets = {
            'budgetID': forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle form-control col-md-5',
                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
            'category': forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle form-control col-md-5',
                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control col-md-5'}),
        }
        

class NewExpenseForm(forms.ModelForm):
    # Crispy Forms
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NewExpenseForm, self).__init__ (*args, **kwargs)
        self.fields['budgetID'].queryset = Budget.objects.filter(user=user)

    class Meta:
        model = Expense
        fields = ['budgetID', 'category', 'date', 'title', 'amount', 'description']
        widgets = {
            'budgetID': forms.Select(attrs={'class': 'btn btn-light dropdown-toggle form-control col-md-5',
                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
            'title': forms.TextInput(attrs={'class': 'form-control col-md-5'}),
            'description': forms.Textarea(attrs={'rows':4, 'cols':10, 'class': 'form-control col-md-5'}),
            'date': forms.DateInput(attrs={'class': 'form-control datepicker col-md-5'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control col-md-5'}),
            'category': forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle form-control col-md-5',
                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
        }
        labels = {
            'budgetID': 'Budget Name',
            'amount': 'Amount ($)'
        }
    
class NewCategoryForm(forms.ModelForm):
    # Crispy Forms
    helper = FormHelper()
    class Meta:
        model = Category
        fields = ['category']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control col-md-5'})
        }

