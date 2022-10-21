from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Review
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create(request):
    if request.method == "POST":
        forms = PostForm(request.POST)
        if forms.is_valid():
            review = forms.save(commit=False)
            review.user = request.user
            review.save()
            return redirect ('reviews:index')
    else:
        forms = PostForm()
    context = {
        "forms" : forms,
    }
    return render(request, 'reviews/create.html', context)


def index(request):
    all_data = Review.objects.order_by('-pk')
    context = {
        'all_data' : all_data,
    }
    return render(request, 'reviews/index.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)