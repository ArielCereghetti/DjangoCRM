from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    try:
        if request.user:
            return HttpResponseRedirect('login')
    except:
        return render(request, 'CRM/index.html')


def login(request):
    pass

def register(request):
    return render(request, "CRM/register.html")