from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import IncomeCategoryForm, ChangeIncomeCategoryForm, DeleteIncomeCategoryForm, ExpenseCategoryForm, \
    ChangeExpenseCategoryForm, DeleteExpenseCategoryForm, DeleteRecord, ChangeRecord
from .models import IncomeCategory, ExpenseCategory, Budget, Income, Expense
from itertools import chain
from datetime import datetime, timedelta
import random


@login_required()
def history(request):
    income_records = Income.objects.filter(budget=request.user.budget)
    expense_records = Expense.objects.filter(budget=request.user.budget)
    records = reversed(sorted(chain(income_records, expense_records), key=lambda instance: instance.date_time))
    context = {
        'records': records
    }
    if request.method == "POST":
        if 'delete_record' in request.POST:
            form = DeleteRecord(request.POST)
            if form.is_valid():
                record_id = form.cleaned_data['record_id']
                record_type = form.cleaned_data['record_type']
                if record_type == "Income":
                    record = Income.objects.filter(budget=request.user.budget, id=record_id)
                    record.delete()
                elif record_type == "Expense":
                    record = Expense.objects.filter(budget=request.user.budget, id=record_id)
                    record.delete()
        elif 'change_record' in request.POST:
            form = ChangeRecord(request.POST)
            if form.is_valid():
                record_id = form.cleaned_data['record_id']
                record_type = form.cleaned_data['record_type']
                new_value = form.cleaned_data['new_value']
                if record_type == "Income":
                    record = Income.objects.get(budget=request.user.budget, id=record_id)
                    record.amount = new_value
                    record.save()
                elif record_type == "Expense":
                    record = Expense.objects.get(budget=request.user.budget, id=record_id)
                    record.amount = new_value
                    record.save()
        income_records = Income.objects.filter(budget=request.user.budget)
        expense_records = Expense.objects.filter(budget=request.user.budget)
        records = reversed(sorted(chain(income_records, expense_records), key=lambda instance: instance.date_time))
        context = {
            'records': records
        }
        return render(request, 'FinanceManager/history.html', context)

    return render(request, 'FinanceManager/history.html', context)


@login_required()
def income(request):
    if request.method == "POST":
        if "add_category" in request.POST:
            form = IncomeCategoryForm(request.POST)
            if form.is_valid():
                category_name = form.cleaned_data['category_name']
                if not IncomeCategory.objects.filter(budget=request.user.budget, category_name=category_name):
                    IncomeCategory.objects.create(budget=request.user.budget, category_name=category_name).save()
        if "change_category" in request.POST:
            form = ChangeIncomeCategoryForm(request.POST)
            if form.is_valid():
                current_category_name = form.cleaned_data['current_category_name']
                new_category_name = form.cleaned_data['new_category_name']
                category = get_object_or_404(IncomeCategory, budget=request.user.budget,
                                             category_name=current_category_name)
                if category and not IncomeCategory.objects.filter(budget=request.user.budget,
                                                                  category_name=new_category_name):
                    category.category_name = new_category_name
                    category.save()
        if "delete_category" in request.POST:
            form = DeleteIncomeCategoryForm(request.POST)
            if form.is_valid():
                current_category_name = form.cleaned_data['current_category_name']
                category = get_object_or_404(IncomeCategory, budget=request.user.budget,
                                             category_name=current_category_name)
                category.delete()

    return render(request, 'FinanceManager/income.html')


@login_required()
def expenses(request):
    if request.method == "POST":
        if "add_category" in request.POST:
            form = ExpenseCategoryForm(request.POST)
            if form.is_valid():
                category_name = form.cleaned_data['category_name']
                if not ExpenseCategory.objects.filter(budget=request.user.budget, category_name=category_name):
                    ExpenseCategory.objects.create(budget=request.user.budget,
                                                   category_name=category_name).save()
                    return render(request, 'FinanceManager/expenses.html')
        if "change_category" in request.POST:
            form = ChangeExpenseCategoryForm(request.POST)
            if form.is_valid():
                current_category_name = form.cleaned_data['current_category_name']
                new_category_name = form.cleaned_data['new_category_name']
                category = get_object_or_404(ExpenseCategory, budget=request.user.budget,
                                             category_name=current_category_name)
                if category and not ExpenseCategory.objects.filter(budget=request.user.budget,
                                                                   category_name=new_category_name):
                    category.category_name = new_category_name
                    category.save()
                    return render(request, 'FinanceManager/expenses.html')
        if "delete_category" in request.POST:
            form = DeleteExpenseCategoryForm(request.POST)
            if form.is_valid():
                current_category_name = form.cleaned_data['current_category_name']
                category = get_object_or_404(ExpenseCategory, budget=request.user.budget,
                                             category_name=current_category_name)
                category.delete()
                return render(request, 'FinanceManager/expenses.html')

    return render(request, 'FinanceManager/expenses.html')


@login_required()
def general_statistics(request):
    return render(request, 'FinanceManager/general-statistics.html')


@login_required()
def daily(request):
    return render(request, 'FinanceManager/daily.html')


@login_required()
def home(request):
    return render(request, 'FinanceManager/home.html')


@login_required()
def profile(request):
    return render(request, 'FinanceManager/profile.html')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return ("rgb" + str(tuple(rgb)))

@login_required()
def start(request):
    expense_set = request.user.budget.expense_set.filter(date_time__gte=datetime.now() - timedelta(days=7)).order_by(
        'category__category_name')
    expense_categories = expense_set.values_list('category__category_name', flat=True).distinct()
    income_set = request.user.budget.income_set.filter(date_time__gte=datetime.now() - timedelta(days=7)).order_by(
        'category__category_name')
    income_categories = income_set.values_list('category__category_name', flat=True).distinct()

    labels1 = []
    data1 = []
    backgroundcolor1 = []

    labels2 = []
    data2 = []
    backgroundcolor2 = []

    for category in expense_categories:
        values = expense_set.filter(category__category_name=category).values_list('amount', flat=True)
        expense_sum = sum(values)
        labels1.append(category)
        data1.append(expense_sum)
        backgroundcolor1.append(random_color())
        all_sum1 = sum(data1)

    for category in income_categories:
        values = income_set.filter(category__category_name=category).values_list('amount', flat=True)
        income_sum = sum(values)
        labels2.append(category)
        data2.append(income_sum)
        backgroundcolor2.append(random_color())
        all_sum2 = sum(data2)

    context = {
        "labels1": labels1,
        "data1": data1,
        "backgroundColor1": backgroundcolor1,
        "all_sum1": all_sum1,
        "labels2": labels2,
        "data2": data2,
        "backgroundColor2": backgroundcolor2,
        "all_sum2": all_sum2
    }

    return render(request, 'FinanceManager/start.html', context)
