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
            IncomeCategory(budget=instance, category_name='Salary', category_icon='<i class="fas fa-money-bill-alt fa-7x"></i>'),
            IncomeCategory(budget=instance, category_name='Deposit', category_icon='<i class="fas fa-university fa-7x"></i>'),
            IncomeCategory(budget=instance, category_name='Saving', category_icon='<i class="fas fa-piggy-bank fa-7x"></i>'),
        ])
        ExpenseCategory.objects.bulk_create([
            ExpenseCategory(budget=instance, category_name='Bills', category_icon='<i class="fas fa-file-invoice-dollar fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='House', category_icon='<i class="fas fa-home fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='Pets', category_icon='<i class="fas fa-paw fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='Health', category_icon='<i class="fas fa-heartbeat fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='Entertainment', category_icon='<i class="fas fa-futbol fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='Food', category_icon='<i class="fas fa-hamburger fa-7x"></i>'),
            ExpenseCategory(budget=instance, category_name='Car', category_icon='<i class="fas fa-car fa-7x"></i>'),
        ])


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()