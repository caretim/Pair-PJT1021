from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def create(request):
    if request.method == "POST":
        forms = PostForm(request.POST)
        if forms.is_valid():
            review = forms.save(commit=False)
            review.user = request.user
            review.save()
            return render(request, 'base.html')
    
    else:
        forms = PostForm()
    context = {
        "forms" : forms,
    }
    return render(request, 'reviews/create.html', context)