from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.


def profile(request, user_id):
    user = get_object_or_404(auth_user, pk=user_id)
    central_user = get_object_or_404(User, auth_user=user)
    upcoming_absences = central_user.absences.filter()
    context = {
        'central_user': central_user,
        'absences': upcoming_absences
    }


def create_user(request, user_id):
    print(request.POST)
    a_user = get_object_or_404(auth_user, pk=user_id)
    context = {}
    if 'name' not in request.POST or request.POST['name'] == '':
        context['retry'] = 'true'
        context['bad_input'] = 'name'
        return render(request, 'central/index.html', context)
    elif 'email' not in request.POST or request.POST['email'] == '':
        context['retry'] = 'true'
        context['bad_input'] = 'email'
        return render(request, 'central/index.html', context)
    elif 'is_rookie' not in request.POST:
        context['retry'] = 'true'
        context['bad_input'] = 'is_rookie'
        return render(request, 'central/index.html', context)
    elif ('is_starboard' not in request.POST and 'is_port' not in request.POST):
        context['retry'] = 'true'
        context['bad_input'] = 'side'
        return render(request, 'central/index.html', context)
    user = User.objects.get_or_create(auth_user=a_user, name=request.POST['name'],
                                      grad_year=request.POST['grad_year'], is_starboard=(
                                          'is_starboard' in request.POST), is_port=('is_port' in request.POST), is_rookie=request.POST['is_rookie'], email=request.POST['email'])
    return HttpResponseRedirect(reverse('central:home'))

class CoachesView(LoginRequiredMixin, generic.TemplateView):
    template_name='central/coaches_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unapproved_users'] = User.objects.filter(is_approved=False)
        print(f'context: {context}')
        return context

def edit_user(request, user_id):
    a_user = get_object_or_404(auth_user, pk=user_id)
    user = get_object_or_404(User, auth_user=a_user)

    print(request)

    if 'name' in request.POST:
        user.name = request.POST['name']
    if 'email' in request.POST:
        user.email = request.POST['email']
    if 'grad_year' in request.POST:
        user.grad_year = request.POST['grad_year']
    if 'is_port' in request.POST:
        user.is_port = request.POST['is_port']
    elif user.is_port:
        user.is_port = False
    if 'is_starboard' in request.POST:
        user.is_starboard = request.POST['is_starboard']
    elif user.is_starboard:
        user.is_starboard = False
    if 'is_rookie' in request.POST:
        user.is_rookie = request.POST['is_rookie']
    user.save()

    return HttpResponseRedirect(reverse('central:profile'))

class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = auth_user
    template_name = 'central/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(auth_user=self.request.user).first()
        context['lineup'] = user.boats_rowed.order_by('-date').first()
        return context

def accept_user(request, user_id):
    pass

def decline_user(request, user_id):
    pass