from django import forms
from .models import Reservation, Room


class NewReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_day', 'end_day', 'amount']


class NewRoomForm(forms.ModelForm):
    star_date=forms.DateField(required=True,widget=forms.DateInput(
        format=('%d/%m/%y'),
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
                'type':'date'
               }
             ))

    class Meta:
        model = Room
        fields = ['room_no', 'room_type','price','star_date']
