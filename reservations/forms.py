from django import forms
from django.contrib.auth.models import User

from reservations.models import Chambre, Reservation, Categorie, Payment


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class AjoutCategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['type', 'prix']


class AjoutChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['categorie', 'chambre_status', 'chambre_numero']


class AjoutReservationForm(forms.ModelForm):
    # debut_sejour = forms.DateField(required=True, widget=forms.DateInput(
    #     format=('%d/%m/%y'),
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Select a date',
    #            'type': 'date'
    #            }
    # ))
    # fin_sejour = forms.DateField(required=True, widget=forms.DateInput(
    #     format=('%d/%m/%y'),
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Select a date',
    #            'type': 'date'
    #            }
    # ))

    class Meta:
        model = Reservation
        fields = ['debut_sejour', 'fin_sejour']


class EditReservationForm(forms.ModelForm):
    # debut_sejour = forms.DateField(required=True, widget=forms.DateInput(

    #     attrs={'class': 'form-control',
    #            'placeholder': 'Select a date',
    #            'type': 'text',
    #            'disabled':"True",
    #            }
    # ))
    # fin_sejour = forms.DateField(required=True, widget=forms.DateInput(

    #     attrs={'class': 'form-control',
    #            'placeholder': 'Select a date',
    #            'type': 'text',
    #            'disabled':"True",
    #            }

    # ))

    class Meta:
        model = Reservation
        fields = ['status']


class iHelaClientAccountForm(forms.ModelForm):
    # account = forms.CharField(max_length=50)
    class Meta:
        model = Payment
        fields = ['amount']
