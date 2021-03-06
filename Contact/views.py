from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from .models import Contacts
from .forms import ContactsForms


class List(ListView):
    paginate_by = 10
    model = Contacts
    queryset = Contacts.objects.all().order_by('id')
    template_name = 'List.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        qsearch = self.request.GET.get('txtSearch')
        object_list = Contacts.objects.all().order_by('id')
        if qsearch:
            object_list = self.model.objects.filter(Q(phone__icontains=qsearch) | Q(name__icontains=qsearch))
        return object_list


class Create(CreateView):
    model = Contacts
    form_class = ContactsForms
    template_name = 'Add.html'
    success_url = '/'


class Delete(DeleteView):
    model = Contacts
    pk_url_kwarg = 'pk'
    template_name = 'Delete.html'
    success_url = '/'


class Update(UpdateView):
    model = Contacts
    form_class = ContactsForms
    pk_url_kwarg = 'pk'
    template_name = 'Edit.html'
    success_url = '/'
