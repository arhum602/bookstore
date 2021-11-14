from django.shortcuts import render

def DonateBooks(request):
    return render(request, 'donate/donatebooks.html' )
