from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('bookflight', views.booking, name="bookflight"),
    path('', views.index, name="index"),
    path('register', views.newUser, name="register"),
    path('flights', views.flights, name="flights"),
    path('itenery', views.userprofile, name="itenery"),
    path('account_info', views.actinfo, name="account_info"),
    path('ticket', views.newTicket, name="ticket"),
    path('alltickets', views.vewTicket, name="alltickets"),
    path('alltickets/<pk>', views.vewTicket, name="alltickets_w"),
    path('bookng', views.save_bookng, name="bookng"),
]