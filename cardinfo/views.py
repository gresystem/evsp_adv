from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Cardinfo

# Create your views here.

class CardinfoList(ListView):
  model = Cardinfo
  template_name='cardinfo.html'
  context_object_name = 'cardinfoList'
  paginate_by = 2
  queryset = Cardinfo.objects.all()


  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   user_id = self.request.session['user']
  #   print(user_id)
  #   context['loginuser'] = user_id
  #   return context

class CardinfoDetail(DetailView):
  template_name='cardinfo_detail.html'
  queryset = Cardinfo.objects.all()
  context_object_name = 'cardinfo'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class CardinfoCreateView(CreateView):
  model = Cardinfo
  template_name = 'cardinfo_register.html'
  fields = ['cardname', 'cardtag', 'username']
  success_url = '/cardinfo'

class CardinfoDeleteView(DeleteView):
  model = Cardinfo
  template_name='cardinfo_confirm_delete.html'
  success_url = '/cardinfo'

class CardinfoUpdateView(UpdateView):
  model = Cardinfo
  template_name='cardinfo_update.html'
  fields = [ 'cardname', 'username', 'cardstatus']
  success_url = '/cardinfo'