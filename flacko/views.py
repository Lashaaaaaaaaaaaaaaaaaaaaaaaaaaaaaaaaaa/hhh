from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Jordy, Lord
from .forms import JordyForm, LordForm


class JordyListView(ListView):
    model = Jordy
    template_name = 'jordys/jordy_list.html'
    context_object_name = 'jordys'


class JordyDetailView(DetailView):
    model = Jordy
    template_name = 'jordys/jordy_detail.html'


class JordyCreateView(CreateView):
    model = Jordy
    form_class = JordyForm
    template_name = 'jordys/jordy_edit.html'
    success_url = reverse_lazy('jordy_list')


class JordyUpdateView(UpdateView):
    model = Jordy
    form_class = JordyForm
    template_name = 'jordys/jordy_edit.html'
    success_url = reverse_lazy('jordy_list')


class JordyDeleteView(DeleteView):
    model = Jordy
    template_name = 'jordys/jordy_confirm_delete.html'
    success_url = reverse_lazy('jordy_list')


class LordListView(ListView):
    model = Lord
    template_name = 'lords/lord_list.html'
    context_object_name = 'lords'


class LordDetailView(DetailView):
    model = Lord
    template_name = 'lords/lord_detail.html'


class LordCreateView(CreateView):
    model = Lord
    form_class = LordForm
    template_name = 'lords/lord_edit.html'
    success_url = reverse_lazy('lord_list')


class LordUpdateView(UpdateView):
    model = Lord
    form_class = LordForm
    template_name = 'lords/lord_edit.html'
    success_url = reverse_lazy('lord_list')


class LordDeleteView(DeleteView):
    model = Lord
    template_name = 'lords/lord_confirm.delete.html'
    success_url = reverse_lazy('lord_list')