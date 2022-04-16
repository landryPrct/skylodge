from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=("Nom"))
    last_name = forms.CharField(max_length=30, label=("Prénom"))
    display_name = forms.CharField(max_length=30, label=("display name"), help_text=("Will be shown"))

    # email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.display_name = self.cleaned_data['display_name']
        user.save()
