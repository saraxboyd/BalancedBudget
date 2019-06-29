from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta
from .models import *

class NewBudgetForm(forms.Form):
    name = forms.CharField(required=True)
    startDate = forms.DateField()
    endDate = forms.DateField()
    show = forms.BooleanField()

# class NewLimitForm(forms.Form):
#     def __init__(self, userInfo, *args, **kwargs):
#         # user_details = userInfo
#         # print('user_info: ', userInfo)
#         # print('user_details: ', user_details)
#         # kwargs.pop('user')
#         super(NewLimitForm, self).__init__(*args, **kwargs)
#         print('before widget')
#         print(userInfo)
#         print(type(userInfo))
#         self.fields['budgets']= forms.ChoiceField(choices=[(o.name) for o in Budget.objects.filter(user=userInfo)])
#         print(self.fields)
#         print('after widget')
        

    
#     budget = forms.ModelChoiceField(queryset=Budget.objects.order_by('name'), 
#                                         required=True,
#                                         widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
#                                             'type' : 'button', 'data-toggle' : 'dropdown'}),
#                                         initial=0,)
#     categories = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
#                                             required=True, 
#                                             widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
#                                                                 'type' : 'button', 'data-toggle' : 'dropdown'}),
#                                             initial=0,
#                                             )
#     amount = forms.FloatField(min_value=0.0, required=True)

class NewLimitForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
                                        required=True, 
                                        widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
                                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
                                        initial=0,
                                        )
    budgetID = forms.ModelChoiceField(queryset=Budget.objects.order_by('name'), 
                                        required=True,
                                        widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
                                            'type' : 'button', 'data-toggle' : 'dropdown'}),
                                        initial=0,)
    
    # def __init__(self, userInfo, *args, **kwargs):
        # nonlocal user
        # user = None
        # user_details = userInfo
        # print('user_info: ', userInfo)
        # print('user_details: ', user_details)
        # kwargs.pop('user')
        # super().__init__(userInfo, *args, **kwargs)
        # nonlocal user
        # user = userInfo
        # print('before widget')
        # print(userInfo)
        # print(type(userInfo))
        # budgetID = forms.ModelChoiceField(queryset=Budget.objects.filter(user=userInfo))
        # print(self.fields)
        # print('after widget')
        # self.fields['budgetID'] = forms.ModelChoiceField(queryset=Budget.objects.filter(user=userInfo),
        #                                 required=True,
        #                                 widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
        #                                     'type' : 'button', 'data-toggle' : 'dropdown'}),
        #                                 initial=0,)
        # self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
        #                                 required=True, 
        #                                 widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
        #                                                     'type' : 'button', 'data-toggle' : 'dropdown'}),
        #                                 initial=0,
        #                                 )
    def __init__(self, user, *args, **kwargs):
        print('in constructor')
        self.user = kwargs.pop('userObj')
        print(user)
        super(NewLimitForm, self).__init__(self, *args, **kwargs)
        # if user is not None:
        self.fields['budgetID'].queryset = Budget.objects.filter(user=self.user)
    class Meta:
        print('in Meta')
        model = Limit
        fields = ['budgetID', 'category', 'amount']
        

class NewExpenseForm(forms.ModelForm):
#     name = forms.CharField(required=True)
#     categories = forms.ModelChoiceField(queryset=Category.objects.order_by('category'), 
#                                             required=True, 
#                                             widget=forms.Select(attrs={'class' : 'btn btn-light dropdown-toggle',
#                                                                 'type' : 'button', 'data-toggle' : 'dropdown'}),
#                                             initial=0
#                                             )
    class Meta:
        model = Expense
        fields = ['budgetID', 'title', 'description', 'date', 'amount', 'category']

