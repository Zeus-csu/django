from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return HttpResponse("""<h1>Hola amigo - Adios amigo </h1>
    <h2>type on search bar '/page/home'</h2>""")


class AboutPageView(TemplateView):
    template_name = 'about.html'
