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
    return HttpResponse('User being edited')