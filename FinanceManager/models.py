from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " Budget"


class IncomeCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    income_category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.budget.user.username + " - Category: " + self.income_category_name

class ExpenseCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    expense_category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.budget.user.username + " - Category: " + self.expense_category_name

class Income(models.Model):
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    income_amount = models.IntegerField()

    def __str__(self):
        return self.income_category.budget.user.username + " - " + str(self.income_amount) + ' - ' + self.income_category.income_category_name
class Expense(models.Model):
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    expense_amount = models.IntegerField()

    def __str__(self):
        return self.expense_category.budget.user.username + " - " + str(self.expense_amount) + ' - ' + self.expense_category.expense_category_name
