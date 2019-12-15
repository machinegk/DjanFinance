from django import forms

class IncomeCategoryForm(forms.Form):
    category_name = forms.CharField()

class ChangeIncomeCategoryForm(forms.Form):
    current_category_name = forms.CharField()
    new_category_name = forms.CharField()

class DeleteIncomeCategoryForm(forms.Form):
    current_category_name = forms.CharField()


class ExpenseCategoryForm(forms.Form):
    category_name = forms.CharField()

class ChangeExpenseCategoryForm(forms.Form):
    current_category_name = forms.CharField()
    new_category_name = forms.CharField()

class DeleteExpenseCategoryForm(forms.Form):
    current_category_name = forms.CharField()

class DeleteRecord(forms.Form):
    record_id = forms.CharField()
    record_type = forms.CharField()

class ChangeRecord(forms.Form):
    record_id = forms.CharField()
    record_type = forms.CharField()
    new_value = forms.IntegerField()