from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Customer, Manager


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone = self.cleaned_data.get("phone")
        customer.address = self.cleaned_data.get("address")
        customer.save()
        return user

class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        manager = Manager.objects.create(user=user)
        manager.phone = self.cleaned_data.get("phone")
        manager.save()
        return user
