from django.contrib import admin
from .models import *


admin.site.register(Budget)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseCategory)
admin.site.register(Income)
admin.site.register(Expense)

