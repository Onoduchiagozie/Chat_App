from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from chat.forms import SignUpForm

from django.contrib.auth.models import User

def index(request):
    return render(request, 'chat/index.html')



def room(request, room_name):
    user=User.objects.all()
    selected_user=User.objects.get(username=room_name)


    return render(request, 'chat/room.html', {
        'room_name': room_name,
        "user":user,
        "current_user":selected_user

    })



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'chat/register.html'

class CustomLoginView(LoginView):
    template_name='chat/login.html'
    success_url = reverse_lazy('index')
