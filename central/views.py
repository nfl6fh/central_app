from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
def profile(request, user_id):
    user = get_object_or_404(auth_user, pk=user_id)
    central_user = get_object_or_404(User, auth_user=user)
    upcoming_absences = central_user.absences.filter()
    context = {
        'central_user': central_user,
        'absences': upcoming_absences
    }
