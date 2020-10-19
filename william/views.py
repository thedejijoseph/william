
import posixpath

from django.conf import settings
from django.shortcuts import render


def index(request):
    return render(request, 'william/index.html')