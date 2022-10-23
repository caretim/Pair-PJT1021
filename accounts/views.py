from django.shortcuts import render, redirect
from .forms import MakeUserForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login, logout as my_logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = MakeUserForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            my_login(request, user)
            return redirect("reviews:index")
    else:
        forms = MakeUserForm()
    context = {
        "forms": forms,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            my_login(request, form.get_user())
            return redirect(request.GET.get("next") or "reviews:index")
    else:
        form = AuthenticationForm()
    context = {"forms": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    my_logout(request)
    return redirect("reviews:index")


@login_required
def update(request, user_pk):
    infos = get_user_model().objects.get(pk=user_pk)

    if request.method == "POST":
        forms = ChangeUserForm(request.POST, request.FILES, instance=infos)
        if forms.is_valid():
            forms.save()
            # my_login(request, user)
            return redirect("accounts:user_detail", user_pk)
    else:
        forms = ChangeUserForm(instance=infos)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/update.html", context)


@login_required
def user_detail(request, user_pk):
    pick_user = get_user_model().objects.get(pk=user_pk)
    context = {
        "pick_user": pick_user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def delete(request, user_pk):
    pick_user = get_user_model().objects.get(pk=user_pk)

    if pick_user.pk == request.user.pk:
        pick_user.delete()

    return render(request, "accounts/detail.html")
