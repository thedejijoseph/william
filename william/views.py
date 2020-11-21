
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from markdown import markdown

def index(request):
    readme = settings.BASE_DIR.joinpath('README.md').read_text()
    html = markdown(readme, extensions=['markdown.extensions.tables'])
    return HttpResponse(html)
