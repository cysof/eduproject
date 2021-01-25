from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,TemplateView, CreateView,)
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Project, Department, Contact

class Payment(TemplateView):
    template_name = 'payment.html'


class About(TemplateView):
    template_name= 'about.html'

class Hirewriter(TemplateView):
    template_name = 'hirewriter.html'

class Success(TemplateView):
    template_name = 'thanks.html'





class Index(ListView):
    model= Project
    paginate_by = 1
    queryset = Project.objects.all()
    template_name = 'index.html'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'content.html'


class DepartmentListView(ListView):
    model = Department
    template_name = 'department.html'

class ProjectList(ListView):
    model = Project
    template_name = 'projectlist.html'


class Contact(CreateView):
    model = Contact
    template_name = 'contact.html'
    success_url =('thanks')
