from django.shortcuts import render, redirect
from .forms import MakeUserForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login, logout as my_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
    pick_user = infos
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
        'pick_user':pick_user
    }
    return render(request, "accounts/update.html", context)


@login_required
def user_detail(request, user_pk):
    pick_user = get_user_model().objects.get(pk=user_pk)
    p_page = request.GET.get("postpage")  # postpage=3
    c_page = request.GET.get("comment_page")
    if not c_page:
        status = 0
    else:
        status = 1

    user_post = pick_user.review_set.all()
    post_data = Paginator(user_post, 5)

    user_comment = pick_user.comment_set.all()
    comment_data = Paginator(user_comment, 5)

    post_page = post_data.get_page(p_page)
    comment_page = comment_data.get_page(c_page)

    context = {
        "pick_user": pick_user,
        "post_page": post_page,
        "comment_page": comment_page,
        "status": status,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def delete(request, user_pk):
    return render(request, "accounts/delete.html")


@login_required
def realdelete(request, user_pk):
    pick_user = get_user_model().objects.get(pk=user_pk)
    if pick_user.pk == request.user.pk:
        pick_user.delete()
    return redirect("reviews:index")
