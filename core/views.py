from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'core/index.html')


@login_required(login_url="/admin")
def login(request):
    return render(request,'core/authentication.html')