from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def history(request):
    return render(request, 'FinanceManager/history.html')

@login_required()
def income(request):
    return render(request, 'FinanceManager/income.html')

@login_required()
def expenses(request):
    return render(request, 'FinanceManager/expenses.html')

@login_required()
def general_statistics(request):
    return render(request, 'FinanceManager/general-statistics.html')
@login_required()
def cash_card(request):
    return render(request, 'FinanceManager/cash-and-card.html')

@login_required()
def daily(request):
    return render(request, 'FinanceManager/daily.html')

@login_required()
def home(request):
    return render(request, 'FinanceManager/home.html')

@login_required()
def profile(request):
    return render(request, 'FinanceManager/profile.html')

