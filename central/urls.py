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
    path('profile', TemplateView.as_view(template_name='central/profile.html'), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create_user/<int:user_id>/', views.create_user, name='create_user'),
    path('coaches_view', views.CoachesView.as_view(), name='coaches_view'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('navbar/', TemplateView.as_view(template_name='central/navbar.html'), name='navbar'),
    path(r'*/navbar/', TemplateView.as_view(template_name='central/navbar.html'), name='navbar'),
    path(r'*/navbar', TemplateView.as_view(template_name='central/navbar.html'), name='navbar'),
    path('<int:pk>/profile', views.ProfileView.as_view(), name='profile_personal')
]
