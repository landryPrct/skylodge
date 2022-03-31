from django import forms

from reservations.models import Chambre


class AjoutChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['chambre_type', 'chambre_status', 'prix', 'chambre_numero']
