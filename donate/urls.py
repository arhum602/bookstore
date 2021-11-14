from django.urls import path

from . import views

app_name = 'donate'

urlpatterns = [
    path('books/', views.DonateBooks, name='donate_books'),
]
