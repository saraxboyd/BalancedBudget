from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def get_ordering(self, request): # orders entries alphabetically
        return ['category']
admin.site.register(Category, CategoryAdmin)

class LimitAdmin(admin.TabularInline):
    model = Limit
class ExpenseAdmin(admin.TabularInline):
    model = Expense
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'startDate', 'endDate') # information to be displayed on the model page
    # list_filter = ('category', 'location') # add filter options
    # enables editing these models within the same page as the orgnaizaiton admin page
    inlines = [LimitAdmin, ExpenseAdmin]
    search_fields = ['name'] # adds type in search bar for organizaiton name
    def get_ordering(self, request): # orders entries by start date
        return ['startDate']

admin.site.register(Budget, BudgetAdmin)