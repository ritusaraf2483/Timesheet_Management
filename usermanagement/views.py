from django.shortcuts import render
from django.views.generic import ListView

from usermanagement.models import User


class users_list(ListView):
    model = User
    template_name = 'users/users_list.html'