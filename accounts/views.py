from django.shortcuts import render, redirect
from .forms import MakeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import login as my_login , logout as my_logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = MakeUserForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            my_login(request, user)
            return redirect ('reviews:index')
    else:
        forms = MakeUserForm()
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect (request.GET.get('next') or  'reviews:index')
    else:
        form = AuthenticationForm()
    context={
        'forms':form
    }
    return render(request, "accounts/login.html",context)


def logout(request):
    my_logout(request)
    return redirect ('reviews:index')