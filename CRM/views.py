from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    try:
        if request.user:
            return HttpResponseRedirect('login')
    except:
        return render(request, 'CRM/index.html')

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        else:
            return render(request, 'CRM/login.html', {"form": form })

def login(request):
    pass
def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            print(request.POST)
        else:
            return render(request, "CRM/register.html", {
                "form": RegisterUser(),
                "message": "One or more fields were incorrect, please try again"
            })


    return render(request, "CRM/register.html", {
        "form": RegisterUser(),
    })