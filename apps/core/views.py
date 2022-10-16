from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'core/home.html')


def index(request):
    return render(request, 'index.html')
