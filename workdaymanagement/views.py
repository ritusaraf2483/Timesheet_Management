from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from workdaymanagement.forms import WorkdayForm
from workdaymanagement.models import Workday


def home(request):
     return render(request,'home.html')

class get_list(ListView): # Industry norms - ClassName follows CamelCase naming conventions 
     model=Workday
     template_name = 'workday/workday_list.html'

class user_detail(DetailView):
     model=Workday
     template_name = 'workday/workday_detail.html'

class WorkdayCreate(CreateView):
     model=Workday
     form_class = WorkdayForm
     template_name = 'workday/workday_new.html'
     success_url = reverse_lazy("Workday:workday_list")
