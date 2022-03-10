from re import template
from django.shortcuts import render

from django.views.generic import ListView ,DetailView ,DeleteView, CreateView ,UpdateView
from django.urls import reverse_lazy
from .models import Teams

class TeamsListView(ListView):
  template_name = 'teams_list.html'
  model = Teams

class TeamsDetailView(DetailView):
  template_name = 'teams_detail.html'
  model = Teams

class TeamsDeleteView(DeleteView):
  template_name = 'teams_delete.html'
  model = Teams

class TeamsCreateView(CreateView):
  template_name = 'teams_create.html'
  model = Teams
  fields =['name' ,'trophy', 'rater']

class TeamsUpdateView(UpdateView):
  template_name = 'teams_update.html'
  model = Teams
  fields =['name' ,'trophy' ,'rater']
