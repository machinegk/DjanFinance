from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import IncomeCategoryForm, ChangeIncomeCategoryForm, DeleteIncomeCategoryForm, ExpenseCategoryForm, \
    ChangeExpenseCategoryForm, DeleteExpenseCategoryForm, DeleteRecord, ChangeRecord
from .models import IncomeCategory, ExpenseCategory, Budget, Income, Expense
from itertools import chain


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

@login_required()
def start(request):
    return render(request, 'FinanceManager/start.html')
