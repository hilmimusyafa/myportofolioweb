from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import myprojects

# Create your views here.

def projects(request):
    template_name = 'projects.html'
    queryset = myprojects.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def projects_detail(request, slug):
    template_name = 'projects.html'
    obj = myprojects.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)

class MyProjectsDetailView(DetailView):
    model = myprojects
    queryset = myprojects.objects.all()

class MyProjectsListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = myprojects.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = myprojects.objects.all()
        return queryset

