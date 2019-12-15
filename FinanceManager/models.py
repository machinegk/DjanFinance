from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " Budget"


class IncomeCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=120)
    category_icon = models.CharField(max_length=50, default='<i class="fas fa-dollar-sign fa-7x"></i>')

    def __str__(self):
        return self.budget.user.username + " - Category: " + self.category_name

class ExpenseCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=120)
    category_icon = models.CharField(max_length=50, default='<i class="fas fa-dollar-sign fa-7x"></i>')

    def __str__(self):
        return self.budget.user.username + " - Category: " + self.category_name

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    type = "Income"
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.budget.user.username + " - " + str(self.amount) + ' - ' + self.category.category_name
class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    type = "Expense"
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.budget.user.username + " - " + str(self.amount) + ' - ' + self.category.category_name
