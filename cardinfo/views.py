from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.edit import FormView
from .models import Cardinfo
from .forms import CardinfoCreateRemoteForm

# Create your views here.

def get_cardtag(cpnumber):
  pass

class CardinfoList(ListView):
  model = Cardinfo
  template_name='cardinfo.html'
  context_object_name = 'cardinfoList'
  paginate_by = 2
  queryset = Cardinfo.objects.all()


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

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
  fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
  success_url = '/cardinfo'    

# class CardinfoCreateRemoteView(CreateView):
#   model = Cardinfo
#   template_name = 'cardinfo_register_remote.html'
#   fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
#   success_url = '/cardinfo'   

class CardinfoCreateRemoteView(FormView):
  template_name = 'cardinfo_register_remote.html'
  form_class = CardinfoCreateRemoteForm
  success_url = '/cardinfo'

  def form_valid(self, form):
    cardtag = get_cardtag(form.data.get('cpnumber'))
    # cardinfo = Cardinfo(
    #   cardname = form.cardname,
    #   userid=form.data.get('userid'),
    #   cardtag='1010010112340003',
    #   cardstatus='원격추가'
    # )
    # cardinfo.save()

    print(form.data.get('userid'))
    print(form.data.get('cpnumber'))
    print(form.cardname)
    print(form)

    return super().form_valid(form) 

class CardinfoDeleteView(DeleteView):
  model = Cardinfo
  template_name='cardinfo_confirm_delete.html'
  success_url = '/cardinfo'

class CardinfoUpdateView(UpdateView):
  model = Cardinfo
  template_name='cardinfo_update.html'
  fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
  success_url = '/cardinfo'