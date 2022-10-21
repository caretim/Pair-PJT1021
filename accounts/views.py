from django.shortcuts import render
from .forms import MakeUserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = MakeUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'base.html')

    else:
        forms = MakeUserForm()
    context = {
        "forms" : forms,
    }
    return render(request, "accounts/signup.html", context)