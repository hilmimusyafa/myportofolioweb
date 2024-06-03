from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import skills
from .models import certification
from .models import myprojects

from .forms import ContactForm
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def aboutme(request):
    all_skills = skills.objects.all()
    all_certifications = certification.objects.all()
    context = {
        'skills': all_skills,
        'certifications': all_certifications
    }
    return render(request, 'pages/aboutme.html', context)

def projects(request):
    template_name = 'pages/projects.html'
    queryset = myprojects.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def projects_detail(request, slug):
    template_name = 'pages/projects_detail.html'
    obj = myprojects.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simpan data ke database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']

            contact = Contact.objects.create(
                name = name,
                email = email,
                title = title,
                message = message
            )

            return render(request, 'pages/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

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

