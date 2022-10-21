from django.shortcuts import render,redirect
from .forms import PostForm ,CommentForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form':comment_form,
    }
    return render(request, 'reviews/detail.html', context)

def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        forms = PostForm(request.POST, instance=review)
        if forms.is_valid():
            forms.save()
            return redirect('reviews:detail', review_pk)
        
    else:
        forms = PostForm(instance=review)
    context = {
        "forms" : forms,
    }
    return render(request, 'reviews/update.html', context)

def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if review.user == request.user:
        review.delete()
        return redirect('reviews:index')
    
    else:
        return HttpResponseForbidden()


def comments(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
           comment= form.save(commit=False)
           comment.user = request.user 
           comment.review = review
           comment.save()
           return redirect('reviews:detail',review_pk)
    
