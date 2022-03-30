from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from reservations.models import Room
from accounts.models import Manager
from reservations.forms import NewRoomForm


# Create your views here.


def home(request):
    return render(request, '../templates/home.html')



class RoomView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'rooms.html'


@login_required
def newRoom(request):
    if request.method == 'POST':
        form = NewRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            my_room = Manager.objects.get(user=request.user)
            room.manager = my_room
            room.save()
            return redirect('home')
    else:
        form = NewRoomForm()
    return render(request, 'new_room.html', {'form': form})

#
# @login_required
# def newReservation(request):
#     if request.method == 'POST':
#         form = NewReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation
