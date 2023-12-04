from django.views.generic import ListView, CreateView
from .models import Tip
from .forms import TipForm
from django.urls import reverse_lazy

class TipsView(ListView):
   model = Tip
   template_name = 'tips.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['user'] = self.request.user
       return context

class AddTipView(CreateView):
   model = Tip
   template_name = 'add_tip.html'
   form_class = TipForm
   success_url = reverse_lazy('tips:tips')

   def form_valid(self, form):
      self.object = form.save(commit=False)
      if self.request.user.is_authenticated:
          self.object.user = self.request.user
      else:
        self.object.user = None
      self.object.save()
      return super().form_valid(form)
