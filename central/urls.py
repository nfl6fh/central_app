from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from . import views

app_name='central'
urlpatterns = [
    path('', TemplateView.as_view(template_name="central/index.html"), name='home'),
    path('extra_work', TemplateView.as_view(template_name='central/ew.html'), name='extra_work'),
    path('absences', TemplateView.as_view(template_name='central/absences.html'), name='absences'),
    path('<int:user_id>/profile/', views.profile, name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
]
