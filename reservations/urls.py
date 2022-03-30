from django.urls import path
from . import views

urlpatterns = [

    path('new_room/', views.newRoom, name='new_room'),
    path('', views.RoomView.as_view(), name='rooms'),

]
