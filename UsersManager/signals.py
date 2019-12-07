from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from FinanceManager.models import Budget, ExpenseCategory, IncomeCategory

@receiver(post_save, sender=User)
def create_budget(sender, instance, created, **kwargs):
    if created:
        Budget.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_budget(sender, instance, created, **kwargs):
    instance.budget.save()

@receiver(post_save, sender=Budget)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        IncomeCategory.objects.bulk_create([
            IncomeCategory(budget=instance, income_category_name='Salary'),
            IncomeCategory(budget=instance, income_category_name='Deposit'),
            IncomeCategory(budget=instance, income_category_name='Saving'),
        ])
        ExpenseCategory.objects.bulk_create([
            ExpenseCategory(budget=instance, expense_category_name='Bills'),
            ExpenseCategory(budget=instance, expense_category_name='House'),
            ExpenseCategory(budget=instance, expense_category_name='Pets'),
            ExpenseCategory(budget=instance, expense_category_name='Health'),
            ExpenseCategory(budget=instance, expense_category_name='Entertainment'),
            ExpenseCategory(budget=instance, expense_category_name='Food'),
            ExpenseCategory(budget=instance, expense_category_name='Car'),
        ])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()