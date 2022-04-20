from django import forms

from reservations.models import Chambre, Reservation


class AjoutChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['chambre_type', 'chambre_status', 'prix', 'chambre_numero']


class AjoutReservationForm(forms.ModelForm):
    debut_sejour = forms.DateField(required=True, widget=forms.DateInput(
        format=('%d/%m/%y'),
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'
               }
    ))
    fin_sejour = forms.DateField(required=True, widget=forms.DateInput(
        format=('%d/%m/%y'),
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'
               }
    ))

    class Meta:
        model = Reservation
        fields = ['debut_sejour', 'fin_sejour']


class EditReservationForm(forms.ModelForm):
    debut_sejour = forms.DateField(required=True, widget=forms.DateInput(

        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'text'
               }
    ))
    fin_sejour = forms.DateField(required=True, widget=forms.DateInput(

        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'text'
               }
    ))

    class Meta:
        model = Reservation
        fields = ['debut_sejour', 'fin_sejour']
